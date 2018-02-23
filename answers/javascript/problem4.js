const convertHexToBinary    = require('./utilityfunctions/hextobinary'),
      convertBinaryToNumber = require('./utilityfunctions/binarytonumber'),
      testForXOR            = require('./utilityfunctions/testforxor'),
      convertLetterToBinary = require('./utilityfunctions/charactertobinary'),
      keyGenerator          = require('./utilityfunctions/keygenerator');


const readFileAndDecode = () => {
  // const xml = new XMLHttpRequest();
  // xml.open( 'GET', file, false );

  // xml.onreadystatechange = function() {
  //   if( xml.readyState === 4 ) {
  //     if( xml.status === 200 || xml.status === 0 ) {
  //       let allText = xml.responseText;
  //       console.log( allText );
  //     }
  //   }
  // };

  let file = new File('./files/problem4.txt');

  return file;
};

console.log( 'hi' );
console.log( readFileAndDecode() );

const decodeSingleByteXOR = ( toDecode ) => {
  const keys      = keyGenerator();
  const keysArray = Object.keys( keys );
  
  for( let k=0; k< keysArray.length; k++ ) {
    let concatBinary   = [];
    let answerArrayed  = [];
    let keyDecodedChar = convertLetterToBinary( keysArray[k] );

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
    
    let possibleAnswer = answerArrayed.join('');
    
    keys[ keysArray[ k ] ] = possibleAnswer;
  }
  
  return keys;
};