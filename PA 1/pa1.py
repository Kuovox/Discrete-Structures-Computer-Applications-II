import math

""" ---------------- PROBLEM 1 ----------------"""
def equiv_to(a, m, low, high):
    k_low = math.ceil((low-a)/m) 
    k_high = math.floor((high-a)/m) 
    k_vals = list(range(k_low, k_high +1))
    x_vals = [a + k*m for k in k_vals]
    return x_vals

""" ---------------- PROBLEM 2 ----------------"""
def b_rep(n, b):
    digits = []
    q = n
    while q != 0:
        digit = q % b 
        if b == 16 and digit > 9:
          hex_dict = {10: 'A', 11 : 'B', 12: 'C', 13: 'D', 14: 'E', 15 : 'F'}
          digit = hex_dict[digit]
        digits.append(str(digit))
        q = q // b
    return ''.join(reversed(digits))
        

""" ---------------- PROBLEM 3 ----------------"""
def binary_add(a, b): 
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    # padding the strings with 0's so they are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" *diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" *diff + b
    
    # addition algorithm
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])
    
        result += str((a_i + b_i + carry) % 2)
        carry = (a_i + b_i + carry) // 2
        
    if carry == 1:
        result += str(carry) 
    return result[::-1] 


""" ---------------- PROBLEM 4 ----------------"""
def binary_mul(a, b):
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    # multiplication algorithm
    partial_products = []
    i = 0 # index of the current bit of string 'a' beginning at 0, right-to-left
    for bit in reversed(a):
        if bit == '1':
          partial_products.append(b + '0' * i)
        i += 1

    result = '0'
    while len(partial_products) > 0:
        result = binary_add(result, partial_products[0])
        del partial_products[0]
    return result