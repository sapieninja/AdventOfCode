#include <stdio.h>
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
    int amalgamation;
    amalgamation = amalgamate(posa, posb, scorea, scoreb);
    if (cachea[amalgamation] != 0)
    {
        *aways = cachea[amalgamation];
        *bways = cacheb[amalgamation];
        return;
    }
    if (cacheb[amalgamation] != 0)
    {
        *aways = cachea[amalgamation];
        *bways = cacheb[amalgamation];
        return;
    }
    long totala = 0;
    long totalb = 0;
    long aget, bget;
    if (scorea >= 21)
    {
        *aways = 1;
        *bways = 0;
        cachea[amalgamation] = 1;
        cacheb[amalgamation] = 0;
        return;
    }
    if (scoreb >= 21)
    {
        *aways = 0;
        *bways = 1;
        cachea[amalgamation] = 0;
        cacheb[amalgamation] = 1;
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
    long aways, bways;
    noways(10, 1, 0, 0, &aways, &bways, rolls);
    if (aways>bways)
    {
        printf("%ld\n",aways);
    }
    if (bways>aways)
    {
        printf("%ld\n",bways);
    }
}
