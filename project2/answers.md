# Part 1
## 1.1
-pbkdf2 stands for Password-Based Key Derivation Function 2. This turns a readable passphrase into a cryptographic key by running it through many rounds of hasing, making brute-force attacks harder. Without it, weak passphrases map to weak keys with zero protection

## 1.2
- The checksums differ because AES-CBC generates a random IV (initialization vector) for every encryption.
- Even w identical plaintax/passphrase, random IV gives totally different ciphertext each time.
- If a file's two encryptions gave identical output, attackers can detect when it was sent twice.
This is the vulnerability ECB mode has.

## 1.3
ECB gave 2 distinct repeated blocks, w the most common appearing 24 times. CBC gave all unique blocks, no repetition.
ECB leaked the plaintext's structure. An attacker could see which chunks of text repeat
This would reveal the same block appearing multiple times and give them info on repeating patterns.
Before trusting that records are protected, I would ask:
Which block cipher mode is being used? ECB mode would leak records that are the same even withou breaking the key.

