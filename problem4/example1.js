const decodeSingleByteXOR = ( toDecode ) => {
  // Generate all the keys we believe is used in our encryption
  const keys      = keyGenerator();
  const keysArray = Object.keys( keys );
  
  for( let k=0; k< keysArray.length; k++ ) {
    // convert each key into binary for XOR cipher
    let keyDecodedChar = convertLetterToBinary( keysArray[k] );

    // find a possible answer string after XOR'd
    let possibleAnswer = xorComparisons( toDecode, keyDecodedChar );

    // do a count of actual letters within the string
    let characterCount = countCharacters( possibleAnswer );

    // save the output
    keys[ keysArray[ k ] ] = {
      'answer'  : possibleAnswer,
      'chCount' : characterCount,
    };
  }
  
  return keys;
};