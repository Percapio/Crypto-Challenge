def key_counter( keys, ch ):
  if keys.has_key( ch ):
    counter = keys[ ch ]
    counter += 1
    keys[ ch ] = counter
  else:
    keys[ ch ] = 0
  
  return keys