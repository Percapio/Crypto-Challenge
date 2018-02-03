const convertNumToBin = ( number ) => {
  var binaryResult = [];   // first we set our Binary encoded array we wish to output

  while (number > 0) {                  // we iterate through the number until we can iterate no more
    var remainder = number % 2;         // next, modular the number by 2 to find the remainder
    binaryResult.unshift( remainder );  // then we add the result to the beginning of our binary array

    number = Math.floor( number / 2 );  // We divide our iterator by 2, and make sure it returns an integer
  }

  if ( binaryResult.length % 8 !== 0 ) {     // We check if the binary string is long enough
    let numberOfIterations = binaryResult.length % 8;

    for ( var i=0; i< numberOfIterations; i++ ) {  // If not, we add until it is
      binaryResult.unshift( 0 );
    }
  }

  return binaryResult.join('');
};

export default convertNumToBin;