def findDiagonalOrder(matrix):
    if matrix == []:
        return

    rows = len(matrix)
    cols = len(matrix[0])
    diagonalMatrix = []
    traversals = rows + (cols - 1)

    row = 0
    col = 0
    for i in range(traversals):
        # TopRight Traversal
        if i % 2 == 0:
            while row > -1 and col < cols:
                diagonalMatrix.append(matrix[row][col])
                row -= 1
                col += 1

            if col > cols - 1:
                row += 2
                col -= 1
            else:
                row += 1

        # BottomLeft Traversal
        else:
            while col > -1 and row < rows:
                diagonalMatrix.append(matrix[row][col])
                row += 1
                col -= 1

            if row > rows - 1:
                row -= 1
                col += 2
            else:
                col += 1

    return diagonalMatrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(findDiagonalOrder(matrix))  # --> [1,2,4,7,5,3,6,8,9]
