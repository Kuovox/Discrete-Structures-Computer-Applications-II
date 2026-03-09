from collections.abc import ValuesView
from Vec import Vec
from math import cos, sin

"""-------------------- PROBLEM 1 --------------------"""
class Matrix:

    def __init__(self, rows):
        """
        initializes a Matrix with given rows
        :param rows: the list of rows that this Matrix object has
        """
        self.rows = rows
        self.cols = []
        self._construct_cols()
        return

    """
  INSERT MISSING SETTERS AND GETTERS HERE
  """
    def set_row(self, i, new_row):
        """
        sets the ith row of this Matrix to the given new_row
        :param i: the row to be set
        :param new_row: the new row to be set
        """
        if len(new_row) != len(self.rows[0]):
          raise ValueError("Incompatible row length.")
        for k in range(len(self.rows[0])):
          self.rows[i-1][k] = new_row[k]
        self._construct_cols()
      
    def set_col(self, j, new_col):
        """ 
        sets the ith column of this Matrix to the given new_col
        :param i: the column to be set
        :param new_col: the new column to be set
        """
        if len(new_col) != len(self.cols[0]):
          raise ValueError("Incompatible column length.")
        for v in range(len(self.cols[0])):
          self.cols[j - 1][v] = new_col[v]
        self._construct_rows()


    def set_entry(self, i, j, val):
      """
      sets the (i, j) entry of this Matrix to val
      :param i: the row of the entry to be set
      :param j: the column of the entry to be set
      :param val: the value to be set
      """
      self.rows[i-1][j-1] = val
      self._construct_cols()
      self._construct_rows()
      
  
    def get_row(self, i):
      """
      returns the ith row of this Matrix
      :param i: the row to be returned (zero-based index)
      :return: the ith row of this Matrix
      """
      if 1 <= i <= len(self.rows):
          return self.rows[i-1]
      else:
          raise IndexError("Index out of range")
  
    def get_col(self, j):
      """
      returns the jth column of this Matrix
      :param j: the column to be returned (zero-based index)
      :return: the jth column of this Matrix
      """
      if 1 <= j <= len(self.cols):
          return self.cols[j-1]
      else:
          raise IndexError("Index out of range")
  
    def get_entry(self, i, j):
      """
      returns the (i, j) entry of this Matrix
      :param i: the row of the entry to be returned (zero-based index)
      :param j: the column of the entry to be returned (zero-based index)
      :return: the (i, j) entry of this Matrix
      """
      if 1 <= i <= len(self.rows) and 1 <= j <= len(self.cols):
          return self.rows[i-1][j-1]
      else:
          raise IndexError("Index out of range.")
  

    def get_columns(self):
      return self.cols

    def get_rows(self):
      return self.rows

    def get_diag(self, k):
      if k == 0:
          return [self.rows[i][i] for i in range(min(len(self.rows), len(self.cols)))]
      elif k > 0:
          return [self.rows[i][i + k] for i in range(min(len(self.rows), len(self.cols) - k))]
      elif k < 0:
          return [self.rows[i - k][i] for i in range(min(len(self.rows) + k, len(self.cols)))]
      else:
          raise ValueError("Invalid value for k.")

    def _construct_cols(self):
        """
        HELPER METHOD: Resets the columns according to the existing rows
        """
        self.cols = []
        for i in range(len(self.rows[0])):
            col = [row[i] for row in self.rows]
            self.cols.append(col)

    def _construct_rows(self):
        """
        HELPER METHOD: Resets the rows according to the existing columns
        """
        self.rows = []
        for i in range(len(self.cols[0])):
            row = [col[i] for col in self.cols]
            self.rows.append(row)

    def __add__(self, other):
        """
        overloads the + operator to support Matrix + Matrix
        :param other: the other Matrix object
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
        """
        if isinstance(other, Matrix):
          if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Incompatible matrix dimensions.")
          result = [[self.rows[i][j] + other.rows[i][j] for j in range(len(self.rows[0]))] for i in range(len(self.rows))]
          return Matrix(result)
        else:
          raise TypeError("Unsupported Type")

    def __sub__(self, other):
        """
        overloads the - operator to support Matrix - Matrix
        :param other:
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from Matrix - Matrix operation
        """
        if isinstance(other, Matrix):
          if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Incompatible matrix dimensions.")
          result = [[self.rows[i][j] - other.rows[i][j] for j in range(len(self.rows[0]))] for i in range(len(self.rows))]
          return Matrix(result)
        else:
          raise TypeError("Unsupported Type")

    def __mul__(self, other):
        """
        overloads the * operator to support
            - Matrix * Matrix
            - Matrix * Vec
            - Matrix * float
            - Matrix * int
        :param other: the other Matrix object
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
        """
        if isinstance(other, (int, float)):
          result = [[self.rows[i][j] * other for j in range(len(self.cols))] for i in range(len(self.rows))]
          return Matrix(result)
          
        elif isinstance(other, Matrix):
          if len(self.cols) != len(other.rows):
            raise ValueError("Incompatible matrix dimensions.")
            
          result = [[sum(self.rows[i][k] * other.rows[k][j] for k in range(len(self.cols))) for j in range(len(other.cols))] for i in range(len(self.rows))]
          return Matrix(result)

        elif isinstance(other, Vec):
          if len(self.cols) != len(other):
            raise ValueError("Incompatible vector dimensions.")
          result = [sum(self.rows[i][k] * other[k] for k in range(len(self.cols))) for i in range(len(self.rows))]
          return Vec(result)
          
        else:
            raise TypeError(f"Matrix * {type(other)} is not supported.")
        

    def __rmul__(self, other):
        """
        overloads the * operator to support
            - float * Matrix
            - int * Matrix
        :param other: the other Matrix object
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
        """
        if isinstance(other, (int, float)):
          result = [[self.rows[i][j] * other for j in range(len(self.cols))] for i in range(len(self.rows))]
          return Matrix(result)
        else:
            raise TypeError(f"{type(other)} * Matrix is not supported.")
    

    '''-------- ALL METHODS BELOW THIS LINE ARE FULLY IMPLEMENTED -------'''

    def dim(self):
        """
        gets the dimensions of the mxn matrix
        where m = number of rows, n = number of columns
        :return: tuple type; (m, n)
        """
        m = len(self.rows)
        n = len(self.cols)
        return (m, n)

    def __str__(self):
        """prints the rows and columns in matrix form """
        mat_str = ""
        for row in self.rows:
            mat_str += str(row) + "\n"
        return mat_str

    def __eq__(self, other):
        """
        overloads the == operator to return True if
        two Matrix objects have the same row space and column space
        """
        if type(other) != Matrix:
            return False
        this_rows = [round(x, 3) for x in self.rows]
        other_rows = [round(x, 3) for x in other.rows]
        this_cols = [round(x, 3) for x in self.cols]
        other_cols = [round(x, 3) for x in other.cols]

        return this_rows == other_rows and this_cols == other_cols

    def __req__(self, other):
        """
        overloads the == operator to return True if
        two Matrix objects have the same row space and column space
        """
        if type(other) != Matrix:
            return False
        this_rows = [round(x, 3) for x in self.rows]
        other_rows = [round(x, 3) for x in other.rows]
        this_cols = [round(x, 3) for x in self.cols]
        other_cols = [round(x, 3) for x in other.cols]

        return this_rows == other_rows and this_cols == other_cols


"""-------------------- PROBLEM 2 --------------------"""



def rotate_2Dvec(v: Vec, tau: float) -> Vec:
    """
    computes the 2D-vector that results from rotating the given vector
    by the given number of radians
    :param v: Vec type; the vector to rotate
    :param tau: float type; the radians to rotate by
    :return: Vec type; the rotated vector
    """
    x, y = v[0], v[1]
    prime_x = x * cos(tau) - y * sin(tau)
    prime_y = x * sin(tau) + y * cos(tau)
    return Vec([prime_x, prime_y])
