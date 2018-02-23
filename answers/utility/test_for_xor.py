def test_for_xor( string_a, string_b ):
  results = []

  for i in range( len( string_a ) ):
    if string_a[ i ] == string_b[ i ]:
      results.append( '0' )
    else:
      results.append( '1' )

  return ''.join( results )