from utility.hex_to_binary import convert_hex_to_binary
from utility.binary_to_number import convert_binary_to_number
from utility.test_for_xor import test_for_xor


def convert_string_with_fixed_xor( string_a, string_b ):
  decoded_array = []

  for i in range( len( string_a ) ):
    # convert the hex characters into binary
    hex_decoded_ch = convert_hex_to_binary( string_a[i] )
    key_decoded_ch = convert_hex_to_binary( string_b[i] )

    # XOR compare them against one another
    decoded_binary = test_for_xor( hex_decoded_ch, key_decoded_ch )

    # change the binary to a number
    number = convert_binary_to_number( decoded_binary )

    # convert number to hex
    hex_ch = convert_number_to_hex( number )

    decoded_array.append( hex_ch )
  
  return ''.join( decoded_array )

def convert_number_to_hex( number ):
  HEX_DIGITS = {
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
  }

  return str( number ) if number < 10 else HEX_DIGITS[ number ]

## Test Run
def run_test():
  stringA = '1c0111001f010100061a024b53535009181c'
  stringB = '686974207468652062756c6c277320657965'
  answer  = '746865206b696420646f6e277420706c6179'

  test_run = convert_string_with_fixed_xor( stringA, stringB )

  if test_run == answer:
    print 'Success! The result is ' + test_run
  else:
    print 'Fail. The result is ' + test_run

run_test()