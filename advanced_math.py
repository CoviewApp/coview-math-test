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

# Example Usage
if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[2, 0], [1, 2]])
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    print("Matrix A * B:")
    print(matrix_multiply(A, B))

    matrix = np.array([[2, 1, 3], [1, 0, 0], [0, 1, 4]])
    print("Determinant of matrix:")
    print(determinant(matrix))

    print("Solving quadratic equation x^2 - 3x + 2:")
    print(solve_quadratic(1, -3, 2))
