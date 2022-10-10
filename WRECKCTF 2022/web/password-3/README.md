# password-3
## Solved By: [Blenderwizard](https://github.com/Blenderwizard)
## Worth: 403 points
## Total Solves: 93 solves
## Solution

The server is vulnurable to the same SQL injection that `password-2`. However this time the flag is stored in the password database we don't retrive the flag from having as sucessfull "password".

However we can abuse SQL's `LIKE` keyword. Using the fact that we get a success each time we input a correct "password" means the perfect oracle exists for bruteforcing the flag character by character. 

Once we find the next correct character we can begin to bruteforce the next one. Repeating until we encounter a `}`.

Example exploit `solve.py` in the solve folder.