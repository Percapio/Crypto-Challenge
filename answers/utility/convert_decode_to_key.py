from utility.char_to_binary import convert_letter_binary
from utility.binary_to_number import convert_binary_to_number
from utility.test_for_xor import test_for_xor
from utility.score import score


def convert_decode_to_key( to_decode ):
  decoded = to_decode.decode('hex')

  keys = {}

  for ch in decoded:
    keys[ ch ] = decoded.count( ch )

  decoded_keys = keys.keys()

  decoded_dict = convert_array_to_bin( decoded_keys )

  answers = {}

  for i in range(256):  
    scored = 0

    binary_ascii = convert_letter_binary( chr( i ) )

    for key in keys:
      binary_key  = decoded_dict[ key ]

      scored += xor_conversion( binary_key, binary_ascii, keys, key )

    if scored > 0:
      answers[ chr( i ) ] = scored

  return answers


def xor_conversion( binary_key, binary_string, keys, key ):
  xord = test_for_xor( binary_key, binary_string )

  number = convert_binary_to_number( xord )

  if number in range(256):
    letter = chr( number ).lower()

    return score( letter, keys, key )
  else:
    return 0


def convert_array_to_bin( ch_array ):
  binary_dict = {}

  for ch in ch_array:
    binary_dict[ ch ] = ( convert_letter_binary( ch ) )
  
  return binary_dict
