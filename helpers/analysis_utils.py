import pandas as pd
import seaborn as sns
from matplotlib import pyplot
from scipy.stats import pearsonr


# =================================================================================================================== #

def scatterplot(
        dataframe: pd.DataFrame,
        metric_x: str,
        metric_y: str,
        plot_title: str = None,
        plot_size: tuple[int, int] = (8, 8)
) -> None:

    pyplot.figure(figsize=plot_size)
    sns.set(font_scale=1)
    _plt = sns.scatterplot(data=dataframe, x=metric_x, y=metric_y)
    _title = plot_title or f'Scatterplot : {metric_x} v. {metric_y}'
    _plt.set(title=_title)


def corr_value(
        dataframe: pd.DataFrame,
        metric_a: str,
        metric_b: str,
        num_digits: int = None
) -> float:

    _corr, _ = pearsonr(dataframe[metric_a], dataframe[metric_b])
    _ndig = num_digits or 3
    return round(_corr, _ndig)


def corr_matrix(
        dataframe: pd.DataFrame,
        plot_title: str = None,
        plot_size: tuple[int, int] = (8, 8),
        plt_square: bool = True,
        plt_annot: bool = True,
        plt_cbar: bool = True
) -> None:
    
    pyplot.figure(figsize=plot_size)

    _plt = sns.heatmap(data=dataframe.corr(),
                       vmin=1, vmax=1,center=0,
                       square=plt_square, annot=plt_annot, cbar=plt_cbar,
                       cmap=sns.diverging_palette(20, 200, n=200))

    _plt.set_xticklabels(_plt.get_xticklabels(),
                         rotation=45,
                         horizontalalignment='right')

    _title = plot_title or f'Correlation Matrix'
    _plt.set(title=_title)


# =================================================================================================================== #

if __name__ == '__main__':
    print(f"\n\n---------------------------------------- {__file__.split('/')[-1]}")
