def main():
    # synthetic data
    labels = ["A", "B"]
    y = ["A", "B", "A", "B", "A", "B", "A", "B", "A", "B"]
    y_hat = ["A", "A", "B", "B", "A", "B", "A", "B", "B", "A"]

    cm = confusion_matrix(y, y_hat, labels)

    try:
        plot_confusion_matrix(cm, labels, "test/confusion_matrix.png", "error")
    except:
        Exception(f"Comparison failed.")


if __name__ == "__main__":
    from visualization_utils.confusion_matrix import confusion_matrix
    from visualization_utils.plot_confusion_matrix import plot_confusion_matrix

    main()
