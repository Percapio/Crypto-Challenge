# Detection
Challenge 4: [Detect single-character XOR](https://cryptopals.com/sets/1/challenges/4)

### Table Of Contents
* [Main Page](../)
* [Encoding Magic Numbers: Integers](../problem1/)
* [Digital Logic](../problem2/)
* [One Time Pad](../problem3/)
* Detection
* [link] Encryption
* [link] Error-prone coding
* [link] AES-128 in ECB? *what?*
* [link] TBD
---
### Detection
In the previous challenge, we were fortunate that the secret message was written in plain text english, but what if we were attempting to decrypt something that was not a silly string of words.  We would need a function that is more pragmatic in its approach.  Something more elegant than a brute force search, which is why we were given a hint to create a function that would check for character frequency.

By doing so, we can minimize the number of possible answers to a small fraction of the original output.

##### Parts of Challenge 3's solution
We are going to briefly discuss bits of the solution for challenge three in order to better understand today's challenge.

Below is one of the functions we used to solve the previous challenge.
```
const decodeSingleByteXOR = ( toDecode ) => {
  // Generate all the keys we believe is used in our encryption
  const keys      = keyGenerator();
  const keysArray = Object.keys( keys );
  
  for( let k=0; k< keysArray.length; k++ ) {
    // convert each key into binary for XOR cipher
    let keyDecodedChar = convertLetterToBinary( keysArray[k] );

    // find a possible answer string after XOR'd
    let possibleAnswer = xorComparisons( toDecode, keyDecodedChar );

    // do a count of actual letters within the string
    let characterCount = countCharacters( possibleAnswer );

    // save the output
    keys[ keysArray[ k ] ] = {
      'answer'  : possibleAnswer,
      'chCount' : characterCount,
    };
  }
  
  return keys;
};
```

As you can see, all it does it create a list of possible answer strings and counts the number of characters occurring in the string and populate a _keys_ object, so that we can use it in another function to discover our solution.

The important thing to note in this function is why we counted the characters after the XOR comparison and not before the XOR comparison.  The reason for it is because we are _heuristically_ assuming that the solution to today's problem will be one written in plain text and not an additional layer of cipher text that we need to decode.

When decoding other cipher blocks, we need to ensure that we always consider the importance of cipher/decypher orders, and we may sometimes have to try different orders to see which works best.

In the next function, we will see another _heuristic_ approach to our solution.  In it we count the number of times symbols appear in the given possible answer, but given that we are assumming the actual answer will be written in plain text English, we only account for capital and lower case English letters.
```
const countCharacters = ( possibleAnswer ) => {
  let counter = 0;

  possibleAnswer.split('').forEach( ch => {
    let number = ch.charCodeAt(0);

    // check letter based on ASCII number
    if ( number > 64 && number < 123 ) {
      counter++;
    }
  });

  return counter;
};
```

The reason we opted for this is to minimize the size of the counter, so we can reduce the number of possible keys as our answer.

Finally, we evaluate all the keys with their number of character occurrences and return an array of the most likely answers for further evaluation.
```
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
```

With this in mind, off you go to tackle today's challenge: [Detect single-character XOR](https://cryptopals.com/sets/1/challenges/4)

Good luck!

### Bonus
##### Symmetric-Key Encryption
Symmetric-Key Encryptions are algorithms that use the same cryptographic keys for both encryption of plain text and decryption of cipher text.  The keys themselves can be identical when used or is some transformation that occurs between the two keys.  For the last few challenges, we have been learning how to manipulate the most basic forms of symmetric-key encryptions.  The more advanced algorithms used on today's computers can be listed here: [GlobalSign](https://www.globalsign.com/en/blog/glossary-of-cryptographic-algorithms/).

