"""
CY2550 Project 3 - Secure Password Storage
"""

import bcrypt


def hash_password(password: str) -> str:
    """Return a secure hash of password suitable for database storage."""
    # gensalt() generates unique random salt each time
    # default cost factor is 12,2^12 iterations is slow
    salt = bcrypt.gensalt()
    # encode password to bytes, combine with salt, hash
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    # return as string
    return hashed.decode('utf-8')


def verify_password(password: str, stored_hash: str) -> bool:
    """Return True if password matches stored_hash, False otherwise."""
    # checkpw extracts salt embedded in stored_hash
    # rehashes input password with the salt and compares
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))


if __name__ == "__main__":
    test_password = "Hunter2!"
    wrong_password = "not_the_right_password"

    print("Testing hash_password() and verify_password()...")

    try:
        h = hash_password(test_password)
    except NotImplementedError:
        print("FAIL - hash_password() is not implemented yet.")
        raise SystemExit(1)
    except Exception as e:
        print(f"FAIL - hash_password() raised an exception: {e}")
        raise SystemExit(1)

    if not isinstance(h, str) or len(h) < 10:
        print(f"FAIL - hash_password() returned an unexpected value: {h!r}")
        raise SystemExit(1)

    if h == test_password:
        print("FAIL - hash_password() returned the plaintext password unchanged.")
        raise SystemExit(1)

    print(f"  hash_password() returned: {h[:30]}...")

    try:
        result_correct = verify_password(test_password, h)
    except NotImplementedError:
        print("FAIL - verify_password() is not implemented yet.")
        raise SystemExit(1)
    except Exception as e:
        print(f"FAIL - verify_password() raised an exception: {e}")
        raise SystemExit(1)

    if result_correct is not True:
        print(f"FAIL - verify_password(correct_password, hash) returned {result_correct!r}; expected True.")
        raise SystemExit(1)

    print("  verify_password(correct_password, hash) -> True")

    result_wrong = verify_password(wrong_password, h)
    if result_wrong is not False:
        print(f"FAIL - verify_password(wrong_password, hash) returned {result_wrong!r}; expected False.")
        raise SystemExit(1)

    print("  verify_password(wrong_password, hash) -> False")

    h2 = hash_password(test_password)
    if h == h2:
        print("WARN - hash_password() produced the same output twice for the same input.")
    else:
        print("  Two hashes of the same password are different (random salt)")

    print("\nAll tests passed. Your implementation looks correct.")
