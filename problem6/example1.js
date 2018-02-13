const findHammingDistance = ( stringA, stringB ) => {

  // Counter of non-same bits
  let nonSameBitCounter = 0;

  // We are going to assume the string lengths are the same
  // and iterate through them using an index value to choose
  // each corresponding character in the string to do our
  // bit checks
  for( let i=0; i< stringA.length; i++) {

    // We have a small function that converts our characters
    // to ASCII number then to binary
    let bitsOfA = convertToBits( stringA[ i ] );
    let bitsOfB = convertToBits( stringB[ i ] );

    // We make sure our binary strings are of the same lengths
    bitsOfA, bitsOfB = checkBinarySize( bitsOfA, bitsOfB );

    // Another for-loop to check the bits within the binary strings
    // against one another for similarity

    for( let j=0; j< bitsOfA.length; j++ ) {
      if( bitsOfA[ j ] !== bitsOfB[ j ] ) {

        // if they are not the same, raise the counter by one
        nonSameBitCounter++;
      }
    }
  }

  return nonSameBitCounter;
}