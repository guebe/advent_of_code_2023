#include <stdint.h>
#include <stdio.h>

static uint16_t map[0x10000][2], key[0x1000];
static size_t keylen = 0;

static inline uint16_t enc(const char *s) { return (s[0]-'A')<<10|(s[1]-'A')<<5|(s[2]-'A'); }
static inline uint64_t gcd(uint64_t a, uint64_t b) { while (b != 0) { uint64_t tmp = a % b; a = b; b = tmp; } return a; }
static inline uint64_t lcm(uint64_t a, uint64_t b) { return (a / gcd(a, b)) * b; }

int main(void)
{
    FILE *f = fopen("input", "r");
    char *d = NULL, *l = NULL;
    size_t dsize = 0, lsize = 0;
    ssize_t dlen = getline(&d, &dsize, f);
    getline(&l, &lsize, f);
    while ((getline(&l, &lsize, f)) != -1) {
        uint16_t k = enc(l);
        map[k][0]  = enc(l+7);
        map[k][1]  = enc(l+12);
        if (l[2] == 'A') key[keylen++] = k;
    }

    uint64_t n = 1;
    for (size_t i = 0; i < keylen; i++) {
        size_t j = 0;
        uint16_t k = key[i];
        while ((k & 0x1F) != ('Z'-'A'))
            k = map[k][(d[(j++)%(dlen-1)] == 'L') ? 0 : 1];
        n = lcm(n, j);
    }
    printf("%lu\n", n);
}
