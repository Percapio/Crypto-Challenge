def key_generator():
  keys = {}

  for i in range(256):
    keys[ chr( i ) ] = 0
  
  return keys