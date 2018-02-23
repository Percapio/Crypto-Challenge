def open_file( file_to_open ):
  file_opened = open( file_to_open, 'r' )
  
  lines = file_opened.readlines()

  file_opened.close()

  return lines