def bit_sum(word: str):
    return sum(ord(character) for character in word)


def bit_xor(word: str) -> int:
    hash_code = 0
    for c in word:
        hash_code = hash_code ^ ord(c)  # can also be shortened to hash_code ^= ord(c)
    return hash_code


def polynomial(word: str, constant: int) -> int:
    return sum(ord(letter) * constant ** (len(word) - index - 1) for index, letter in enumerate(word))


def cyclic_shift(s: str):
    mask = (1 << 32) - 1
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(character)
    return h

def main():
    words = ["stop", "tops", "spot"]
    for word in words:
        print(word, end=" ")
        print(polynomial(word, 33))


if __name__ == "__main__":
    main()