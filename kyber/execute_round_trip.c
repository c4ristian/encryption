/*
Test of the Kyber encryption system based on its reference implementation.
The round_trip function tests a key exchange between two fictional parties,
Alice and Bob.
*/
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include "kem.h"
#include "randombytes.h"


// Function declarations
static void print_key(const char* name, const uint8_t* key);
void round_trip(void);


static void print_key(const char* name, const uint8_t* key) {
    printf("%s: ", name);
    for (int i = 0; i < 10; i++) {
        printf("%02X", key[i]);
    }
    printf("..\n");
}


void round_trip(void) {
    uint8_t pk[CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[CRYPTO_SECRETKEYBYTES];
    uint8_t ct[CRYPTO_CIPHERTEXTBYTES];
    uint8_t key_a[CRYPTO_BYTES];
    uint8_t key_b[CRYPTO_BYTES];

    //Alice generates a public key
    crypto_kem_keypair(pk, sk);
    print_key("Alice' public key", pk);

    //Bob derives a secret key and creates a response
    crypto_kem_enc(ct, key_b, pk);
    print_key("Bob's shared key", key_b);
    print_key("Bob's response key", ct);

    //Alice uses Bobs response to get her shared key
    crypto_kem_dec(key_a, ct, sk);
    print_key("Alice' shared key", key_a);
}


int main(void) {
    round_trip();
    return 0;
}
