
# Used standard libraries for a more pleasant experience
def repeating_key_xor( to_encrypt, key ):
  # scale key length up to plain text length
  size_key = len( to_encrypt ) / len( key )

  longer_key = key * size_key

  # make sure the key isn't over/under scaled
  longer_key = check_key_size( to_encrypt, longer_key, key )

  # XOR them against each other
  to_encrypt = sxor( to_encrypt, longer_key )

  return to_encrypt.encode('hex')

def check_key_size( to_encrypt, longer_key, key ):
  if len( longer_key ) > len( to_encrypt ):
    longer_key = longer_key[: len( to_encrypt ) ]

  elif len( to_encrypt ) > len( longer_key ):
    longer_key += key[: len( to_encrypt ) - len( longer_key ) ]

  return longer_key

def sxor( string_a, string_b ):
  list_a = list( string_a )
  list_b = list( string_b )
  result = []

  for index in range( len( list_a ) ):
    xord = ord( list_a[ index ] ) ^ ord( list_b[ index ] )

    result.append( chr( xord ) )

  return ''.join( result )


## Test run
def run_test5():
  key = "ICE"

  test_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
  
  answer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
  
  test_run = repeating_key_xor( test_string, key )

  print 'Success!' if test_run == answer else "Fail."

run_test5()