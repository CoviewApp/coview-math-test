import numpy as np

def matrix_multiply(A, B):
    """Multiply two matrices A and B."""
    return np.dot(A, B)

def determinant(matrix):
    """Calculate the determinant of a matrix."""
    return np.linalg.det(matrix)

def solve_quadratic(a, b, c):
    """Solve quadratic equation ax^2 + bx + c = 0."""
    delta = b**2 - 4*a*c
    if delta < 0:
        return "No real solutions"
    elif delta == 0:
        return -b / (2*a)
    else:
        x1 = (-b + np.sqrt(delta)) / (2*a)
        x2 = (-b - np.sqrt(delta)) / (2*a)
        return (x1, x2)

def matrix_inverse(matrix):
    """Compute the inverse of a matrix if it is invertible."""
    if np.linalg.det(matrix) == 0:
        return "Matrix is not invertible"
    else:
        return np.linalg.inv(matrix)

# Example Usage
if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    print("Matrix A:")
    print(A)
    print("Inverse of Matrix A:")
    print(matrix_inverse(A))
