#!/usr/bin/env python
"""
This script starts a subprocess to call GnuPG for encrypting and decrypting a file.
"""

import subprocess
import getpass


def _main():
    """
    This function executes the script.

    :return: None.
    """
    # Read passphrase
    passphrase = getpass.getpass("Passphrase:")
    passphrase2 = getpass.getpass("Passphrase:")

    if passphrase != passphrase2:
        raise ValueError("Passphrases not identical!")

    # Perform encryption
    print("Encrypting...")

    args = [
        "gpg",
        "--batch",
        "--passphrase-fd", "0",
        "--output", "encrypted.gpg",
        "--symmetric",
        "--yes",
        "--cipher-algo", "AES256",
        "plain.txt",
    ]

    result = subprocess.run(
        args, input=passphrase.encode(),
        capture_output=True)

    if result.returncode != 0:
        raise ValueError(result.stderr)

    # Perform decryption
    print("Decrypting...")

    args = [
        "gpg",
        "--decrypt",
        "--batch",
        "--passphrase-fd", "0",
        "--output", "decrypted.txt",
        "--yes",
        "--cipher-algo", "AES256",
        "encrypted.gpg",
    ]

    result = subprocess.run(
        args, input=passphrase.encode(),
        capture_output=True)

    if result.returncode != 0:
        raise ValueError(result.stderr)

    print("Roundtrip successful!")


# This block calls the main function
if __name__ == "__main__":
    _main()
