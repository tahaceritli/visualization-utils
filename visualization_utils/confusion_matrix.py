import numpy as np


def confusion_matrix(annotations, predictions, classes):
    """Calculates the confusion matrix of a classifier.

    This function compares a set of true labels and a set of predicted labels
    obtained by a classifier.

    Parameters
    ----------
    annotations : array-like of shape (n_samples,)
        True labels.

    predictions : array-like of shape (n_samples,)
        Predicted labels.

    classes : array-like of shape (n_classes,)
        A list of possible class labels in alphabetical order.

    Returns
    -------
    confusion_matrix : {array-like} of shape (n_classes, n_classes)
        Confusion matrix. confusion_matrix[i,j] denotes the number of
        confusions where i and j respectively indicate the orders of
        the prediction and annotation.

    """
    n_classes = len(classes)
    confusion_matrix = np.zeros((n_classes, n_classes), dtype=int)
    for annotation, prediction in zip(annotations, predictions):
        if prediction != "any":
            confusion_matrix[classes.index(prediction), classes.index(annotation),] += 1
    return confusion_matrix
