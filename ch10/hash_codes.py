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

def main():
    words = ["stop", "tops", "spot"]
    print(string_cyclic_shift("an"))
    print(string_cyclic_shift("na"))


if __name__ == "__main__":
    main()