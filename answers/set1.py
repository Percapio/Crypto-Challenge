import base64


# Problem 1
#####################################################################
def convert_hex_to_base64( to_decode ):
  decoded = to_decode.decode('hex')
  return base64.b64encode( decoded )

# Problem 2
#####################################################################
def convert_string_with_fixed_xor( stringA, stringB ):
  if len( stringA ) != len( stringB ):
    return False

  stringA = stringA.decode('hex')
  stringB = stringB.decode('hex')
  
  result = xor_comparison( stringA, stringB )

  return result.encode('hex')

def xor_comparison( stringA, stringB ):
  result = ''
  for i in range( len( stringA ) ):
    letter  = single_character_xor( stringA[ i ], stringB[ i ] )
    result += letter
  return result

def single_character_xor( chA, chB ):
  xord = ord( chA ) ^ ord( chB )
  return chr( xord )

# Problem 3
#####################################################################
def decode_with_single_byte_xor( to_decode ):
  hex_decoded = to_decode.decode('hex')
  key         = locate_key( hex_decoded )

  answer = ''
  for ch in hex_decoded:
    answer += single_character_xor( key, ch )

  return key, answer

def locate_key( hex_decoded ):
  all_scores = {}
  for i in range( 256 ):
    letter = chr( i )
    build_score( letter, hex_decoded, all_scores )

  return max( all_scores, key=all_scores.get )

def build_score( letter, hex_decoded, all_scores ):
  scored = 0

  for ch in hex_decoded:
    xorded  = single_character_xor( letter, ch )
    scored += score( xorded )

  all_scores[ letter ] = scored

def score( letter ):
  letter = letter.lower()

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

  return frequencies[ letter ] if letter in frequencies else 0

# Problem 4
#####################################################################
def decode_line_in_file( _file ):
  lines = open_file_return_lines( _file )

  possible_answers = {}
  max_score = 0
  message   = ''
  true_key  = ''

  for line in lines:
    key, answer = decode_with_single_byte_xor( line.rstrip() )
    scores = 0
    for ch in answer:
      scores += score( ch )

    if max_score < scores:
      max_score = scores
      message   = answer
      true_key  = key

  return true_key, message

def open_file_return_lines( _file ):
  file_opened = open(_file, 'r')
  lines = file_opened.readlines()
  file_opened.close()
  return lines

# Problem 5
#####################################################################
def implement_repeating_xor_key( message, key ):
  encrypted = ''

  for i in range( len( message ) ):
    if i % 3 == 0:
      k = key[ 0 ]
    elif i % 3 == 1:
      k = key[ 1 ]
    elif i % 3 == 2:
      k = key[ 2 ]

    encrypted += single_character_xor( message[ i ], k )
  return encrypted.encode('hex')

# Problem 6
#####################################################################
def break_repeating_xor_key( _file ):
  lines = open_file_return_lines( _file )

def hamming_distance( stringA, stringB ):
  if len( stringA ) != len( stringB ):
    return False
  
  count = 0
  for i in range( len( stringA ) ):
    xorded = ord( stringA[ i ] ) ^ ord( stringB[ i ] )
    count += bin( xorded ).count('1')

  return count

## Test Run Problem 1
#####################################################################
def run_test1():
  string_to_decode = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
  answer = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
  run_conversion = convert_hex_to_base64(string_to_decode)

  return 'Success!' if str( run_conversion ) == answer else 'Fail.'

## Test Run Problem 2
#####################################################################
def run_test2():
  stringA = '1c0111001f010100061a024b53535009181c'
  stringB = '686974207468652062756c6c277320657965'
  answer = '746865206b696420646f6e277420706c6179'
  test_run = convert_string_with_fixed_xor(stringA, stringB)

  return 'Success!' if test_run == answer else 'Fail.'

## Test Run Problem 3
#####################################################################
def run_test3():
  to_decode = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
  key, answer = decode_with_single_byte_xor(to_decode)
  
  if key == 'X':
    return 'Success!', key, answer
  else:
    return 'Fail.', key, answer

## Test Run Problem 4
#####################################################################
def run_test4():
  key, answer = decode_line_in_file('./files/problem4.txt')

  if key == '5':
    return 'Success!', key, answer
  else:
    return 'Fail.', key, answer

## Test Run Problem 5
#####################################################################
def run_test5():
  key = "ICE"
  test_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
  answer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
  test_run = implement_repeating_xor_key(test_string, key)

  return 'Success!' if test_run == answer else "Fail."

## Test Run Problem 6 
#####################################################################
def run_test6():
  key = break_repeating_xor_key('./files/problem6.txt')

  print key 

def test_hamming():
  string_a = 'this is a test'
  string_b = 'wokka wokka!!!'

  hamming = hamming_distance(string_a, string_b)

  return 'Success!' if hamming == 37 else 'Fail.'

# Utilities
#####################################################################
def print_row(left, right):
  left = 'Running test on %s' % left
  print '{:>30}{:.>35}'.format(left, right)

def print_row_with_answer(left, func):
  message, key, answer = func
  left    = 'Running test on %s' % left
  key     = 'Key: %s' % key
  answer  = 'Message: %s' % answer
  print '{:>30}{:.>35}'.format(left, message)
  print '{:>20}'.format('Solution...')
  print '{:>20}     {:>5}'.format(key,answer)

# Main
#####################################################################
if __name__ == '__main__':
  print 'Running Tests for CryptoPals Challenge Set 1:'
  print_row( 'Problem 1', run_test1() )
  print_row( 'Problem 2', run_test2() )
  print_row_with_answer( 'Problem 3', run_test3() )
  print_row_with_answer( 'Problem 4', run_test4() )
  print_row( 'Problem 5', run_test5() )
  print_row( 'Hamming D', test_hamming() )
