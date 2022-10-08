# my-frob
## Solved By: [Blenderwizard](https://github.com/Blenderwizard)
## Worth: 437 points
## Total Solves: 66
## Solution

Decompiling the code shows us that the binary reads a file, then applys an xor on every byte of the string with the values `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144`.

Thankfully, we only need to reverse the xor of 144 and 89, since the output after the xor of 55 is equal to the flag. (Look at decomp.c output)

Reversing an xor is easy, to find the value of p, simply xor x with q.
``` python
# p ^ q = x
# x ^ q = p
```

The script in solve reverses the output generated when connecting to the provided host and port, getting us the flag.