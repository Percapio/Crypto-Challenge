from utility.open_read_file import open_file
from utility.char_to_binary import convert_letter_binary
from utility.test_for_xor import test_for_xor
from utility.binary_to_number import convert_binary_to_number
from utility.key_generator import key_generator
# from problem3 import convert_decode_to_key

frequencies = {
  'a': 0.0651738,
  'b': 0.0124248,
  'c': 0.0217339,
  'd': 0.0349835,
  'e': 0.1041442,
  'f': 0.0197881,
  'g': 0.0158610,
  'h': 0.0492888,
  'i': 0.0558094,
  'j': 0.0009033,
  'k': 0.0050529,
  'l': 0.0331490,
  'm': 0.0202124,
  'n': 0.0564513,
  'o': 0.0596302,
  'p': 0.0137645,
  'q': 0.0008606,
  'r': 0.0497563,
  's': 0.0515760,
  't': 0.0729357,
  'u': 0.0225134,
  'v': 0.0082903,
  'w': 0.0171272,
  'x': 0.0013692,
  'y': 0.0145984,
  'z': 0.0007836,
  ' ': 0.1918182 
}


## note: slow function
def detect_single_character_xor( file_name ):
  lines = open_file( file_name )

  # to track most likely string as answer
  max_score = 0
  final_answer = ''
  final_key = ''

  for line in lines:
    # strip the bad stuff
    to_decode = line.rstrip()

    # generate possible keys, do conversions and comparisons, along with
    # computing the frequencies of each character on a single line
    answers = convert_decode_to_key( to_decode )

    # grab most likely key of the string
    key = max( answers, key= answers.get )

    # convert to binary
    key_binary = convert_letter_binary( key )

    # do conversion again on string to find the letter the string output
    decoded = to_decode.decode('hex')

    score = 0
    answer = ''

    # convert and compare out of current string against most the string most
    # likely the answer
    for ch in decoded:
      ch_binary = convert_letter_binary( ch )

      xord = test_for_xor( ch_binary, key_binary )

      number = convert_binary_to_number( xord )

      letter = chr( number )

      if letter in frequencies:
        score += frequencies[ letter ]
        answer += letter
    
    if score > max_score:
      max_score = score

      final_answer = answer
      final_key = key
  
  return final_key, final_answer


def score( letter, keys, key ):
  # if ASCII value falls on a English letter, we take the number of occurences
  # and multiply it by the frequency value of the given character
  if letter in frequencies:
    return keys[ key ] * frequencies[ letter ]

  # if not, then return 0
  else:
    return 0


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
      binary_key = decoded_dict[ key ]

      scored += xor_conversion( binary_key, binary_ascii, keys, key )

    if scored > 0:
      answers[ chr( i ) ] = scored

  return answers


def xor_conversion( binary_key, binary_string, keys, key ):
  xord = test_for_xor( binary_key, binary_string )

  number = convert_binary_to_number( xord )

  if number in range(127):
    letter = chr( number )

    return score( letter, keys, key )
  else:
    return 0


def convert_array_to_bin( ch_array ):
  binary_dict = {}

  for ch in ch_array:
    binary_dict[ ch ] = ( convert_letter_binary( ch ) )
  
  return binary_dict


## Test Run
def run_test():
  print detect_single_character_xor('./files/problem4.txt')

run_test()
