""" Miscellaneous """

import numpy as np

def moving_average(x, kernel_size):
    assert kernel_size % 2 == 0
    # pad with edge value to keep size of array and avoid edge effects
    pad_width = int(kernel_size/2)
    x = np.pad(x, pad_width, mode='edge')
    kernel = np.ones(kernel_size)/kernel_size
    return np.convolve(x, kernel, 'same')[pad_width:-pad_width]
