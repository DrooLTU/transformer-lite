import numpy as np

def transpose2d(input_matrix: list[list[float]]) -> list:
    """Implement this function using only Python and its standard library."""
    num_rows = len(input_matrix)
    num_cols = len(input_matrix[0])

    # Create a new matrix with transposed dimensions
    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    # Iterate over the input matrix and assign values to the transposed matrix
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = input_matrix[i][j]

    return transposed_matrix        
    

def window1d(input_array: list | np.ndarray, size: int, shift: int = 1, stride: int = 1) -> list[list | np.ndarray]:
    """Implement this function using only Python, its standard library, and Numpy."""
    if isinstance(input_array, np.ndarray):
        input_array = input_array.tolist()

    num_windows = (len(input_array) - size) // shift + 1
    windows = []

    for i in range(num_windows):
        start = i * shift
        end = start + size
        window = input_array[start:end:stride]
        windows.append(window)

    if isinstance(input_array, np.ndarray):
        windows = [np.array(window) for window in windows]

    return windows


def convolution2d(input_matrix: np.ndarray, kernel: np.ndarray, stride : int = 1) -> np.ndarray:
    """Implement this function using only Python, its standard library, and Numpy."""
    # Get dimensions of input matrix and kernel
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate output dimensions
    output_height = (input_height - kernel_height) // stride + 1
    output_width = (input_width - kernel_width) // stride + 1

    # Initialize output matrix
    output_matrix = np.zeros((output_height, output_width))

    # Perform convolution
    for i in range(output_height):
        for j in range(output_width):
            # Calculate the indices for the current window
            start_row = i * stride
            start_col = j * stride
            end_row = start_row + kernel_height
            end_col = start_col + kernel_width

            # Extract the window from the input matrix
            window = input_matrix[start_row:end_row, start_col:end_col]

            # Perform element-wise multiplication and sum
            output_matrix[i, j] = np.sum(window * kernel)

    return output_matrix
