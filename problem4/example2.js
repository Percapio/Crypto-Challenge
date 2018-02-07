const countCharacters = ( string ) => {
  let counter = 0;

  string.split('').forEach( ch => {
    let number = ch.charCodeAt(0);

    if ( number > 64 && number < 123 ) {
      counter++;
    }
  });

  return counter;
};