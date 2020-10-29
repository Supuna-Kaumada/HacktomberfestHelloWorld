
#include <stdio.h>
#include <stdlib.h>

int main()
{
    float cm, m, km;

    /* get input in centimeter from user */
    printf("Enter length in centimeter: ");
    scanf("%f", &cm);

    /* Convert centimeter value into meter and kilometer */
    m = cm / 100.0;
    km    = cm / 100000.0;

    printf("Length in Meter = %.2f m \n", m);
    printf("Length in Kilometer = %.2f km", km);

    return 0;
}
