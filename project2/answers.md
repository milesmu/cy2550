## 2.2
SHA-256 itself can't protect from attackers controlling the channel since they may modify files and compute a valid SHA-256 hash themself.
My colleague would never notice the mismatch, this cannot be tracked since the recipient would see a matching hash.
The hash needs a shared secret key to compute with HMAC. In this case, the attacker could potentially modify the file, but would fail to get a valid HMAC. My colleague would detect the mismatch here.

## 3.3
The check proves that I (or whoever the user is) has successful access to the inbox. It cannot prove if I am actually the right person, since anyone could hypothetically access my email and pass this.
A way to verify the fingerprint securely would be to meet my classmate and compare the 40-character fingerprint together. This would be out of the attacker's control since they can't enter our conversation directly. It's offline.
