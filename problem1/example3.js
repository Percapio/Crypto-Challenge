const convertBinToNum = ( binary ) => {
  let binaryArray = binary.split('');      // make sure our bites are strings and then turn the whole thing into an array

  let convertedNumFromBinary = 0;      // our sum total we wish to return
  let power = binaryArray.length - 1;      // our max 2 ^ M power

  for (let i=0; i< binaryArray.length; i++) { 
    if (binaryArray[i] === '1') {              // Only do the math if 1 bit is present
      var twoPowerOfM = Math.pow( 2, power );  // grab our 2 ^ M
      
      convertedNumFromBinary += twoPowerOfM;  // add it to our sum total
    }
    
    power -= 1;                             // Lower the power after every iteration
  }

  return convertedNumFromBinary;
};

export default convertBinToNum;