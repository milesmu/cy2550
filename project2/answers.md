
## 1.1
-pbkdf2 stands for Password-Based Key Derivation Function 2. This turns a readable passphrase into a cryptographic key by running it through many rounds of hasing, making brute-force attacks harder. Without it, weak passphrases map to weak keys with zero protection
## 1.2
The checksums differ because AES-CBC generates a random IV (initialization vector) for every encryption.
Even w identical plaintax/passphrase, random IV gives totally different ciphertext each time.
If a file's two encryptions gave identical output, attackers can detect when it was sent twice. This is the vulnerability ECB mode has.

## 1.3
ECB gave 2 distinct repeated blocks, w the most common appearing 24 times. CBC gave all unique blocks, no repetition. ECB leaked the plaintext's structure. An attacker could see which chunks of text repeat This would reveal the same block appearing multiple times and give them info on repeating patterns. Before trusting that records are protected, I would ask: Which block cipher mode is being used? ECB mode would leak records that are the same even withou breaking the key.
## 2.2
SHA-256 itself can't protect from attackers controlling the channel since they may modify files and compute a valid SHA-256 hash themself.
My colleague would never notice the mismatch, this cannot be tracked since the recipient would see a matching hash.
The hash needs a shared secret key to compute with HMAC. In this case, the attacker could potentially modify the file, but would fail to get a valid HMAC. My colleague would detect the mismatch here.

## 3.3
The check proves that I (or whoever the user is) has successful access to the inbox. It cannot prove if I am actually the right person, since anyone could hypothetically access my email and pass this.
A way to verify the fingerprint securely would be to meet my classmate and compare the 40-character fingerprint together. This would be out of the attacker's control since they can't enter our conversation directly. It's offline.
cat ~/cy2550/project2/answers.md
