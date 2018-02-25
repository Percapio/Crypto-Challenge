def convert_letter_binary( letter ):
  ascii_number = ord( letter )
  binary_array = []

  while ascii_number > 0:
    bit = ascii_number % 2
    binary_array.insert( 0, str( bit ) )
    ascii_number = ascii_number / 2

  return binary_length_check( binary_array )

def binary_length_check( binary_array ):
  if len( binary_array ) != 8:
    number_to_iterate = 8 - len( binary_array )

    for i in range( 0, number_to_iterate ):
      binary_array.insert( 0, str( '0' ) )
  
  return "".join( binary_array )
