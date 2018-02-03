import convertBinToNum from './example3';    // Import functions, so we 
import convertNumToBin from './example1'; //  won't have to re-write code;

const convertHexToNumber = ( hex ) => {
  const HEX_LETTERS = { 
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
  }; // Letters to convert in a quick access object
  
  let binaryString = '';       // the string we are going to concat all octet with

  hex.split('').forEach( hexValue => {   // turn our given hex into an array and iterate
    
    let convertedNumToBinary;

    if (Object.keys( HEX_LETTERS ).includes( hexValue )) { // check inclusion in our object
      let capitalizeHexValue = hexValue.toUpperCase(); // to make sure it matches our key
      
      convertedNumToBinary = convertNumToBin( HEX_LETTERS[ capitalizeHexValue ] );
    } else {
      convertedNumToBinary = convertNumToBin( hexValue );
    }

    if ( convertedNumToBinary.length > 4) {
      convertedNumToBinary = convertedNumToBinary.slice( 4 );
    } // an extra step since we made our last function 8 bits in length

    binaryString = binaryString.concat( convertedNumToBinary );
  });

  return convertBinToNum( binaryString );
};