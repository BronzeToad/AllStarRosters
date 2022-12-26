import pandas as pd
import seaborn as sns
from matplotlib import pyplot
from scipy.stats import pearsonr


# ============================================================================ #

def scatterplot(dataframe: pd.DataFrame,
                metric_x: str,
                metric_y: str,
                plot_title: str = None,
                plot_size: tuple[int, int] = None) -> None:
    if plot_size is None:
        pyplot.figure(figsize=(8, 8))
    else:
        pyplot.figure(figsize=plot_size)

    sns.set(font_scale=1)
    plt = sns.scatterplot(data=dataframe, x=metric_x, y=metric_y)

    if plot_title is None:
        plt.set(title=f'Scatterplot : {metric_x} v. {metric_y}')
    else:
        plt.set(title=plot_title)


# ============================================================================ #

def corr_value(dataframe: pd.DataFrame,
               metric_a: str,
               metric_b: str,
               num_digits: int = None) -> float:
    corr, _ = pearsonr(dataframe[metric_a], dataframe[metric_b])
    ndigits = 3 if num_digits is None else num_digits
    return round(corr, ndigits)


# ============================================================================ #

def corr_matrix(dataframe: pd.DataFrame,
                plot_title: str = None,
                plot_size: tuple[int, int] = None,
                plt_square: bool = True,
                plt_annot: bool = True,
                plt_cbar: bool = True) -> None:
    if plot_size is None:
        pyplot.figure(figsize=(8, 8))
    else:
        pyplot.figure(figsize=plot_size)

    plt = sns.heatmap(data=dataframe.corr(),
                      vmin=1, vmax=1,center=0,
                      square=plt_square, annot=plt_annot, cbar=plt_cbar,
                      cmap=sns.diverging_palette(20, 200, n=200))

    plt.set_xticklabels(plt.get_xticklabels(),
                        rotation=45,
                        horizontalalignment='right')

    if plot_title is None:
        plt.set(title=f'Correlation Matrix')
    else:
        plt.set(title=plot_title)


# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
