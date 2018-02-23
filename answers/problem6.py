from utility.open_read_file import open_file
from utility.convert_decode_to_key import convert_decode_to_key

from math import sqrt
import base64


def break_repeating_xor_key( file_name ):
  lines = open_file( file_name )

  for line in lines:
    # strip line of '\n'
    stripped_line = line.strip()

    # decrypt from base64
    decoded = base64.decodestring( stripped_line )

    ## binary of each decoded character and add 0's if length too short
    bytes_array = transform_bytes( decoded )

    ## iterate 2 through 40 key size guesses, create key size list
    #  of our bytes list, and performing hamming distance between
    # the keys
    possible_key_size = guess_size_length( bytes_array )

    # get list of possible key size bytes into a long list
    bytes_key_sizes = keysize_bytes( bytes_array, possible_key_size )

    # transpose into tuples list of ordered
    bytes_key_sizes = zip( *bytes_key_sizes )

    # solve each block of code
    jumbled_solution = []
    print bytes_key_sizes
    for key_size_list in bytes_key_sizes:
      return key_size_list
      jumbled_solution.append( convert_decode_to_key( key_size_list ))

  return jumbled_solution

def guess_size_length( bytes_array ):
  smallest_normalized = 100
  smallest_norm_key = 2

  for keysize in range(2, 41):
    keysize_array = keysize_bytes( bytes_array, keysize )

    sum_of_bits = find_hamming_distance( keysize_array )

    normalize = sum_of_bits / keysize
    print str( sum_of_bits ) + ': ' + str( normalize )

    if smallest_normalized > normalize:
      smallest_normalized = normalize

    else:
      if normalize < smallest_normalized:
        smallest_normalized = normalize

        smallest_norm_key = keysize

  print smallest_normalized
  return smallest_norm_key

def find_hamming_distance( keysize_array ):
  bits_a = []
  bits_b = []
  sum_of_bits = 0

  for i in range( len( keysize_array ) ):
    if i % 2 == 0:
      bits_a = ''.join( keysize_array[ i ] )
    else:
      bits_b = ''.join( keysize_array[ i ] )

      sum_of_bits += hamming_distance( bits_a, bits_b )
      
      bits_a = []
      bits_b = []
    
  return sum_of_bits

def keysize_bytes( bytes_array, keysize ):
  keysize_array = []

  for size in xrange(0, len( bytes_array ), keysize):
     bytes_tuple = bytes_array[size: size + keysize]

     keysize_array.append( bytes_tuple )
  
  return keysize_array

def transform_bytes( concat_file ):
  bytes_array = []

  for ch in concat_file:
    byte = ch_to_bytes( ch )

    bytes_array.append( byte )

  return bytes_array

def ch_to_bytes( ch ):
  byte = bin( ord( ch ) )

  if len( byte ) < 10:
    zeros = 10 - len( byte )

    zero = '0' * zeros

    byte = insert_zero( byte, zero )

  return byte

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

## Hamming Test
def test_hamming():
  string_a = 'this is a test'
  string_b = 'wokka wokka!!!'

  hamming = strings_to_hamming( string_a, string_b )

  print 'Success!' if hamming == 37 else 'Fail.'

# test_hamming()

## Test run
def run_test():
  print break_repeating_xor_key('./files/problem6.txt')

run_test()