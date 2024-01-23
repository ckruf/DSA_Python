# Hash functions

Hash functions are used in a hash table in order to convert a key of any data type into an integer in range [0, N - 1], where N is the capacity of the bucket array for a hash table.

## Hash codes and compression functions

The hash function consists of two parts, a hash code, and a compression function.

The hash code maps the key to an integer (any integer), and the compression function then maps the hash code to an integer in the range [0, N - 1].

The hash code should be quick to compute and minimize compressions. 

### Hash code methods

#### Treating the bit representation as an integer

Python relies on 32 bit hash codes. So if we have a data type which can be represented using 32 bits or less, its hash code could just be the integer representation of its bits. 

A problem arises with data types which either use a bit representation greater than 32 bits, or which are a tuple of objects. An example of the former could be floating point integers, represented using 64 bits. An example of the latter could be a string, which is a tuple of characters, where each could be represented using 32 bits.

In these cases, we could either ignore some of the bits. For example for a 64 bit floating number, we could just use the higher order 32 bits or lower order 32 bits. However, this ignores half the information, and therefore increases collisions. 

Another possibility is to combine the information into a 32 bit number somehow. For example, we could add the individual parts into a single 32 bit integer, ignoring overflow. Or we can use an exclusive-or operation on the individual parts.

The problem with that, in the case of tuples, is that we lose information about the order of the objects. Using a sum, or a XOR, strings such as "stop", "post", "pots", "tops" (or indeed any strings made up of the same letters, in different order) produce the same hash code, and therefore lead to collisions.

Let's look at a more concrete XOR example, with the strings "stop", "tips" and "pots". The characters in these words have the following Unicode integer representations: s=115, t=116, o=111, p=112. We can use Python's `ord` function to get these. Their binary representations are:

```
s = 1110011
t = 1110100
o = 1101111
p = 1110000
```

Now let's XOR them:

```
s = 1110011
t = 1110100
    0000111
o = 1101111
    1101000
p = 1110000
    0011000
```

Which is 24 when converted to binary. Since the XOR operation is commutative, all of the words with the same characters, regardless of orderd, will have the same XOR hash code.


#### Polynomial hash codes

One way to produce a hash code for n-tuples, made up of the same objects, in a different order, are polynomial hash codes, which take the form:

a<sup>n-1</sup>x<sub>0</sub> + a<sup>n-2</sup>x<sub>1</sub> + ... + x<sub>n-2</sub>a + x<sub>n-1</sub>

Where x<sub>0</sub> up to x<sub>n-1</sub> are the objects of the n tuple, and a is a constant, being raised to various power. Mathematically speaking, this is a polynomial in a, with the various objects of the tuple as its coefficients. Therefore it's called a polynomial hash code. 

Let's do another example using the s. Experimentally, 33 has been shown to be a good value to produce few collisions for English words. Therefore, the hash code for "stop" would be computed as follows:

```
115 x 33^3 + 116 x 33^2 + 111x33 + 112
```

Which gives 4,262,854

We can use the following cool, hard-to-decipher one-liner to compute the hash codes:

```
def hash_code(word: str, constant: int) -> int:
    return sum(ord(letter) * constant ** (len(word) - index - 1) for index, letter in enumerate(word))
```

The letters (or their Unicode integer value) are coefficients of different powers of the constant, depending on their order. Therefore, the polynomial hash codes for words with the same characters, in different order, are different:

stop 4,262,854
tops 4,293,382
spot 4,258,502

Evaluating the polynomial can cause the bits to overflow, but since we are merely interested in a good spread of the object x with respect to other keys, we simply ignore such overflows.

Regarding the constant `a`, experimental studies have shown that numbers 33, 37, 39 or 41 are particularly good choices, leading to less than 7 collisions on a list of over 50,000 English words.

#### Cyclic shift hash codes

Another way to produce a hash code is to do a cyclic bit shift. This operation does not really have meaning in arithmetic, byt it achieve the goal of varying the bits of the calculation. Let's look at an example, using the following 32 bit value: 00111101100101101010100010101000. We take the leftmost five bits, highlighted using the pipe character here 00111|101100101101010100010101000. And we place them on the rightmost side of the original value, giving us: 101100101101010100010101000|00111. The pipe is again used just for highlighting purposes. In python, an implementation of the five bit cyclic shift is as follows:

```
def cyclic_shift(word: str):
    mask = (1 << 32) - 1
    hash_code = 0
    for character in word:
        hash_code = (hash_code << 5 & mask) | (hash_code >> 27)
        hash_code += ord(character)
    return hash_code
```

Let's look at an example to understand what exactly is happening.

The mask is used in order to make sure that the resulting hash code stays at 32 bits. The way this is achieved is that we generate the 32-bit binary value `0b11111111111111111111111111111111`. This is done by first generating the 33-bit value `0b100000000000000000000000000000000`, by taking 1 and doing a zero fill left shift by 32, expressed as `(1 << 32)`. And then we subtract one, which gives us the 32 bit binary value. Once we have this 32 bit value, we can take any binary value and AND it with this mask, allowing us to keep just the rightmost 32 bits, ensuring that the generated hash code does not exceed 32 bits.

Let's consider the string 'stop' again, and examine iteration-by-iteration what is going on.

First iteration

- The cyclic shift does not do anything, since h is just 0 on the first iteration
- We then add ord("s") to h, which is 115

Second iteration

- h is now 115, which in binary is the 7-bit value 1110011
- In the first half of the expression, we do a zero fill left shift by 5, giving us the 12-bit value 111001100000, and AND it with our mask, which doesn't change anything, since our value is less than 32 bits anyway
- The second half of the operation does a right shift of h (1110011) by 27 characters, which causes all the bits to fall off, and gives 0
- We then do an OR of the first half and the second half, which just gives the first half, because the second half is 0
- To sum up the bitwise operations:

```
bin(115) = '0b1110011'
'0b111001100000' << 5 = '0b111001100000'
'0b111001100000' AND '0b11111111111111111111111111111111' = 0b111001100000
'0b1110011' >> 27 = 0
'0b111001100000' OR 0 = 0b111001100000 = 3680
```

- We then add ord("t") to the result, which gives 3680 + 116 = 3796 

Third iteration

- h is now 3796, which in binary is the 12-bit value '0b111011010100'
- Again we do a zero fill left shift by 5, giving the 17-bit value '0b11101101010000000'
- The second half operation of a 27 bit right shift again gives 0, as all 17 bits are pushed off
- An OR between the 17-bit value from the first half and 0 again leaves the value unchanged at '0b11101101010000000', which is 121472 in decimal
- We then add ord("o") to the result, which gives 121472 + 111 = 121583

Fourth iteration

- h is now 121583, which in binary is the 17-bit value '0b11101101011101111'
- Again, we do a zero fill left shift by 5, giving the 22-bit value '0b1110110101110111100000'
- The second half operation of a 27-bit right shift of h again gives 0
- An OR between the 22 bit-value from the first half and 0 again leaves the value unchanged at '0b1110110101110111100000', which is 3890656
- We then add ord("p") to the result, which gives 3890656 + 112 = 3890768


Now, let's look at how the cyclic shift would work with the 32-bit value of '0b00111101100101101010100010101000', which is actually really a 30 bit value, since we can drop the two leading 0s

- the zero fill will give us the 35 bit value 0b11110110010110101010001010100000000
- ANDing this with the 32 bit mask will give us 0b10110010110101010001010100000000. It truncates the 35-bit value by only considering the rightmost 32 bits, dropping the front 3 bits
- Doing a 27-bit right shift of the original value leaves the first 3 bits of the value 111
- If we then OR these two values, we get the 32 bit value 0b10110010110101010001010100000111

As we can see, the result is indeed the cyclic shift.

Compare that to what happened in our example, where what effectively occured was just a zero fill left shift on the partial sums.

That's because in order for a cyclic shift to actually occur, rather than just a left shift, there have to be some non-zero bits in the leftmost 5 positions. Since those are the bits which get cycled to the back. Alternatively, we could consider it a cyclic shift for those smaller values also, if we imagine there to be leading zeroes. 

The smallest number undergoing an actual cyclic shift is 2 ** 27, or 0b00001000000000000000000000000000. Which has a 1 in the 5th position from the left. This is the 28th position position from the right, which is the bit corresponding to 2 ** 27. The 5 bit cyclic shift for this number results in 1.
