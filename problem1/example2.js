module.exports = function convertNumberToHex ( number ) {
  // Hex number system
  const HEX_DIGITS = 
    [ '0', '1', '2', '3', '4', '5', '6', '7', 
      '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' ];

  // Divide the given value with 16
  let dividedNum = Math.floor( number / 16 );

  // Find the remainder
  let remainder  = number % 16;

  // Find the first Hex Digit using the remainder
  let hexResult  = HEX_DIGITS[ remainder ];

  // Repeat until we can no longer divide by 16
  while (dividedNum > 0) {
    dividedNum = Math.floor( dividedNum / 16 );
    remainder  = dividedNum % 16;

    // Make sure to add the Hex Digit to the beginning of the Hex Result
    hexResult  = HEX_DIGITS[ remainder ].concat( hexResult );
  }

  return hexResult;
};