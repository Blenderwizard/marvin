#include <stdio.h>
#include <string.h>

int main(void) {
  char local_48 [64];
  
  setbuf(stdout,(char *)0x0);
  puts("Welcome to Crosland Tower, what will you be studying today?");
  gets(local_48);
  puts("okay, good luck!");
  return 0;
}
