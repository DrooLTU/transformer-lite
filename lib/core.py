from numpy import np

class transpose2d: 
    """Implement this function using only Python and its standard library."""
    def __init__(self, input_matrix: list[list[float]]):
        self.input_matrix = input_matrix
    

class window1d:
    """Implement this function using only Python, its standard library, and Numpy."""
    def __init__(input_array: list | np.ndarray, size: int, shift: int = 1, stride: int = 1) -> list[list | np.ndarray]:
        pass

class convolution2d:
    """Implement this function using only Python, its standard library, and Numpy."""
    def __init__(input_matrix: np.ndarray, kernel: np.ndarray, stride : int = 1) -> np.ndarray:
        pass
