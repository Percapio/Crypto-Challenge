// Import functions, so we don't re-write code
const convertBinToNum = require('./example3.js'),
      convertNumToBin = require('./example1.js');


module.exports = function convertStrToBase64( string ) {
  // definitely don't recommend anyone ever typing this out
  const BASE_64 = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b',
    28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k',
    37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't',
    46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2',
    55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'
  }; 

  // our string arrayed
  const arrayOfString = string.split('');

  // convert each char to ASCII
  const arrayOfASCII  = arrayOfString.map( el => el.charCodeAt() );

  // the binary string we will eventually concat
  let binaryString = [];

  arrayOfASCII.forEach( ascii => {

    // conversions and concations
    let shortenedBinaryString = convertNumToBin( ascii ).slice(4);
    binaryString.push( shortenedBinaryString );
  });

  let arrayOfBinary      = binaryString.join('').split(''); 

  // number of equal signs to pad out the hex encryption
  let numberOfEqualSigns = arrayOfBinary.length % 6;

  // make sure we pad
  if ( numberOfEqualSigns !== 0 ) {
    let numberOfZeros      = 6 - numberOfEqualSigns; 

    // pad it
    for (let i=0; i< numberOfZeros; i++) {
      arrayOfBinary.push( '0' );
    }
  }

  const base64Result = [];

  while (arrayOfBinary.length > 0) {

    // take the first octeat
    let octeat    = arrayOfBinary.slice(0, 6);

    // remove the first 6 positions
    arrayOfBinary = arrayOfBinary.slice( 6 );
    
    // conversion
    let binaryToBase64 = convertBinToNum( octeat.join('') );

    // key value check
    base64Result.push( BASE_64[ binaryToBase64 ] );
  }
  
  // pad that result
  if (numberOfEqualSigns > 0) {
    base64Result.push( '=' );
  }
  
  return base64Result.join('');
};