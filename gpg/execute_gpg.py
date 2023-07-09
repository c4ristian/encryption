#!/usr/bin/env python
"""
This script starts a subprocess to call GnuPG for encrypting and decrypting a string. It was developed
under Kali Linux Release 2023.2.
"""

import subprocess
import getpass


def _main():
    """
    This function executes the script.

    :return: None.
    """
    # Define plain text
    text_to_encrypt = b"My plain text!"
    print("Plain text:", text_to_encrypt)

    # Read passphrase
    passphrase = getpass.getpass("Passphrase:")
    passphrase2 = getpass.getpass("Passphrase:")

    if passphrase != passphrase2:
        raise ValueError("Passphrases not identical!")

    # Perform encryption
    args = [
        "gpg",
        "--symmetric",
        "--cipher-algo", "AES256",
        "--batch",
        "--passphrase", passphrase2
    ]

    result = subprocess.run(
        args, input=text_to_encrypt,
        capture_output=True)

    encrypt = result.stdout
    print("Encrypted:", encrypt)

    # Perform decryption
    args = [
        "gpg",
        "--decrypt",
        "--cipher-algo", "AES256",
        "--batch",
        "--passphrase", passphrase2
    ]

    result = subprocess.run(
        args, input=encrypt,
        capture_output=True)

    decrypt = result.stdout.decode()
    print("Decrypted:", decrypt)


# This block calls the main function
if __name__ == "__main__":
    _main()
