from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Rotates the given n x n matrix by 90 degrees clockwise in-place.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
# Example usage
if __name__ == "__main__":
    matrix = [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ]
    
    print("Original matrix:")
    for row in matrix:
        print(row)

    rotate(matrix)
    
    print("\nRotated matrix:")
    for row in matrix:
        print(row)
