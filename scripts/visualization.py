import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import Markdown, display, Image, display_html


def plot_count(df: pd.DataFrame, column: str, xcolumn: str = None, ycolumn: str = None) -> None:
    plt.figure(figsize=(12, 7))
    sns.countplot(data=df, x=column)
    plt.title(f'Plot count of {column}', size=18, fontweight='bold')
    if xcolumn:
        plt.xlabel(xcolumn)
    if xcolumn:
        plt.ylabel(ycolumn)
    plt.show()


def plot_correlation(x):
    corr = x.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    fig, ax = plt.subplots(figsize=(24, 20))
    heatmap = sns.heatmap(corr, mask=mask, square=True, linewidths=.5,
                          vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.1f')
    heatmap.set_title('Correlation between features',
                      fontdict={'fontsize': 15}, pad=12)
    fig.show()