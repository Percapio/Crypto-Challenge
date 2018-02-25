const convertHexToBinary    = require('./utilityfunctions/hextobinary'),
      convertBinaryToNumber = require('./utilityfunctions/binarytonumber'),
      testForXOR            = require('./utilityfunctions/testforxor'),
      convertLetterToBinary = require('./utilityfunctions/charactertobinary'),
      keyGenerator          = require('./utilityfunctions/keygenerator');


const finalAnswer = ( toDecode ) => {
  const findPossibleKeys = decodeSingleByteXOR( toDecode );

  /* side note: 
     after rendering all the possible answers, I chose the character where the
     solution seemed the most likely answer, which was 'X'.  In the next
     challenge is where I write out the 'scoring' function to find the best 
     possible solution with a frequency table
  */
  return findPossibleKeys[ 'X' ];
};

const xorComparisons = ( toDecode, keyDecodedChar ) => {
  let concatBinary   = [];
  let answerArrayed  = [];

  toDecode.split('').forEach( char => {
    let hexDecodedChar = convertHexToBinary( char );
    concatBinary.push( hexDecodedChar );
    
    if ( concatBinary.length === 2 ) {
      let xord     = testForXOR( concatBinary.join(''), keyDecodedChar );
      let number   = convertBinaryToNumber( xord );
      
      let asciiCha = String.fromCharCode( number );
      answerArrayed.push( asciiCha );
      concatBinary = [];
    }
  });

  return answerArrayed.join('');
};

const decodeSingleByteXOR = ( toDecode ) => {
  const keys      = keyGenerator();
  const keysArray = Object.keys( keys );
  
  for( let k=0; k< keysArray.length; k++ ) {
    let keyDecodedChar = convertLetterToBinary( keysArray[k] );

    
    let possibleAnswer = xorComparisons( toDecode, keyDecodedChar );

    let characterCount = countCharacters( possibleAnswer );

    keys[ keysArray[ k ] ] = {
      'answer'  : possibleAnswer,
      'chCount' : characterCount,
    };
  }
  
  return keys;
};

const countCharacters = ( string ) => {
  let counter = 0;

  string.split('').forEach( ch => {
    let number = ch.charCodeAt(0);

    if ( number > 64 && number < 123 ) {
      counter++;
    }
  });

  return counter;
};

const evaluateOutput = allKeys => {
  let mostLikely = {},
      topCount   = 0;

  Object.keys( allKeys ).forEach( key => {
    let number = key['chCount'];

    topCount = number > topCount ? number : topCount;
  });

  Object.keys( allKeys ).forEach( key => {
    let number = key['chCount'];

    if ( topCount === number) {
      mostLikely[ key ] = allKeys[ key ];
    }
  });

  return mostLikely;
};


// Test run
let stringToDecode = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736';

const testRun = finalAnswer( stringToDecode );

console.log( testRun );