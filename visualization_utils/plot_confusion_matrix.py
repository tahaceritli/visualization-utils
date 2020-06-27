import matplotlib.pyplot as plt

from visualization_utils.base_functions import annotate_heatmap, heatmap


def plot_confusion_matrix(
    confusion_matrix, classes, figure_path="confusion_matrix.png"
):
    """Plots a given confusion matrix.

    This function plots a given confusion matrix and saves it as a figure.

    Parameters
    ----------
    confusion_matrix : array-like of shape (n_classes, n_classes)
        Confusion matrix.

    classes : array-like of shape (n_classes,)
        Classes.

    figure_path : str, default=confusion_matrix.png
        Figure path.


    Returns
    -------
        None
    """
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 5),)
    fig.tight_layout()

    im = heatmap(
        confusion_matrix,
        classes,
        classes,
        x_label="True Class",
        y_label="Predicted Class",
        ax=ax,
        vmin=0,
        vmax=0,
    )
    annotate_heatmap(im, valfmt="{x:d}", size=20, textcolors=["black", "white"])
    fig.tight_layout()

    plt.savefig(figure_path, dpi=300, bbox_inches="tight")
