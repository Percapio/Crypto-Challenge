def number_to_hex( number ):
  HEX_LETTERS = { 
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
  }

  return str( number ) if number < 10 else HEX_LETTERS[ number ]