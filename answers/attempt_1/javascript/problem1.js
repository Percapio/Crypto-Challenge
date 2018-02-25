const convertHexToBinary    = require('./utilityfunctions/hextobinary'),
      convertBinaryToNumber = require('./utilityfunctions/binarytonumber');

const convertHexToBase64 = ( inputString ) => {
  const fullBinaryString = [];

  inputString.split('').forEach( el => {
    fullBinaryString.push( convertHexToBinary( el ) );
  });

  let octeatsArray = seperateIntoOcteats( fullBinaryString.join('') );

  const base64String = convertOcteatsToBase64( octeatsArray );

  return base64String;
};

// Seperate into Octeats
const seperateIntoOcteats = ( binaryString ) => {
  const octeatsArray = [];

  while( binaryString.length > 0) {
    octeatsArray.push( binaryString.slice(0, 6) );

    binaryString = binaryString.slice(6);
  }

  return octeatsArray;
};

// Convert Octeats into Base64
const convertOcteatsToBase64 = ( octeatsArray ) => {
  let base64Array = [];

  octeatsArray.forEach( octeat => {
    if( octeat.length === 6 ) {
      let number = convertBinaryToNumber( octeat );

      base64Array.push( convertNumberToBase64( number ) );
    } else {
      let times   = Math.abs( 6 - octeat.length );

      octeat      = addZerosToBinary( octeat, times );

      let number  = convertBinaryToNumber( octeat );

      base64Array.push( convertNumberToBase64( number ) );

      base64Array = addEqualSigns( base64Array );
    }
  });

  return base64Array.join('');
};

// Convert a number into Base 64
const convertNumberToBase64 = ( number ) => {
  const BASE_64 = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b',
    28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k',
    37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't',
    46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2',
    55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'
  };

  return BASE_64[ number ];
};

// Add zeros
const addZerosToBinary = ( binary, times ) => {
  for( let i=0; i<times; i++ ) {
    binary += '0';
  }

  return binary;
};

// Add equal signs
const addEqualSigns = ( base64 ) => {
  while( base64.length % 4 !== 0 ) {
    base64.push( '=' );
  }

  return base64;
};

// Run test
let stringToDecode = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d',
    answer  = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t';

let testRun = convertHexToBase64( stringToDecode );

testRun === answer ? console.log( 'Success!' ) : console.log( 'Fail.' );