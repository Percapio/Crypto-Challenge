# One Time Pad
Challenge 3: [Single-byte XOR cipher](https://cryptopals.com/sets/1/challenges/3)

### Table Of Contents
* [Main Page](../)
* [Encoding Magic Numbers: Integers](../problem1/)
* [Digital Logic](../problem2/)
* One Time Pad
* [Detection](../problem4/)
* [link] Encryption
* [link] Error-prone coding
* [link] AES-128 in ECB? *what?*
* [link] TBD
---
### One Time Pad
_What we are going to cover next doesn't directly relate to solving the challenge, but instead talks about why having a fixed XOR is not the "perfect" cipher._

In today's challenge, our objective is to solve a single-byte XOR that was already set in advance.  During the course of attempting to solve this problem, we will attempt to solve the challenge by looking for patterns that we can recognize.  These patterns are the fundamental reasons why a fixed password, whether XOR or not, is far from the "perfect" cipher.  Instead, there is something out there that could be considered the "perfect" cipher, but it comes with its own downfall.  This cipher is known as the One Time Pad.

The One Time Pad is a XOR cipher, much like the ones we have recently completed, but the difference is that the key to decode the cipher is randomized and paired once to each decryption.  Imagine a lock with only one key in the world capable of unlocking it, and after we use the key to unlock the lock, both key and lock disintegrates--never to be used again.  That is the One Time Pad.

Sounds perfect right?  Well, yes.  Especially, if we have something of significance to keep hidden away, but what if we needed to share what we have to a business partner, or an employee?  How many keys would have we to go through to keep our private information continuously hidden from unwanted eyes?  How many keys will have to be made before it would deter prying eyes from constantly attempting to brute force an answer to our encoding? 

The number is probably somewhere close to inifinity, as there will always be someone seeking to unlock the 'perfect' lock.

Encrypting information is a tricky business.  On one hand, we want to ensure that the encryption is secure, and by randomizing XOR, we ensure that the chances of any third party is able to gain access to our private information is reduced significantly.  Yet, at the same time, consistently changing our key to some random value is not a feasible solution, especially if we have to share this information with another party.

##### JavaScript Example
Let's explore creating a simple One Time Pad encryption function.

First, we create a simple array to create an array of 9 numbers, and we save it to a constant variable called _POSSIBLE_KEYS_ to be used in the future.
```
const oneTimePadKey = () => {
  const numbers = [];

  for( let i=0; i< 10; i++ ) {
    numbers.push( i );
  }

  return numbers;
};

const POSSIBLE_KEYS = oneTimePadKey();
```

Then, we create a simple encryption function using one of the possible keys.  In this function, we save the key we need to unlock it, and then we delete it from the constant _POSSIBLE_KEYS_ array to ensure we never use it again.
```
const oneTimePadEncryption = ( theSecretMessage ) => {
  const randIdx = [ Math.floor ( Math.random() * POSSIBLE_KEYS.length ) ];

  const key     = POSSIBLE_KEYS[ randIdx ];
  POSSIBLE_KEYS = POSSIBLE_KEYS.slice( 0, randIdx ).concat( POSSIBLE_KEYS.slice( randIdx + 1) );
};
```

We are going to use it to encrypt the secret message we were given with the key we have saved.  Before we do so, we need to turn our key into a binary string in order to XOR convert our secret message.
```
const convertKeyToBinary = ( key ) => {
  let number         = key.charCodeAt(0);
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
```

Now we step through the secretmessage, convert each character to binary and XOR it, and then return the encrypted message.
```
const secretMessageEncryptor = ( theSecretMessage, key ) => {
  const encryptedMessage = [];

  theSecretMessage.split('').forEach( letter => {
    let binaryOfLetter = convertLetterToBinary( binaryOfLetter );

    let XORd = testForXOR( binaryOfLetter, key );

    let encryptedCharacter = convertBinaryToLetter( XORd );

    encryptedMessage.push( encryptedCharacter );
  });

  return encryptedMessage.join('');
};
```

Voila!  Our encrypted message.  You may have noticed that there are a number of functions that were pre-written and used in our _secretMessageEncryptor_, that we didn't cover.  It was done on purpose, for the sake of the challenge, but I'm sure you can quickly figure it out.

Here's the challenge: [Single-byte XOR cipher](https://cryptopals.com/sets/1/challenges/3)

Once your done with that, go ahead and check out [example 1](../example1.js) and let me know how we can improve our secret message encryption functions.

Good luck!

___