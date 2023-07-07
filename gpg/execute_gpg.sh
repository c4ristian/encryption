#!/usr/bin/bash

# Encrypt
gpg --output encrypted.gpg --symmetric --cipher-algo AES256 plain.txt

# Decrypt
gpg --output decrypted.txt --decrypt encrypted.gpg