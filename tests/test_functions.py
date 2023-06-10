import numpy as np
from transformer_lite.core import transpose2d, window1d, convolution2d

def test_transpose2d():
    input_matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    expected_output = [[1, 2, 3], [1 , 2, 3], [1, 2, 3]]
    assert transpose2d(input_matrix) == expected_output

def test_window1d():
    input_array = [1, 2, 3, 4, 5, 6]
    size = 3
    shift = 2
    stride = 1
    expected_output = [[1, 2, 3], [3, 4, 5], [5, 6]]
    assert window1d(input_array, size, shift, stride) == expected_output

def test_convolution2d():
    input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    kernel = np.array([[1, 0], [0, 1]])
    stride = 1
    expected_output = np.array([[6, 8], [12, 14]])
    assert np.array_equal(convolution2d(input_matrix, kernel, stride), expected_output)