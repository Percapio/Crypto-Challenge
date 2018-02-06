// Import functions, so we don't re-write code
const convertBinToNum = require('./example3.js'),
      convertNumToBin = require('./example1.js');


module.exports = function decodeBase64( base64 ) {
  // cut and paste... you're my only friend
  const BASE_64 = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b',
    28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k',
    37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't',
    46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2',
    55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'
  };
  
  // split the base64 string
  const base64Array = base64.split('');

  // one cup of an array
  const octeatArray = [];
  
  // beat gently
  base64Array.forEach( el => {

    // remove shells
    let baseNum = Object.keys( BASE_64 ).find( key => BASE_64[key] === el );

    // throw at pan
    octeatArray.push( baseNum );
  });

  // toss into bin
  let arrayOfBinary   = octeatArray.map( el => {
    let newBinary     = convertNumToBin( el );
    let sliceLocation = newBinary.length - 6;

    return newBinary.slice( sliceLocation );
  }); 

  // smoosh together
  arrayOfBinary = arrayOfBinary.join('');

  const stringOutput = [];

  while (arrayOfBinary.length > 0) {
    // slice
    let doubleBytes = arrayOfBinary.slice(0, 8);

    // dice
    arrayOfBinary = arrayOfBinary.slice( 8 );

    // mix
    let asciiChar = convertBinToNum( doubleBytes );
    asciiChar = String.fromCharCode( asciiChar );

    // serve
    stringOutput.push( asciiChar );
  }

  return stringOutput.join('');
};