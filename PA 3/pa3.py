from util import digits2letters, letters2digits, blocksize
import math 

def bezout_coeffs(a, b):
  """
      computes the Bezout coefficients of two given positive integers
      :param a: int type; positive integer
      :param b: int type; positive integer
      :returns: dict type; a dictionary with parameters a and b as keys, 
                and their corresponding Bezout coefficients as values.
      :raises: ValueError if a < 0 or b < 0
      """
  if a < 0 or b < 0:
    raise ValueError(f"bezout_coeffs(a, b) does not support negative arguments.")
  s0 = 1
  t0 = 0
  s1 = -1 * (b // a)
  t1 = 1

  temp = b
  bk = a
  ak = temp % a

  while ak != 0:
    temp_s = s1
    temp_t = t1

    s1 = s0 - (bk // ak) * s1

    t1 = t0 - (bk // ak) * t1

    s0 = temp_s
    t0 = temp_t
    temp = bk

    bk = ak
    ak = temp % ak

  a_inv = s0
  
  return a_inv

""" ----------------- PROBLEM 1 ----------------- """

def affine_encrypt(text, a, b):
  
  """
    encrypts the plaintext 'text', using an affine transformation key (a, b)
    :param: text - str type; plaintext as a string of letters
    :param: a - int type; integer satisfying gcd(a, 26) = 1
    :param: b - int type; shift value
    :raise: ValueError if gcd(a, 26) is not 1.
    :return: str type; the encrypted message as string of uppercase letters
    """
  if math.gcd(a, 26) != 1: # FIXME: raise an error if the gcd(a, 26) is not 1
    raise ValueError("The given key is invalid.")

  cipher = ""
  for letter in text:
    if letter.isalpha(): # FIXME: Use util.py to initialize 'num' to be the integer corresponding to the current letter
      num = letters2digits(letter)
      num = int(num)

      # K. VARELA COMMENT: num is of the type str, so you need to convert it to int first
      cipher_num = (a * num + b) % 26 

      # FIXME: Encrypt the current 'num' using the affine transformation with key (a, b). Store the result in cipher_digits.
      cipher_digits = str(cipher_num)
      
      if len(cipher_digits) == 1: # FIXME: If the cipherdigit is 0 - 9, prepend the string with a 0 to make it a two-digit number
        cipher_digits = '0' + cipher_digits

      # FIXME: Use util.py to append to the cipher the ENCRYPTED letter corresponding to the current cipher digits
      cipher += digits2letters(cipher_digits)
    
  return cipher


""" ----------------- PROBLEM 2 ----------------- """



def affine_decrypt(ciphertext, a, b):
  """
    decrypts the given cipher, assuming it was encrypted using an affine transformation key (a, b)
    :param: ciphertext - str type; a string of digits
    :param: a - int type; integer satisfying gcd(a, 26) = 1.
    :param: b - int type; shift value
    :return: str type; the decrypted message as a string of uppercase letters
    """
  
  if math.gcd(a, 26) != 1:
    raise ValueError("The given key is invalid.")
  else:
    a_inv = bezout_coeffs(a, 26)
  
  text = ""
  for letter in ciphertext:
    if letter.isalpha():
      letter = letter.upper()

      # FIXME: Use util.py to find the integer `num` that corresponds to the given letter
      num = letters2digits(letter)
      num = int(num)

      # FIXME: Decrypt the integer that corresponds to the current encrypted letter using the decryption function for an affine transformation with key (a, b) so that letter_digits holds the decrypted number as a string of two digits
      # K. VARELA COMMENT: num is of the type str, so you need to convert it to int first
      letter_digits = (a_inv * (num - b)) % 26

      if len(str(letter_digits)) == 1:
        # FIXME: If the letter number is between 0 - 9, inclusive, prepend the string with a 0
        letter_digits = '0' + str(letter_digits)

      # FIXME: Use util.py to append to the text the decrypted
      # letter corresponding to the current letter digits
      text += digits2letters(str(letter_digits))
      
  return text


""" ----------------- PROBLEM 3 ----------------- """


def encryptRSA(plaintext, n, e):
  """
    encrypts plaintext using RSA and the key (n, e)
    :param: text - str type; plaintext as a string of letters
    :param: n - int type; positive integer that is the modulo in the RSA key
    :param: e - int type; positive integer that is the exponent in the RSA key
    :return: str type; the encrypted message as a string of digits
    """

  text = plaintext.replace(' ', '')  # removing whitespace

  # FIXME: Use util.py to initialize 'digits' as a string of the two-digit integers that correspond to the letters of 'text'
  digits = ''.join([str(letters2digits(letter)) for letter in text])

  # FIXME: Use util.py to initialize 'l' with the length of each RSA block
  l = blocksize(n) # K. VARELA COMMENT: This is incorrect.  You must use the blocksize() function from util.py to get the length of the block.

  # FIXME: Use a loop to pad 'digits' with enough 23's (i.e. X's) so that it can be broken up into blocks of length l
  #padding_length = l - (len(digits) % l)
  if len(str(digits)) % l != 0:
    digits = str(digits) + '23' 
  
  # creating a list of RSA blocks
  blocks = [digits[i:i + l] for i in range(0, len(digits), l)]
  
  cipher = ""
  for b in blocks:
    # FIXME: Initialize 'encrypted_block' so that it contains the encryption of block 'b' as a string
    encrypted_block = str(pow(int(b), e, n))

    if len(encrypted_block) < l:
      # FIXME: If the encrypted block contains less digits than the block size l, prepend the block with enough 0's so that the numeric value of the block remains the same, but the new block size is l, e.g. if l = 4 and encrypted block is '451' then prepend one 0 to obtain '0451'
      encrypted_block = '0' * (l - len(encrypted_block)) + encrypted_block
    # FIXME: Append the encrypted block to the cipher
    cipher += encrypted_block
    
  return cipher


""" ----------------- PROBLEM 4 ----------------- """


def decryptRSA(cipher, p, q, e):
  """
    decrypts the cipher, which was encrypted using RSA and the key (p * q, e)
    :param: cipher - ciphertext as a string of digits
    :param: p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
    :param: e - integer satisfying gcd((p-1)*(q-1), e) = 1
    :return: str type; the decrypted message as a string of letters
    """

  n = p * q
  ciphertext = cipher.replace(' ', '')

  # FIXME: Use util.py to initialize `l` with the size of
  # each RSA block
  l = blocksize(n)

  # FIXME: Use a Python list comprehension to break the ciphertext
  # into blocks of equal length 'l'. Initialize 'blocks' so that it
  # contains these blocks as elements
  blocks = [ciphertext[i:i + l] for i in range(0, len(ciphertext), l)]

  text = ""  # initializing the variable that will hold the decrypted text

  # FIXME: Compute the inverse of e
  modulo = (p - 1) * (q - 1)
  s0 = 1
  t0 = 0
  s1 = -1 * (modulo // e)
  t1 = 1

  temp = modulo
  bk = e
  ak = temp % e
  while ak != 0:
    temp_s = s1
    temp_t = t1

    s1 = s0 - (bk // ak) * s1
    t1 = t0 - (bk // ak) * t1

    s0 = temp_s
    t0 = temp_t
    temp = bk

    bk = ak
    ak = temp % ak
    # ARGGG
  while s0 < 0:
    s0 += modulo
    
  e_inv = s0

  for b in blocks:
    # FIXME: Use the RSA decryption function to decrypt
    # the current block
    decrypted_block = str(pow(int(b), e_inv, n))

    if len(decrypted_block) < l:
      # FIXME: If the decrypted block contains less digits
      # than the block size l, prepend the block with
      # enough 0's so that the numeric value of the block
      # remains the same, but the new block size is l,
      # e.g. if l = 4 and decrypted block is '19' then prepend
      # two 0's to obtain '0019'
      decrypted_block = '0' * (l - len(decrypted_block)) + decrypted_block

    # FIXME: Use util.py to append to text the decrypted block
    # transformed into letters
    text += digits2letters(decrypted_block)

  return text
