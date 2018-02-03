const convertNumberToHex = ( number ) => {
  const HEX_DIGITS = 
    [ '0', '1', '2', '3', '4', '5', '6', '7', 
      '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' ];  // Hex number system

  let dividedNum = Math.floor( number / 16 );    // Divide the given value with 16
  let remainder  = number % 16;                  // Find the remainder
  let hexResult  = HEX_DIGITS[ remainder ];      // Find the first Hex Digit using the remainder

  while (dividedNum > 0) {                       // Repeat until we can no longer divide by 16
    dividedNum = Math.floor( dividedNum / 16 );
    remainder  = dividedNum % 16;
    hexResult  = HEX_DIGITS[ remainder ].concat( hexResult );  // Make sure to add the Hex Digit to the beginning of the Hex Result
  }

  return hexResult;
};