def convert_binary_to_number( binary ):
  converted_number = 0
  power = len( binary ) - 1

  for bin in binary:
    if bin == '1':
      power_of_m = 2 ** power
      converted_number += power_of_m

    power -= 1
  
  return converted_number