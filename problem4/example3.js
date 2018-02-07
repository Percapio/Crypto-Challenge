const evaluateOutput = allKeys => {
  let mostLikely = {},
      topCount   = 0;

  Object.keys( allKeys ).forEach( key => {
    let number = key['chCount'];

    topCount = number > topCount ? number : topCount;
  });

  Object.keys( allKeys ).forEach( key => {
    let number = key['chCount'];

    if ( topCount === number) {
      mostLikely[ key ] = allKeys[ key ];
    }
  });

  return mostLikely;
};