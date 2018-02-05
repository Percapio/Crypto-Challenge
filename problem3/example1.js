// Creating all possible keys
const oneTimePadKey = () => {
  const numbers = [];

  for( let i=0; i< 10; i++ ) {
    numbers.push( i );
  }

  return numbers;
};

// setting the keys to a pad
const POSSIBLE_KEYS = oneTimePadKey();

// encrypting a message, while also deleting any used keys
const oneTimePadEncryption = ( theSecretMessage ) => {
  const randIdx = [ Math.floor ( Math.random() * POSSIBLE_KEYS.length ) ];

  const key     = POSSIBLE_KEYS[ randIdx ];
  POSSIBLE_KEYS = POSSIBLE_KEYS.slice( 0, randIdx ).concat( POSSIBLE_KEYS.slice( randIdx + 1) );

  const binaryKey = convertLetterToBinary( key );
  const encryptedMessage = secretMessageEncryptor( theSecretMessage, binaryKey );

  return encryptedMessage;
};

// converting a letter to binary
const convertLetterToBinary = ( letter ) => {
  let number         = letter.charCodeAt(0);
  const binaryResult = [];   

  while (number > 0) {
    let remainder = number % 2;
    
    binaryResult.unshift( remainder );

    number = Math.floor( number / 2 );
  }

  if ( binaryResult.length !== 8 ) {
    let numberOfIterations = 8 - binaryResult.length;

    for ( let i=0; i< numberOfIterations; i++ ) {
      binaryResult.unshift( 0 );
    }
  }

  return binaryResult.join('');
};

// stepping through the secret message to do the conversions
const secretMessageEncryptor = ( theSecretMessage, key ) => {
  const encryptedMessage = [];

  theSecretMessage.split('').forEach( letter => {
    let binaryOfLetter = convertLetterToBinary( binaryOfLetter );

    let XORd = testForXOR( binaryOfLetter, key );

    let encryptedCharacter = convertBinaryToLetter( XORd );

    encryptedMessage.push( encryptedCharacter );
  });

  return encryptedMessage.join('');
};

// XOR conversion
const testForXOR = ( stringA, stringB ) => {
  const results = [];

  for(let i=0; i< stringA.length; i++) {
    if( stringA[i] === stringB[i] ) {
      results.push( '0' );
    } else {
      results.push( '1' );
    }
  }

  return results.join('');
};

// binary back to ASCII character
const convertBinaryToLetter = ( binary ) => {
  let binaryArrayed = binary.split('');

  let convertedBinaryToNumber = 0;

  let power = binary.length - 1;

  for( let i=0; i<binary.length; i++ ) {
    if( binaryArrayed[i] === '1' ) {
      let twoPower = Math.pow( 2, power );

      convertedBinaryToNumber += twoPower;
    }

    power -= 1;
  }

  return String.fromCharCode( convertedBinaryToNumber );
};