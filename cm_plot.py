#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


def cm_plot(y, yp):
    cm = confusion_matrix(y, yp)
    plt.matshow(cm, cmap=plt.cm.Greens)
    plt.colorbar()

    for x1 in range(len(cm)):
        for y1 in range(len(cm)):
            plt.annotate(cm[x1, y1], xy=(x1, y1), horizontalalignment='center', verticalalignment='center')

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    return plt