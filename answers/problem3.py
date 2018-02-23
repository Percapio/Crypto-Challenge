from utility.char_to_binary import convert_letter_binary
from utility.test_for_xor import test_for_xor
from utility.binary_to_number import convert_binary_to_number

from utility.convert_decode_to_key import convert_decode_to_key

def pick_most_likely_key( to_decode ):
  # decode from hex, then do binary XOR comparisons, then add up possible scores
  # for every letter (both capital and lowercase) in the English Alphabet
  possible_answers = convert_decode_to_key( to_decode )

  # choose the value with the highest probability
  key = max( possible_answers, key= possible_answers.get )

  # decode from hex to XOR conversion once again, but using key this time to
  # return the correct answer
  decoded = to_decode.decode('hex')

  key_binary = convert_letter_binary( key )

  answer = ''

  for ch in decoded:
    ch_binary = convert_letter_binary( ch )

    xord = test_for_xor( ch_binary, key_binary )

    number = convert_binary_to_number( xord )

    answer += chr( number )

  return key, answer


## Test Run
def run_test():
  to_decode = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

  key, answer =  pick_most_likely_key( to_decode )

  answer = '"' + answer + '"'

  print 'The key is ' + key + ' and the answer is ' + answer
   
run_test()