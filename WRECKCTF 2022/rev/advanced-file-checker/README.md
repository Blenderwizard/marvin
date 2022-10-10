# advanced-flag-checker
## Solved By: [Blenderwizard](https://github.com/Blenderwizard)
## Worth: 343 points
## Total Solves: 135 solves
## Solution

Using Ghidra we can see that the flag is split into 4 byte chunks at memory address in reverse. We can simply reconstruct the flag by retrieving all the chunks and reversing them.
