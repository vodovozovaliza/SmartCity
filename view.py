import matplotlib as mpl
import matplotlib.pyplot as plt

dpi = 80


def show(df, bg=0, step=-1):
    """
    :does: shows all the data in a diagram
    :return: subplot [bg, bg + step]
    :does: counts Total Score in the dataframe, sorts by it, and creates a subplot
    """

    # Set font size
    mpl.rcParams.update({'font.size': 9})
    # Create figure
    fig, ax = plt.subplots(dpi=dpi, figsize=(1920 / dpi, 1080 / dpi))
    plt.xlim(0, 1)
    # Drawing vertical lines for x axis
    ax.xaxis.grid(True, zorder=1)

    if step == -1:
        df = df[(len(df['Total score']) - bg):]
    else:
        bg = len(df['Total score']) - bg
        df = df[max(bg-step, 0):max(bg, 0)]

    xs = range(len(df['Total score'].values))
    # Create a horizontal bar plots
    plt.barh(xs, df['Total score'].values, height=0.2, color='blue', alpha=0.7, label='KPI', zorder=2)

    # Draw names of objects
    plt.yticks(xs, df[df.columns[0]].values, rotation=10)

    return fig, ax
