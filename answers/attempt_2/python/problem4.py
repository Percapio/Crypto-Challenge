from utility.char_to_binary import convert_letter_binary
from utility.open_read_file import open_file
from utility.convert_decode_to_key import convert_decode_to_key
from utility.re_score import re_score
from utility.re_score import re_xor


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
      letter = re_xor( ch, key_binary )

      score += re_score( letter )

      answer += letter
    
    if score > max_score:
      max_score = score

      final_answer = answer
      final_key = key
  
  return final_key, final_answer


## Test Run
def run_test4():
  print 'Please, wait a few seconds to completion.'

  key, answer = detect_single_character_xor( './files/problem4.txt' )

  print 'The key is ' + key + ' and the answer is: ' + answer

run_test4()
