const convertHexToBinary    = require('./utilityfunctions/hextobinary'),
      convertBinaryToNumber = require('./utilityfunctions/binarytonumber'),
      testForXOR            = require('./utilityfunctions/testforxor');


const convertStringWithFixedXOR = ( stringA, stringB ) => {
  const decodedArray = [];
  
  for( let i=0; i< stringA.length; i++) {
    let hexDecodedChar = convertHexToBinary( stringA[i] );
    let keyDecodedChar = convertHexToBinary( stringB[i] );
    
    let decodedBinary  = testForXOR( hexDecodedChar, keyDecodedChar );
    
    let number = convertBinaryToNumber( decodedBinary );
    
    decodedArray.push( convertNumberToHex( number ) );
  }

  return decodedArray.join('');
};

const convertNumberToHex = ( number ) => {
  const HEX_DIGITS = {
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
  };

  return number < 10 ? number : HEX_DIGITS[ number ];
};

// Test run
let stringA = '1c0111001f010100061a024b53535009181c',
    stringB = '686974207468652062756c6c277320657965',
    answer  = '746865206b696420646f6e277420706c6179';

const testRun = convertStringWithFixedXOR( stringA, stringB );

testRun === answer ? console.log( 'Success!' ) : console.log( 'fail.' );