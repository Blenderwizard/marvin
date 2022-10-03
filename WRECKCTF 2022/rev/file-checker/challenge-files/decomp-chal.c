#include <stdio.h>
#include <stdlib.h>

void bad(void) {
  puts("Wrong answer!");
  exit(1);
}

int main(void) {
  int comp;
  size_t sVar2;
  long in_FS_OFFSET;
  char First [3];
  char Second [3];
  char Third [3];
  char Fourth [3];
  char Fifth [3];
  char Sixth [3];
  char Seventh [3];
  char Eigth [3];
  char Nineth [3];
  char Tenth [3];
  char Eleventh [3];
  char Twelfth [3];
  char Thirteenth [3];
  char last;
  
  fgets(First, 0x29 ,stdin);
  sVar2 = strlen(First);
  if (sVar2 != 0x28) {
    bad();
  }
  comp = strncmp(Eleventh,"d94",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(Third,"db_",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(Seventh,"35t",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(Fifth,"y0u",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(Fourth,"1s_",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(Tenth,"d_6",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(Second,"g{g",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(Eigth,"_fr",3);
  if (comp != 0) {
    bad();
  }
  if (last != '}') {
    bad();
  }
  comp = strncmp(Nineth,"13n",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(Thirteenth,"fa6",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(Sixth,"r_b",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(Twelfth,"620",3);
  if (comp != 0) {
    bad();
  }
  comp = strncmp(First,"fla",3);
  if (comp != 0) {
    bad();
  }
  puts("Nice job! Submit your answer as the flag.");
  return 0;
}

