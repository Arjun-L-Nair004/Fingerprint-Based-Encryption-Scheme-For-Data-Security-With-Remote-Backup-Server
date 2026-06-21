import pyAesCrypt
from os import stat, remove
# encryption/decryption buffer size - 64K
# with stream-oriented functions, setting buffer size is mandatory
bufferSize = 64 * 1024
password = "please-use-a-long-and-random-password"

# encrypt
with open("data.txt", "rb") as fIn:
    with open("data.txt.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

# decrypt
with open("data.txt.aes", "rb") as fIn:
    try:
        with open("dataout.txt", "wb") as fOut:
            # decrypt file stream
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize)
    except ValueError:
        # remove output file on error
        remove("dataout.txt")