def convert_base64_to_binary( base64_string ):
  full_binary_string = ''

  for ch in base64_string:
    if ch == '=':
      continue
    full_binary_string += base64_to_octeat( ch )

  return octeats_to_bytes( full_binary_string )


def base64_to_octeat( ch ):
  BASE_64 = {
    'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 
    'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 
    'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 
    'R' : 17, 'S' : 18, 'T' : 19, 'U' : 20, 'V' : 21, 
    'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25, 'a' : 26, 
    'b' : 27, 'c' : 28, 'd' : 29, 'e' : 30, 'f' : 31, 
    'g' : 32, 'h' : 33, 'i' : 34, 'j' : 35, 'k' : 36,
    'l' : 37, 'm' : 38, 'n' : 39, 'o' : 40, 'p' : 41, 
    'q' : 42, 'r' : 43, 's' : 44, 't' : 45, 'u' : 46, 
    'v' : 47, 'w' : 48, 'x' : 49, 'y' : 50, 'z' : 51, 
    '0' : 52, '1' : 53, '2' : 54, '3' : 55, '4' : 56, 
    '5' : 57, '6' : 58, '7' : 59, '8' : 60, '9' : 61, 
    '+' : 62, '/' : 63
  }

  number = BASE_64[ ch ]

  return number_to_octeat( number )

def number_to_octeat( num ):
  binary = ''

  while num > 0:
    bit = num % 2

    binary += '0' + binary if bit == 0 else '1' + binary
    
    num /= 2
  
  return check_octeat_size( binary )

def check_octeat_size( binary ):
  if len( binary ) < 6:
    add_zeros = 6 - len( binary )

    zeros = '0' * add_zeros

    binary = zeros + binary

  return binary

def octeats_to_bytes( binary_string ):
  binary_array = []

  while len( binary_string ) > 0:
    binary_array.append( binary_string[ :8] )

    binary_string = binary_string[8: ]

  return binary_array