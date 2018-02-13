// Import functions, so we don't re-write code
const convertBinToNum = require('./example3.js'),
      convertNumToBin = require('./example1.js');


module.exports = function convertHexToNumber( hex ) {
  // Letters object to convert quickly
  const HEX_LETTERS = { 
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
  };
  
  // the string we are going to concat all octet with
  let binaryString = '';

  // turn our given hex into an array and iterate
  hex.split('').forEach( hexValue => {
    let convertedNumToBinary;

    // check inclusion in our object
    if (Object.keys( HEX_LETTERS ).includes( hexValue )) {

      // to make sure it matches our key in HEX_LETTERS we capitalize the iterated item
      let capitalizeHexValue = hexValue.toUpperCase();
      
      convertedNumToBinary = convertNumToBin( HEX_LETTERS[ capitalizeHexValue ] );
    } else {
      convertedNumToBinary = convertNumToBin( hexValue );
    }

    // Hex is only 4 bits long, so we much remove an unnecessary bits
    if ( convertedNumToBinary.length > 4 ) {
      convertedNumToBinary = convertedNumToBinary.slice( 4 );
    }

    binaryString = binaryString.concat( convertedNumToBinary );
  });

  return convertBinToNum( binaryString );
};