# RevMePlx
## Solved By: [Blenderwizard](https://github.com/Blenderwizard)
## Worth: 100 points
## Total Solves: 201 solves
## Solution

Executing the binary prompts us for a diver name. Typing a random name cause the program to exit. Using ghidra, we can see the 3 avaliable options "Jeremy", "Simon", and "Adminiman".

"Jeremy" is the only interesting name to input, the other 2 cause the program print out a dive count and then exit. However, Inpting "Jeremy" causes the program to ask us for a password.

The inputed password is then passed into a if statement with this condition `(param_1 * 2 >> 8 == 1337)`. `param_1` being our input. therefor we can reverse the correct input by solving `((1337 << 8) / 2))` which is `171136`. Inputing that as out password gets us the flag.