module.exports = function convertHexToBinary( hexChar ) {
  const HEX_LETTERS = {
     'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
  };

  let binary;

  if( Object.keys( HEX_LETTERS ).includes( hexChar )) {
    binary = convertNumberToBinary( HEX_LETTERS[ hexChar ] );
  } else {
    binary = convertNumberToBinary( hexChar );
  }

  return binary;
};

// Convert a number into binary
const convertNumberToBinary = ( number ) => {
  const binaryArray = [];

  while( number > 0 ) {
    let bit = number % 2;
    binaryArray.unshift( bit );
    number  = Math.floor( number / 2 );
  }
  
  return binarySizeCheck( binaryArray ).join('');
};

// Check the length of a binary string
const binarySizeCheck = ( binary ) => {
  while( binary.length < 4 ) {
    binary.unshift('0');
  }
  
  return binary;
};