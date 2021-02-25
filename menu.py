from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
from matplotlib.backends.backend_qt5agg import (FigureCanvas)

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
import select_file
import dashboard
import search
import help

import validation  # validates the files
import view  # displays the diagram of indicators
import main
import sys
import os
from os.path import dirname, abspath

import qtmodern.styles
import qtmodern.windows


class FileWindow(QtWidgets.QMainWindow, select_file.Ui_Form):

    def __init__(self, parent=None):
        """
        :does: init file window
        """
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.datafile_button.clicked.connect(self.datafile_check)
        self.ok_button.setEnabled(False)
        self.ok_button.clicked.connect(self.send_data)
        self.cancel_button.clicked.connect(self.close)

    def datafile_check(self):
        """
        :does: get path of dataframe
        """
        # QFileDialog.getOpenFileName((self,'Open CSV',),os.getenv('Home', 'CSV(*.)'))
        path = QFileDialog.getOpenFileName(self, "Open", "", "CSV Files (*.csv);;All Files (*)")
        if path[0] != '':
            path = path[0]
            print(path)
            check = validation.data_validation(path)
            # print(check)

            if check[0]:
                self.df1 = check[1]
                # self.indfile_button.setEnabled(True)
                if len(check[2]) == 0:
                    self.output1.setText('All {} cities imported.'.format(str(len(self.df1['City']))))
                    self.output1.setStyleSheet('color: green;')
                else:
                    errors = ''
                    print(check[2])
                    for error in check[2]:
                        if error.column == 'City':
                            errors += 'row: ' + str(error.row) + ', column: City, \nCity name must not be empty.'
                        else:
                            errors += 'row: ' + str(error.row) + ', column: ' + error.column + ', \n"' \
                                      + error.value + '" must be decimal.'
                        errors += '\n'
                    self.output1.setText(
                        '{} cities imported\n Lines with errors: {} '.format(str(len(self.df1['City'])),
                                                                             str(len(check[2])) + '\n' + errors))
                    self.output1.setStyleSheet('color: #F0BB15;')
                self.ok_button.setEnabled(True)
            else:
                if check[1] == ['The criteria names are incorrect.'] or check[1] == ['Error rading a file.']:
                    self.output1.setText('\n'.join(check[1]))
                else:
                    errors = ''
                    for error in check[2]:
                        if error.column == 'City':
                            errors += 'row: ' + str(error.row) + ', column: City, City name must not be empty.'
                        else:
                            errors += 'row: ' + str(error.row) + ', column: ' + error.column + ', "' \
                                      + error.value + '" must be decimal.'
                        errors += '\n'
                    self.output1.setText('\n' + errors)
                self.output1.setStyleSheet('color: #E61F0F;')

    def send_data(self):
        """
        :does: set MainWindow dataframe and close file window
        """
        self.parent.set_files(self.df1)
        self.close()

    def close(self):
        """
        :does: close File window
        """
        self.setVisible(False)
        self.df1 = None
        self.ok_button.setEnabled(False)


class SearchWindow(QtWidgets.QMainWindow, search.Ui_MainWindow):

    def __init__(self, parent=None):
        """
        :does: init Search Window
        """
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.search_btn.clicked.connect(self.search_city)
        self.search_inp.setText('')

    def search_city(self):
        """
        :does: search city by name in dataframe
        """
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
            self.error_label.setText('Not found')
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


class HelpWindow(QtWidgets.QMainWindow, help.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.next_btn.clicked.connect(self.next)
        self.prev_btn.clicked.connect(self.prev)
        self.i = 1

    def next(self):
        """
        :does: scroll images
        """
        if self.i == 5:
            return self.close()
        self.next_btn.setEnabled(False)
        self.i += 1
        self.next_btn.setEnabled(True)
        self.update()

    def prev(self):
        """
        :does: scroll images
        """
        self.prev_btn.setEnabled(False)
        self.i -= 1
        self.prev_btn.setEnabled(True)
        self.update()

    def close(self):
        """
        :does: close Help Window
        """
        self.setVisible(False)

    def update(self):
        """
        :does: update bg of window
        """
        if self.i == 1:
            self.prev_btn.setEnabled(False)
        else:
            self.prev_btn.setEnabled(True)

        if self.i == 5:
            self.next_btn.setText('Get started')
        else:
            self.next_btn.setText('Next')

        self.img.setPixmap(QtGui.QPixmap("imgs/help/Frame " + str(self.i) + ".png"))


class MyApp(QtWidgets.QMainWindow, dashboard.Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        dashboard.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.up_button.clicked.connect(self.up_dashboard)
        self.down_button.clicked.connect(self.down_dashboard)
        self.openfile_button.clicked.connect(self.openfile)
        self.search_button.clicked.connect(self.search_btn)
        self.save_button.clicked.connect(self.save_res)
        self.info_button.clicked.connect(self.help)
        self.shortcut_open = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+O'), self)
        self.shortcut_open.activated.connect(self.openfile)
        self.shortcut_save = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+S'), self)
        self.shortcut_save.activated.connect(self.save_res)

        self.layout_widget = QtWidgets.QVBoxLayout(self.widget)
        self.dynamic_canvas = None
        self.ax = None
        self.df_data = None
        self.df_res = None

        # Index of first element in list
        self.bg = 0
        self.step = 10

        self.up_button.setEnabled(False)

    def openfile(self):
        """
        :does: create file window
        """
        self.file_window = FileWindow(self)
        self.file_window.show()

    def help(self):
        """
        :does: create help window
        """
        self.help_window = HelpWindow(self)
        self.help_window.show()

    def search_btn(self):
        """
        :does: create search window
        """
        self.search_window = SearchWindow(self)
        self.search_window.show()

    def set_files(self, df1):
        """
        :does: set dataframe
        """
        # Normalize
        self.df_data = main.minmax_normalization(df1)

        self.weights = [9.92651551e-05, 7.25791032e-02, 3.12450709e-01, 3.58666717e-01, 2.40904263e-01, 2.02728718e-01]
        self.df_res = main.get_df_res(self.df_data, self.weights)

        self.bg = 0
        self.update_canvas()
        self.save_button.setEnabled(True)
        self.search_button.setEnabled(True)
        self.pagename.show()
        self.up_button.show()
        self.down_button.show()

    def up_dashboard(self):
        """
        :does: scroll subplot
        """
        self.bg -= self.step
        if self.bg == 0:
            self.up_button.setEnabled(False)
        self.update_canvas()

    def down_dashboard(self):
        """
        :does: scroll subplot
        """
        self.bg += self.step
        self.up_button.setEnabled(True)
        self.update_canvas()

    def update_canvas(self):
        """
        :does: update canvas
        """
        # Remove old FigureCanvas
        if self.dynamic_canvas is not None:
            self.dynamic_canvas.deleteLater()
        if self.ax is not None:
            self.ax.remove()
        if self.bg == 0:
            self.up_button.setEnabled(False)
        else:
            self.up_button.setEnabled(True)

        if self.bg + self.step >= len(self.df_data['City']):
            self.pagename.setText(str(self.bg) + ' - ' + str(len(self.df_data['City']) - 1))
            self.down_button.setEnabled(False)
        else:
            self.pagename.setText(str(self.bg) + ' - ' + str(self.bg + self.step))
            self.down_button.setEnabled(True)
        # Create new figure
        self.fig, self.ax = view.show(self.df_res, self.bg, self.step)

        self.dynamic_canvas = FigureCanvas(self.fig)

        self.layout_widget.addWidget(self.dynamic_canvas)

    def search_city(self, city):
        """
        :param city: city name
        :return: array of cities, starts with variable city
        :does: search cities in df
        """
        if self.df_res is None:
            return False
        city = city.lower()
        df = self.df_res.copy()
        df = df[df['City'].str.lower().str.startswith(city, na=False)]
        return df, len(self.df_data['City'])

    def save_res(self):
        """
        :does: save df to file
        """
        path, ext = QFileDialog.getSaveFileName(self, 'Save file', '', "CSV Files (*.csv);")
        if path != '':
            print(path)
            self.df_res.to_csv(path, index=False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()

    qtmodern.styles.light(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()

    app.exec_()
