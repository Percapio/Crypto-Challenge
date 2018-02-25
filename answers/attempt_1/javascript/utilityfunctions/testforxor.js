module.exports = function testForXOR( stringA, stringB ) {
  const results = [];

  for(let i=0; i< stringA.length; i++) {
    if( stringA[i] === stringB[i] ) {
      results.push( '0' );
    } else {
      results.push( '1' );
    }
  }

  return results.join('');
};