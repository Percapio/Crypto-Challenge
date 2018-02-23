module.exports = function convertLetterToBinary( letter ) {
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