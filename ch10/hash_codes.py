def bit_sum(word: str):
    return sum(ord(character) for character in word)


def bit_xor(word: str) -> int:
    hash_code = 0
    for c in word:
        hash_code = hash_code ^ ord(c)  # can also be shortened to hash_code ^= ord(c)
    return hash_code


def polynomial(word: str, constant: int) -> int:
    return sum(ord(letter) * constant ** (len(word) - index - 1) for index, letter in enumerate(word))


def string_cyclic_shift(word: str):
    mask = (1 << 32) - 1
    hash_code = 0
    for character in word:
        hash_code = (hash_code << 5 & mask) | (hash_code >> 27)
        hash_code += ord(character)
    return hash_code

def cyclic_shift(n):
    mask = (1 << 32) - 1
    hash_code = n
    hash_code = (hash_code << 5 & mask) | (hash_code >> 27)
    return hash_code


def mad_hash(k: int) -> int:
    return ((3 * k) + 5) % 11

def secondary_hash(k: int) -> int:
    return 7 - (k % 7)

def main():
    nums = [54, 28, 41, 18, 10, 36, 25, 38, 12, 90]
    for key in nums:
        hash_code = (3 * key) % 17
        print(f"key {key}, hash {hash_code}")

if __name__ == "__main__":
    main()