module.exports = function convertBinToNum( binary ) {
  // make sure our bites are strings and then turn the whole thing into an array  
  let binaryArray = binary.split('');

  // our sum total we wish to return
  let convertedNumFromBinary = 0;

  // our max 2 ^ M power
  let power = binaryArray.length - 1;

  for (let i=0; i< binaryArray.length; i++) {

    // Only do the math if 1 bit is present
    if (binaryArray[i] === '1') {

      // grab our 2 ^ M
      var twoPowerOfM = Math.pow( 2, power );
      
      // add it to our sum total
      convertedNumFromBinary += twoPowerOfM;
    }
    
    // Lower the power after every iteration
    power -= 1;
  }

  return convertedNumFromBinary;
};