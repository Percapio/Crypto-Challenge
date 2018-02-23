module.exports = function keyGenerator() {
  let keys     = {};
  let alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');

  alphabet.forEach( letter => { keys[ letter.toUpperCase() ] = 0; } );
  alphabet.forEach( letter => { keys[ letter ] = 0; } );

  return keys;
};