# mtp
## Solved By: [Mout](https://github.com/killinq-joke)
## Worth: 438 point
## Total Solves: 73
## Solution

The server proposes you two choices:

1 - Encrypt message
2 - Get Flag

Choosing 2 gives you the encrypted flag which seems to just be the flag rotRANDED on every character

Choosing 1 gives you the opportunity to write your own message and get its content rotRANDED the same way

Since the message and the flag get the same encryption, I pushed messages filled with each of the same characters - ex: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" - to find the matches and keep on the matching index the same character

Once the cipher was equal to the flag's cipher, I knew I had the flag

And Voila