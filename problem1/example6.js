import convertNumToBin from './example1';
import convertBinToNum from './example3';

const decodeBase64 = ( base64 ) => {
  const BASE_64 = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b',
    28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k',
    37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't',
    46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2',
    55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'
  };  // cut and paste... you're my only friend
  
  const base64Array = base64.split('');  // split the base64 string

  const octeatArray = [];  // one cup of an array
  
  base64Array.forEach( el => {  // beat gently
    let baseNum = Object.keys( BASE_64 ).find( key => BASE_64[key] === el );  // remove shells

    octeatArray.push( baseNum );  // throw at pan
  });

  let arrayOfBinary   = octeatArray.map( el => {
    let newBinary     = convertNumToBin( el );
    let sliceLocation = newBinary.length - 6;

    return newBinary.slice( sliceLocation );
  });  // toss into bin

  arrayOfBinary = arrayOfBinary.join('');  // smoosh together

  const stringOutput = [];

  while (arrayOfBinary.length > 0) {
    let doubleBytes = arrayOfBinary.slice(0, 8);  // slice
    arrayOfBinary = arrayOfBinary.slice( 8 );     // dice

    let asciiChar = convertBinToNum( doubleBytes );
    asciiChar = String.fromCharCode( asciiChar );

    stringOutput.push( asciiChar );  // gobble it up
  }

  return stringOutput.join('');
};