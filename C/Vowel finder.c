#include <stdio.h>
#include <stdlib.h>

int main()
{
    char x;

    printf("Enter a text :");
    scanf("%c",&x);

    switch(x)
    {
        case 'a' : printf("It's a Vowel");
        break;
        case 'e' : printf("It's a Vowel");
        break;
        case 'i' : printf("It's a Vowel");
        break;
        case 'o' : printf("It's a Vowel");
        break;
        case 'u' : printf("It's a Vowel");
        break;
        case 'A' : printf("It's a Vowel");
        break;
        case 'E' : printf("It's a Vowel");
        break;
        case 'I' : printf("It's a Vowel");
        break;
        case 'O' : printf("It's a Vowel");
        break;
        case 'U' : printf("It's a Vowel");
        break;
        default : printf("It's not a vowel");

    }
}
