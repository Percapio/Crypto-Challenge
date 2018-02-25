def convert_hex_to_binary( hex_char ):
  HEX_LETTERS = {
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
  }

  if hex_char in HEX_LETTERS:
    return convert_number_to_binary( HEX_LETTERS[ hex_char ] )
  else:
    return convert_number_to_binary( int( hex_char ) )


def convert_number_to_binary( number ):
  binary_array = []

  if number == 0: binary_array.append('0')

  while( number > 0 ):
    bit = number % 2
    binary_array.insert( 0, str( bit ) )
    number = number / 2

  binary_string = ''.join( binary_array )

  return binary_size_check( binary_string )

def binary_size_check( binary ):
  number_of_zeros = 4 - len( binary )

  binary = '0' * number_of_zeros + binary

  return binary