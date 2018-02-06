function testForXOR ( stringA, stringB ) {
  // the array we want to return our XOR results with
  const results = [];

  for(let i=0; i< stringA.length; i++) {

    // if the strings match as being both false or true return 0
    if( stringA[i] === stringB[i] ) {
      results.push( '0' );
    } 
    
    // else we return 1 for true
    else {
      results.push( '1' );
    }
  }

  return results.join('');
}