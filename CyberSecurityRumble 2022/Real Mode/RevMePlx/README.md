# RevMePlx
## Solved By: [Blenderwizard](https://github.com/Blenderwizard)
## Worth: 100 points
## Total Solves: 201 solves
## Solution

Executing the binary prompts us for a diver name. Typing a random name cause the program to exit. Using ghidra, we can see the 3 avaliable options "Jeremy", "Simon", and "Adminiman".

"Jeremy" is the only interesting name to input, the other 2 cause the program print out a dive count and then exit. However, Inputing "Jeremy" causes the program to ask us for a password.

The inputed passwords are passed into a if statement with this condition `(input * 2 >> 8 == 1337)`. Therefor we can reverse the correct input by solving `((1337 << 8) / 2))` which is `171136`. Entering `171136` as a password prints out the flag.
