#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void my_memfrob(char *str, size_t len, int modif) {
	printf("%d: ", modif);
	for (int i = 0; i < len; i++) {
		str[i] = str[i] ^ modif;
		printf("%c", str[i]);
	}
	printf("\n");
}

void * load_flag(void) {
	FILE *fstream;
	size_t __n;
	char *__ptr;
	
	fstream = fopen("flag.txt","r");
	if (fstream == (FILE *)0x0) {
		exit(1);
	}
	fseek(fstream,0,2);
	__n = ftell(fstream);
	fseek(fstream,0,0);
	__ptr = malloc(__n + 1);
	if (__ptr == 0x0) {
		exit(1);
	}
	__ptr[__n] = 0;
	fread(__ptr,1,__n,fstream);
	fclose(fstream);
	return __ptr;
}

void print(char *str) {
	size_t length;
	int i;
	
	i = 0;
	while(1) {
		length = strlen(str);
		if (length <=i)
			break;
		printf("%hhx ", str[i]);
		i++;
	}
	puts("\n");
}

int main() {
	char inc;
	char *flag;
	size_t flag_len;
	int modif;
	int i;
	
	flag = (char *)load_flag();
	i = 1;
	modif = 1;
	while (modif != 233) {
		flag_len = strlen(flag);
		my_memfrob(flag,flag_len,modif);
		inc = (char)modif;
		modif = modif + i;
		i = (int)inc;
	}
	puts("\n");
	print(flag);
	return 0;
}