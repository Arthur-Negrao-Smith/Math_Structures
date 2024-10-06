# Funções genéricas para aumentar a abstração e diminuir a complexidade de leitura
def scanRow(matrix: list, row_pos: int) -> list:
    return matrix[row_pos]

def scanColumn(matrix: list, column_pos: int) -> list:
    rows = len(matrix)
    row_matrix = []
    for row in range(0, rows):
        row_matrix.append(matrix[row][column_pos])
    return row_matrix

# Protótipo do printMatrix sem classe
'''
def printMatrix(matrix) -> None:
    rows = len(matrix)
    columns = len(matrix[0])
    for line in range(0, rows):
        for column in range(0, columns):
            print(matrix[line][column], end=' ')
        print()
'''

# Classe das matriz
class Matrix:
    def __init__(self, matrix: list) -> None:
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.matrix = matrix

    def printMatrix(self) -> None:
        """
        Will print any matrix in the terminal
        """
        for line in range(0, self.rows):
            print('| ', end='')
            for column in range(0, self.columns):
                print(self.matrix[line][column], end=' ')
            print('|')

    def multiply(self, matrixB: 'Matrix') -> 'Matrix':
        """
        Parameter:
            matrixB: Matrix which will do the multiplication
        """
        if self.columns == matrixB.rows:
            temp_matrix = []
            for rowA in range(0, self.rows):
                temp_list = []
                for columnB in range(0, self.columns):
                    number_result = 0
                    temp_rowA = scanRow(self.matrix, rowA)
                    temp_columnB = scanColumn(matrixB.matrix, columnB)
                    for item in range(0, self.columns):
                        number_result += temp_rowA[item] * temp_columnB[item] 
                    temp_list.append(number_result)
                temp_matrix.append(temp_list)
            return Matrix(temp_matrix)
        else:
            return None

    def sumMatrix(self, matrixB: 'Matrix') -> None:
        """
        Parameter:
            matrixB: Matrix which will do the sum
        """
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                self.matrix[row][column] += matrixB.matrix[row][column]

    def subMatrix(self, matrixB: 'Matrix') -> None:
        """
        Parameter:
            matrixB: Matrix which will do the subtraction
        """
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                self.matrix[row][column] -= matrixB.matrix[row][column]

    def skalar(self, skalar_number: int) -> None:
        """
        Parameter:
            skalar_number: Number that will multiply all elements of the matrix
        """
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                self.matrix[row][column] *= skalar_number

    def transposedMatrix(self) -> None:
        """
        Will transpose the current matrix
        """
        temp_row = temp_matrix = []
        for column in range(0, self.columns):
            temp_row = scanColumn(self.matrix, column)
            temp_matrix.append(temp_row)
        self.matrix = temp_matrix

    def det2x2(self) -> float:
        """
        Will calculate the determinante of the current matrix
        """
        if self.columns == self.rows and self.rows == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            return None

    def det(self) -> float:
        pass

A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

B = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

C = [
    [1, 2],
    [3, 4]
]

if __name__ == '__main__':
    matrixA = Matrix(A)
    matrixA.printMatrix()
    print()
    
    matrixB = Matrix(B)
    matrixB.printMatrix()
    print()
    
    matrixC = Matrix(C)
    matrixC.printMatrix()
    print()

    temp = matrixA.multiply(matrixB)
    temp.printMatrix()
    print()

    print(matrixC.det2x2())
