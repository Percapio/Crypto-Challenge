module.exports = function convertNumToBin( number ) {
  // first we set our Binary encoded array we wish to output
  var binaryResult = [];   
  
  // we iterate through the number until we can iterate no more
  while (number > 0) {
    // next, modular the number by 2 to find the remainder
    var remainder = number % 2;

    // then we add the result to the beginning of our binary array
    binaryResult.unshift( remainder );

    // We divide our iterator by 2, and make sure it returns an integer
    number = Math.floor( number / 2 );
  }

  // We check if the binary string is long enough
  if ( binaryResult.length % 8 !== 0 ) {
    let numberOfIterations = 8 - binaryResult.length;

    // If not, we add until it is
    for ( var i=0; i< numberOfIterations; i++ ) {
      binaryResult.unshift( 0 );
    }
  }

  return binaryResult.join('');
};