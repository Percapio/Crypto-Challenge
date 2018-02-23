module.exports = function convertBinaryToNumber( binary ) {
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

  return convertedBinaryToNumber;
};