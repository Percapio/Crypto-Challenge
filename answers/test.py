from utility.char_to_binary import convert_letter_binary
from utility.convert_decode_to_key import xor_conversion
from utility.re_score import re_xor


def find_single_character_xor( chunks ):
  # chunk = chunks[ i ]
  chunks = chunks.decode('hex')

  keys = {}
  for ch in chunks:
    keys[ ch ] = chunks.count( ch )
  
  binary_dict = {}
  for key in keys:
    binary_dict[ key ] = convert_letter_binary( key )

  answers = {}
  for j in range( 256 ):
    scored = 0

    binary_ascii = convert_letter_binary( chr( j ) )
    for key in keys:
      binary_key = binary_dict[ key ]
      scored += xor_conversion( binary_key, binary_ascii, keys, key )
    
    if scored > 0:
      answers[ chr( j ) ] = scored

  key = max( answers, key= answers.get )
  key_binary = convert_letter_binary( key )

  result = ''
  for ch in chunks:
    result += re_xor( ch, key_binary )

  return result

## Test Run
def run_test3():
  to_decode = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

  key =  find_single_character_xor( to_decode )

  print key

run_test3()