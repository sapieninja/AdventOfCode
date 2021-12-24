#include <stdio.h>
#include <time.h>
long cachea[10000000];
long cacheb[10000000];
int amalgamate(int posa, int posb, int scorea, int scoreb)
{
    int out;
    out = 0;
    out += posa;
    out += posb * 10;
    out += scorea * 1000;
    out += scoreb * 100000;
    return out;
}

void noways(int posa, int posb, int scorea, int scoreb, long *aways, long *bways, int rolls[])
//aways and bways are pointers so two values can be returned
{
    int amalgamation,amalgatron;
    amalgamation = amalgamate(posa, posb, scorea, scoreb);
    if (cachea[amalgamation] != 0 || cacheb[amalgamation] != 0)
    {
        *aways = cachea[amalgamation];
        *bways = cacheb[amalgamation];
        return;
    }
    long totala = 0;
    long totalb = 0;
    long aget, bget;
    if (scorea >= 40 || scoreb >= 40)
    {
        *aways = 1;
        *bways = 0;
        cachea[amalgamation] = 1;
        cacheb[amalgamation] = 0;
        return;
    }
    for (int i = 0; i < 27; i++)
    {
        noways(posb, (posa + rolls[i] - 1) % 10 + 1,scoreb, scorea + (posa + rolls[i] - 1) % 10 + 1, &bget, &aget, rolls);
        totala += aget;
        totalb += bget;
    }
    *aways = totala;
    *bways = totalb;
    cachea[amalgamation] = totala;
    cacheb[amalgamation] = totalb;
    return;
}
int main()
{
    int rolls[] = {3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9};
    clock_t start,end;
    start = clock();
    long aways, bways;
    noways(10, 1, 0, 0, &aways, &bways, rolls);
    end = clock();
    if (aways>bways)
    {
        printf("%ld\n",aways);
    }
    if (bways>aways)
    {
        printf("%ld\n",bways);
    }
    double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("%f\n",cpu_time_used);
}
