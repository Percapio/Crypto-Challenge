const decodeSingleByteXOR = ( toDecode ) => {
    // First, we decode the string from its hex to ASCII characters
    let decoded = decodeFromHex( toDecode );

    // Next we convert our characters in the decoded string to binary
    // and set it inside an Object for quick access
    const keys = {};

    Object.keys( decoded ).forEach( ch => {
      keys[ ch ] = convertLetterToBinary( ch );
    });


    // Max Score, Possible Answer, Possible Key
    let key, answer;
    let highScore = 0;

    // Once that is completed, we are going to iterate through all possible ASCII characters/symbols and convert them to binary
    for( let i=0; i< 256; i++ ) {
      let scored = 0;

      let character = String.fromCharCode( i );

      let binaryASCII = convertLetterToBinary( character );

      // building a possible answer as we go
      let possibleAnswer = '';

      // We now iterate through the keys object to do our XOR comparisons
      Object.keys( keys ).forEach( binaryOfKey => {
        let binaryResult = xorConversion( binaryASCII, binaryOfKey );

        // Add the frequency score to the parent score
        scored += frequencyScores( binaryResult );

        possibleAnswer += binaryToLetter( binaryResult );
      });

      // Check if score is valid, then add choose this answer and key
      if( scored > highScore ) {
        highScore = scored;
        key = character;
        answer = possibleAnswer;
      }
    }

    // Return the key and answer
    return key, answer;
};
