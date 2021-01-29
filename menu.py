from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
from matplotlib.backends.backend_qt5agg import (FigureCanvas)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import select_file
import dashboard
import search

import validation # validates the files
import view # displays the diagram of indicators
import main
import sys

import qtmodern.styles
import qtmodern.windows


class FileWindow(QtWidgets.QMainWindow, select_file.Ui_Form):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.datafile_button.clicked.connect(self.datafile_check)
        self.indfile_button.clicked.connect(self.indfile_check)
        self.ok_button.clicked.connect(self.send_data)
        self.cancel_button.clicked.connect(self.close)

    def datafile_check(self):
        # QFileDialog.getOpenFileName((self,'Open CSV',),os.getenv('Home', 'CSV(*.)'))
        path = QFileDialog.getOpenFileName(self, "Open", "", "CSV Files (*.csv);;All Files (*)")
        if path[0] != '':
            path = path[0]
            print(path)
            check = validation.data_validation(path)
            if check[0]:
                self.df1 = check[1]
                self.indfile_button.setEnabled(True)
                if len(check[2]) == 0:
                    self.output1.setText('Импортированы все {} строк'.format(str(len(self.df1['City']))))
                    self.output1.setStyleSheet('color: green;')
                else:
                    self.output1.setText('Импортированы {} строк\n'
                                         'Строк с ошибками: {}'.format(str(len(self.df1['City'])), str(len(check[2]))))
                    self.output1.setStyleSheet('color: #F0BB15;')
            else:
                self.output1.setText('\n'.join(check[1]))
                self.output1.setStyleSheet('color: #E61F0F;')

    def indfile_check(self):
        # QFileDialog.getOpenFileName((self,'Open CSV',),os.getenv('Home', 'CSV(*.)'))
        path = QFileDialog.getOpenFileName(self, "Open", "", "CSV Files (*.csv);;All Files (*)")
        if path[0] != '':
            path = path[0]
            print(path)
            check = validation.indicators_validation(path, self.df1)
            if check[0]:
                self.datafile_button.setEnabled(False)
                self.indfile_button.setEnabled(False)
                self.df2 = check[1]
                self.df1 = check[2]
                if len(check[3]) == 0:
                    self.output2.setText('Импортированы все {} строк'.format(str(len(self.df2['City']))))
                    self.output2.setStyleSheet('color: green;')
                else:
                    self.output2.setText('Импортированы {} строк\n'
                                         'Строк с ошибками: {}'.format(str(len(self.df2['City'])), str(len(check[3]))))
                    self.output2.setStyleSheet('color: #F0BB15;')
            else:
                self.output2.setText('\n'.join(check[1]))
                self.output2.setStyleSheet('color: #E61F0F;')

    def send_data(self):
        self.parent.set_files(self.df1, self.df2)
        self.close()

    def close(self):
        self.setVisible(False)
        self.df1 = None
        self.df2 = None
        self.datafile_button.setEnabled(True)
        self.indfile_button.setEnabled(True)


class SearchWindow(QtWidgets.QMainWindow, search.UiMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.search_btn.clicked.connect(self.search_city)
        self.search_inp.setText('')

    def search_city(self):
        self.error_label.setText('')
        self.label_name.setText('')
        self.label_place.setText('')
        self.label_v1.setText('')
        self.label_v2.setText('')
        self.label_v3.setText('')
        self.label_v4.setText('')
        self.label_v5.setText('')
        self.label_v6.setText('')
        self.label_sum.setText('')

        res, cnt = self.parent.search_city(self.search_inp.text())
        if len(res) == 0:
            self.error_label.setText('Город не найден')
            return False
        print(res)
        city = res.iloc[0]

        self.label_name.setText(city['City'])
        self.label_place.setText(str(round(cnt - res.index[res['City'] == city['City']].tolist()[0], 3)))
        self.label_v1.setText(str(round(city['Cappuccino'], 3)))
        self.label_v2.setText(str(round(city['Cinema'], 3)))
        self.label_v3.setText(str(round(city['Wine'], 3)))
        self.label_v4.setText(str(round(city['Gasoline'], 3)))
        self.label_v5.setText(str(round(city['Avg Rent'], 3)))
        self.label_v6.setText(str(round(city['Avg Disposable Income'], 3)))
        self.label_sum.setText(str(round(city['Total score'], 3)))


class MyApp(QtWidgets.QMainWindow, dashboard.UiMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        dashboard.UiMainWindow.__init__(self)
        self.setup_ui(self)
        self.up_button.clicked.connect(self.up_dashboard)
        self.down_button.clicked.connect(self.down_dashboard)
        # self.indicatorfile_button.clicked.connect(self.open_indicator_sheet)
        # self.datafile_button.clicked.connect(self.open_data_sheet)
        self.openfile_button.clicked.connect(self.openfile)
        self.search_button.clicked.connect(self.search_btn)
        self.save_button.clicked.connect(self.save_res)

        # self.setCentralWidget(self.widget)
        # self.showMaximized()
        self.layout_widget = QtWidgets.QVBoxLayout(self.widget)
        self.dynamic_canvas = None
        self.ax = None
        self.df_data = None
        self.df_indicator = None
        self.df_res = None
        
        # Index of first element in list
        self.bg = 0
        self.step = 10
        
        self.up_button.setEnabled(False)
        # self.layout_widget.addWidget(self.dynamic_canvas)
        # layout.adjustSize()
        # self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(dynamic_canvas, self))

    def openfile(self):
        self.file_window = FileWindow(self)
        self.file_window.show()

    def search_btn(self):
        # search.Ui_Form.setup_ui(search.Ui_Form)
        self.search_window = SearchWindow(self)
        self.search_window.show()

    def set_files(self, df1, df2):
        # Normalize
        self.df_data = main.minmax_normalization(df1)
        self.df_indicator = main.minmax_normalization(df2)
        self.weights = main.get_new_weights(self.df_data, self.df_indicator)
        self.df_res = main.get_df_res(self.df_data, self.weights)
        # self.df_res = self.df_res.reset_index()

        self.bg = 0
        self.update_canvas()
        self.save_button.setEnabled(True)

    def up_dashboard(self):
        self.bg -= self.step
        if self.bg == 0:
            self.up_button.setEnabled(False)
        self.update_canvas()

    def down_dashboard(self):
        self.bg += self.step
        self.up_button.setEnabled(True)
        self.update_canvas()

    def update_canvas(self):
        # Remove old FigureCanvas
        if self.dynamic_canvas is not None:
            self.dynamic_canvas.deleteLater()
        if self.ax is not None:
            self.ax.remove()
        if self.bg == 0:
            self.up_button.setEnabled(False)
        else:
            self.up_button.setEnabled(True)
        
        if self.bg + self.step >= len(self.df_indicator['Rating']):
            self.pagename.setText(str(self.bg) + ' - ' + str(len(self.df_indicator['Rating']) - 1))
            self.down_button.setEnabled(False)
        else:
            self.pagename.setText(str(self.bg) + ' - ' + str(self.bg + self.step))
            self.down_button.setEnabled(True)
        # Create new figure
        self.fig, self.ax = view.show(self.df_res, self.bg, self.step)
        
        # Попытки сделать график прозрачным
        # self.ax.patch.set_visible(False)
        # self.ax.patch.set_facecolor('None')
        # self.fig.patch.set_visible(False)
        # self.setStyleSheet("background-color:transparent;")
        
        self.dynamic_canvas = FigureCanvas(self.fig)

        self.layout_widget.addWidget(self.dynamic_canvas)

    def search_city(self, city):
        if self.df_res is None:
            return False
        city = city.lower()
        df = self.df_res.copy()
        df = df[df['City'].str.lower().str.startswith(city, na=False)]
        # print(df)
        return df, len(self.df_indicator['Rating'])

    def save_res(self):
        path, ext = QFileDialog.getSaveFileName(self, 'Save file', '', "CSV Files (*.csv);")
        if path != '':
            print(path)
            self.df_res.to_csv(path, index=False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()
    
    # window.show()
    app.exec_()
