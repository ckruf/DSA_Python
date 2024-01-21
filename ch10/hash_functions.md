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
...     return sum(ord(letter) * constant ** (len(word) - index - 1) for index, letter in enumerate(word))
```

The letters (or their Unicode integer value) are coefficients of different powers of the constant, depending on their order. Therefore, the polynomial hash codes for words with the same characters, in different order, are different:

stop 4,262,854
tops 4,293,382
spot 4,258,502

Evaluating the polynomial can cause the bits to overflow, but since we are merely interested in a good spread of the object x with respect to other keys, we simply ignore such overflows.

Regarding the constant `a`, experimental studies have shown that numbers 33, 37, 39 or 41 are particularly good choices, leading to less than 7 collisions on a list of over 50,000 English words.

#### Cyclic shift hash codes