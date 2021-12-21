#include <stdio.h>
long cachea[20000000];
long cacheb[20000000];
int amalgamate(int posa, int posb, int scorea, int scoreb, int turn)
{
    int out;
    out = 0;
    out += posa;
    out += posb * 10;
    out += scorea * 1000;
    out += scoreb * 100000;
    out += (turn % 2) * 10000000;
    return out;
}

void noways(int posa, int posb, int scorea, int scoreb, int turn, long *aways, long *bways, int rolls[])
//aways and bways are pointers so two values can be returned
{
    int amalgamation;
    amalgamation = amalgamate(posa, posb, scorea, scoreb, turn);
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
    if (turn % 2 == 0)
    {
        for (int i = 0; i < 27; i++)
        {
            noways((posa + rolls[i] - 1) % 10 + 1, posb, scorea + (posa + rolls[i] - 1) % 10 + 1, scoreb, turn + 1, &aget, &bget, rolls);
            totala += aget;
            totalb += bget;
        }
        *aways = totala;
        *bways = totalb;
        cachea[amalgamation] = totala;
        cacheb[amalgamation] = totalb;
        return;
    }
    else
    {
        for (int i = 0; i < 27; i++)
        {
            noways(posa, (posb + rolls[i] - 1) % 10 + 1, scorea, scoreb + (posb + rolls[i] - 1) % 10 + 1, turn + 1, &aget, &bget, rolls);
            totala += aget;
            totalb += bget;
        }
        *aways = totala;
        *bways = totalb;
        cachea[amalgamation] = totala;
        cacheb[amalgamation] = totalb;
        return;
    }
}
int main()
{
    int rolls[] = {3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9};
    long aways, bways;
    noways(10, 1, 0, 0, 0, &aways, &bways, rolls);
    printf("%ld,%ld\n", aways, bways);
}
