import numpy as np


# ' generate standard deviation of predicted array and observed array associated with each k
# '
# '
# ' @param *array predicted array generated by the model
# ' @param *array observed array drived from the dataset
# '
# ' @return an array that contain the standard deviation of each paired predicted array and observed array
# ' @export
# '
# ' @examples
# ' para_optimize(yhat, y_test, 10)

def std_Acc(yhat, y_test, Ks):
    std_acc = np.zeros((Ks - 1))

    for n in range(1, Ks):
        std_acc[n - 1] = np.std(yhat == y_test) / np.sqrt(yhat.shape[0])
    return std_acc