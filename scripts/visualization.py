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
