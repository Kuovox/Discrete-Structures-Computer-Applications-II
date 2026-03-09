import cmath
import math

""" ----------------- PROBLEM 1 ----------------- """
def translate(S, z0):
  """
  translates the complex numbers of set S by z0
  :param S: set type; a set of complex numbers
  :param z0: complex type; a complex number
  :return: set type; a set consisting of points in S translated by z0
  """

  translated_set = set()
  for point in S:
    translated_point = point + z0
    translated_set.add(translated_point)

  return translated_set


""" ----------------- PROBLEM 2 ----------------- """
def scale(S, k):
  """
  scales the complex numbers of set S by k.  
  :param S: set type; a set of complex numbers
  :param k: float type; positive real number
  :return: set type; a set consisting of points in S scaled by k
  :raise: raises ValueError if k <= 0       
  """

  if k <= 0:
    raise ValueError("k must be a positive real number")

  scaled_set = set()
  for point in S:
    scaled_point = point * k
    scaled_set.add(scaled_point)
    
  return scaled_set


""" ----------------- PROBLEM 3 ----------------- """
def rotate(S, tau):  
  """
  rotates the complex numbers of set S by tau radians.  
  :param S: set type; - set of complex numbers
  :param tau: float type; radian measure of the rotation value. 
              If negative, the rotation is clockwise.  
              If positive the rotation is counterclockwise. 
              If zero, no rotation.
  :returns: set type; a set consisting of points in S rotated by tau radians
  """
  rotated_set = set()
  for point in S:
    a = point.real
    b = point.imag
    z = math.sqrt((a)**2 + (b)**2)
    theta = (math.atan2(b,a))
    theta_prime = theta + tau
    cos = round(z*math.cos(theta_prime), 3)
    sin = round(z*math.sin(theta_prime), 3)
    rotated_point = complex(cos, sin)
    rotated_set.add(rotated_point)
  
  return rotated_set


""" ----------------- PROBLEM 4 ----------------- """
class Vec:
  def __init__(self, contents = []):
      """
      Constructor defaults to empty vector
      INPUT: list of elements to initialize a vector object, defaults to empty list
      """
      self.elements = contents
      return

  def __abs__(self):
    
      """
      Overloads the built-in function abs(v)
      :returns: float type; the Euclidean norm of vector v
      """
      
      return sum(x ** 2 for x in self.elements) ** 0.5

  def __add__(self, other):
      """
      overloads the + operator to support Vec + Vec
      :raises: ValueError if vectors are not same length 
      :returns: Vec type; a Vec object that is the sum vector of this Vec and 'other' Vec
      """

      if len(self.elements) != len(other.elements):
        raise ValueError("Vectors must have the same length")
      return Vec([x + y for x, y in zip(self.elements, other.elements)])

  def __sub__(self, other):
      """
      overloads the - operator to support Vec - Vec
      :raises: ValueError if vectors are not same length 
      :returns: Vec type; a Vec object that is the difference vector of this Vec and 'other' Vec
      """
      if len(self.elements) != len(other.elements):
        raise ValueError("Vectors must have the same length")
      return Vec([x - y for x, y in zip(self.elements, other.elements)])

  def __mul__(self, other):
      """
      Overloads the * operator to support 
          - Vec * Vec (dot product) raises ValueError if vectors are not 
            same length in the case of dot product; returns scalar
          - Vec * float (component-wise product); returns Vec object
          - Vec * int (component-wise product); returns Vec object

      """
      if type(other) == Vec: #define dot product
          if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must have the same length")
          return sum([x * y for x, y in zip(self.elements, other.elements)])
      elif type(other) == float or type(other) == int: #scalar-vector multiplication
          return Vec([x * other for x in self.elements])


  def __rmul__(self, other):
      """
      Overloads the * operation to support 
          - float * Vec; returns Vec object
          - int * Vec; returns Vec object
      """
      if type(other) == float or type(other) == int: #scalar-vector multiplication
        self = [other * x for x in self.elements]
      
      return Vec(self)

  def __str__(self):
      """returns string representation of this Vec object"""
      return str(self.elements) # does NOT need further implementation