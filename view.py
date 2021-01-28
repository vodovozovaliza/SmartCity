import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from math import sqrt

dpi = 80

def show(df, bg=0, step=-1):
    """
    :does: shows all the data in a diagram
    """
    #df = pd.read_csv(input_filename)

    # print(df['Total score'])

    # Set font size
    mpl.rcParams.update({'font.size': 9})
    # Create figure
    #fig, ax = plt.subplots(dpi = dpi, figsize = (1920 / dpi, 1080 / dpi), num = 'Test')
    fig, ax = plt.subplots(dpi = dpi, figsize = (1920 / dpi, 1080 / dpi))
    # Drawing vertical lines for x axis
    ax.xaxis.grid(True, zorder = 1)
    #ax.set_title('Test')
    # The y coordinates of the bars

    #print(df)

    if step == -1:
        #df['Total score'] = df['Total score'][bg:]
        #df[df.columns[0]] = df[df.columns[0]][bg:]
        df = df[(len(df['Total score']) - bg):]
    else:
        #df['Total score'] = df['Total score'][bg:en]
        #df[df.columns[0]] = df[df.columns[0]][bg:en]
        bg = len(df['Total score']) - bg
        #print('bg: ' + str(bg))
        df = df[max(bg-step, 0):max(bg, 0)]

    #print(str(len(df['Total score'].values)))
    xs = range(len(df['Total score'].values))
    # Create a horizontal bar plots
    plt.barh(xs, df['Total score'].values,
            height = 0.2, color = 'blue', alpha = 0.7, label = 'KPI',
            zorder = 2)

    # Draw names of objects
    plt.yticks(xs, df[df.columns[0]].values, rotation = 10)

    # Set legend location
    #plt.legend(loc='upper right')
    #plt.savefig('result.png')
    #plt.show()
    #plt.tight_layout()
    #plt.subplots_adjust(top=0.9)

    return fig, ax
