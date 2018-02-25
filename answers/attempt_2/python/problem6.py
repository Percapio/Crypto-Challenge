from utility.open_read_file import open_file
from utility.convert_decode_to_key import convert_decode_to_key
from utility.re_score import re_score
from utility.re_score import re_xor
from utility.char_to_binary import convert_letter_binary
from utility.convert_decode_to_key import xor_conversion

from math import sqrt
import base64


def break_repeating_xor_key( file_name ):
  lines       = open_file( file_name )
  p_key_sizes = {}

  # concat file into original format
  # full_file = ''
  # for line in lines:
  #   full_file += line.rstrip()

  full_file = ''.join( lines )

  # iterate from 2 to 40 keysizes, and do hemming distance
  # checks for each pair on the first two substrings
  # return the lowest hemming distance, but also the highest
  # key value
  find_key_sizes( full_file, p_key_sizes )
  print p_key_sizes
  key = int( most_likely_key( p_key_sizes ) )
  print key
  # create nested list with key number of chunky strings
  chunks = break_into_chunks( key, full_file )

  # detet single character XOR per chunk
  answer_key     = ''
  decoded_chunks = [ '' for _ in xrange( key ) ]
  
  for i in range( len( chunks ) ):
    answer_key += find_single_character_xor( i, chunks )

  return answer_key
  # return decoded_chunks
  # return sort_garbage( decoded_chunks )


def break_into_chunks( key, full_file ):
  chunks = [ '' for _ in xrange( key ) ]

  for i in range( 0, len( full_file ) - key, key ):
    for k in range( key ):
      chunks[ k ] += full_file[ i + k ]
  
  return chunks


def find_key_sizes( full_file, p_key_sizes ):
  chunks = {}

  for key_size in range( 2, 41 ):
    for substring in range( 0, len( full_file ) - key_size * 4, key_size * 4 ):
      string1 = full_file[ substring: substring + key_size ]
      string2 = full_file[ substring + key_size: substring + key_size * 2 ]
      string3 = full_file[ substring + key_size * 2: substring + key_size * 3 ]
      string4 = full_file[ substring + key_size * 3: substring + key_size * 4 ]

      hammingA = strings_to_hamming( string1, string2 )
      hammingB = strings_to_hamming( string3, string4 )

      normalized = float( (hammingA + hammingB) / (key_size * 2) )

      if key_size not in p_key_sizes:
        p_key_sizes[ key_size ] = normalized
        chunks[ key_size ]      = string1 + string2
      else:
        p_key_sizes[ key_size ] = ( p_key_sizes[ key_size ] + normalized ) / 2
        chunks[ key_size ]     += string1 + string2

  return chunks

def most_likely_key( p_key_sizes ):
  lowest_normalized = None
  likely_key        = None

  for key in p_key_sizes:
    if lowest_normalized == None:
      lowest_normalized = p_key_sizes[ key ]
      likely_key        = key
    elif lowest_normalized > p_key_sizes[ key ]:
      lowest_normalized = p_key_sizes[ key ]
      likely_key        = key
    elif lowest_normalized == p_key_sizes[ key ]:
      likely_key        = key
  
  return likely_key


def sort_garbage( garbage ):
  answer = [ '' for _ in xrange( len( garbage ) ) ]

  for g in range( len( garbage ) ):
    for ch in garbage[ g ]:
      answer[ g ] += ch

  return ''.join( answer )

def strings_to_hamming( string_a, string_b ):
  list_a = list( string_a )
  list_b = list( string_b )
  sum_of_bits = 0

  for index in range( len( list_a ) ):
    bits_a = convert_to_bits( list_a[ index ] )
    bits_b = convert_to_bits( list_b[ index ] )

    bits_a = check_bin_size( bits_a, bits_b )
    bits_b = check_bin_size( bits_b, bits_a )

    sum_of_bits += hamming_distance( bits_a, bits_b )
  
  return sum_of_bits

def hamming_distance( bits_a, bits_b ):
  sum_of_bits = 0

  zipped = zip( bits_a, bits_b )

  for a, b in zipped:
    if a != b:
      sum_of_bits += 1

  return sum_of_bits

def convert_to_bits( character ):
  number = ord( character )

  return bin( number )

def check_bin_size( string_a, string_b ):
  if len( string_a ) < len( string_b ):
    size = len( string_b ) - len( string_a )
    ooo = '0' * size
    string_a = insert_zero( string_a, ooo )
  
  return string_a

def insert_zero( string, zero ):
  string_beg = string[:4]
  
  return string_beg + zero + string[4:]

def find_single_character_xor( i, chunks ):
  chunk = chunks[ i ]

  keys = {}
  for ch in chunk:
    keys[ ch ] = chunk.count( ch )
  
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
  for ch in chunk:
    result += re_xor( ch, key_binary )
  
  return key
  # return key, result

## Hamming Test
def test_hamming():
  string_a = 'this is a test'
  string_b = 'wokka wokka!!!'

  hamming = strings_to_hamming( string_a, string_b )

  print 'Success!' if hamming == 37 else 'Fail.'

test_hamming()

## Test run
def run_test():
  key = break_repeating_xor_key('./files/problem6.txt')

  print key
  # print 'The key is ' + str( key ) + ' and the answer is: '
# run_test()
