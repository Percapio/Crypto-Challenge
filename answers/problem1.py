from utility.hex_to_binary import convert_hex_to_binary
from utility.binary_to_number import convert_binary_to_number


def convert_hex_to_base64( input_string ):
  binary_array = []

  # binary conversion for each character
  for ch in input_string:
    binary_array.append( convert_hex_to_binary( ch ) )
  
  # concat all the binaries into one big one
  binary_string = ''.join( binary_array )

  # seperate the long binary string into octeats
  octeats_arrayed = seperate_into_octeats( binary_string )

  # convert the octeats into base64 and return the result
  return convert_octeats_to_base64( octeats_arrayed )


def seperate_into_octeats( binary_array ):
  octeats = []

  while( len( binary_array ) > 0 ):
    octeat_string = ''.join( binary_array[0:6] )

    octeats.append( octeat_string )

    binary_array = binary_array[6:]
  
  return octeats


def convert_octeats_to_base64( octeats ):
  base64_array = []

  for octeat in octeats:
    if len( octeat ) == 6:
      number = convert_binary_to_number( octeat )

      base64_array.append( convert_number_to_base64( number ) )
    else:
      times = 6 - len( octeat )

      octeat = add_zeros_to_binary( octeat, times )

      converted_number = convert_binary_to_number( octeat )

      base64_array.append( convert_number_to_base64( converted_number ) )

      base64_array = add_equal_signs( converted_number )
    
  return ''.join( base64_array )



def convert_number_to_base64( number ):
  BASE_64 = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b',
    28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k',
    37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't',
    46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2',
    55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'
  }

  return BASE_64[ number ]

def add_zeros_to_binary( binary, times ):
  for i in range( times ):
    return binary.append('0')

  return binary

def add_equal_signs( base64_array ):
  while len( base64_array % 4 ) != 0:
    base64_array.append('=')
  
  return base64_array

## Test Run
def run_test():
  string_to_decode = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
  
  answer = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

  run_conversion = convert_hex_to_base64( string_to_decode )

  if run_conversion == answer:
    print 'Success! The result is ' + answer
  else:
    print 'Fail. The result is ' + answer

run_test()