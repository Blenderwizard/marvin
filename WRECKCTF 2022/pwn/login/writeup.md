# login
## Solved By: [Blenderwizard](https://github.com/Blenderwizard)
## Worth: 414 points
## Total Solves: 84
## Solution

Upon inspection of the provided source code, we can see that the dangerous gets function is used at line 50. We can use this to our advantage and perform a buffer overflow.
 
Attempting to perform a stack overflow to change the return address is useless since we have nowhere to jump and stack canaries are turned on.
 
However since the program doesn't modify the buffer containing the password after the call to gets and the buffer is located after the buffer that gets is writing to on the stack. We can overflow the password buffer to be whatever we want.
 
Simply overflow the password buffer to be whatever we put for the input buffer. Just remember to terminate both buffers with a null byte.
 
Example exploit in solve folder.
