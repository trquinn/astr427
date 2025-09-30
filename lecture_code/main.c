#include <stdio.h>

int main(int argc, char **argv) 
{
    const int nstars = 100;
    struct {
        double u, v, ra, dec;
    } star[nstars];
    
    for(int i = 0; i < nstars; i++) {
        if(star[i].u - star[i].v < 2.0)
            printf("%f %f\n", star[i].ra, star[i].dec);
    }
}
    
