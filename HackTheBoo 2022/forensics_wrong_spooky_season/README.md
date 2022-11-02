# Wrong Spooky Season
## Solved By: [Blenderwizard](https://github.com/Blenderwizard)
## Worth: 200 points
## Solution

The Packet Capture file starts off as a normal dialogue between a webserver and a browser. At packet #416 a user begins executing commands from what seems to be a webshell. After a while the user switches from the webshell to using socat to execute a reverse shell on the host. We can see at packet 500 some reversed base64. Decoding it gives us the flag `HTB{j4v4_5pr1ng_just_b3c4m3_j4v4_sp00ky!!}`
