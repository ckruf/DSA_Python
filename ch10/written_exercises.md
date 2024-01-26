## 10.4

What is the worst-case running time for inserting n key-value pairs into an initially empty map M that is implemented with the UnsortedTableMap class?

Worst case of inserting n key-value pairs into UnsortedTableMap is O(n^2), because `__setitem__` searches the entire list each time (ie O(n)), since it has to check whether we are overwriting an existing value, or adding a new one.

## 10.6

Which of the hash table collision-handling schemes could tolerate a load factor above 1 and which could not?

Only separate chaining can deal with a load factor above 1. Other collision-handling schemes rely on there being empty slots in the bucket array into which it can store key-value pairs in case of collision.

## 10.7

Our Position classes for lists and trees support the eq method so that
two distinct position instances are considered equivalent if they refer to the same underlying node in a structure. For positions to be allowed as keys in a hash table, there must be a definition for the hash method that is consistent with this notion of equivalence. Provide such a hash method.

The hash method must be based on the node alone. So make a hash based on the node's `id()`:

```
def __hash__(self):
    return id(self._node)

```

## 10.8

What would be a good hash code for a vehicle identification number that is a string of numbers and letters of the form “9X9XX99X9XX999999,” where a “9” represents a digit and an “X” represents a letter?

Either polynomial hash code, or cyclic bit shift. Definitely not a sum or XOR based hash code, since we want order to matter.

## 10.9

<img src="./ex_10_9.png" >

## 10.10

<img src="./ex_10_10.png" >

## 10.11

<img src="./ex_10_11.png" >

## 10.12

<img src="./ex_10_12.png" >

## 10.13

What is the worst-case time for putting n entries in an initially empty hash table, with collisions resolved by chaining? What is the best case?

The worst case is that all the keys hash to the same value. Therefore, when adding the first key, there would be 0 collisions, second key would be 1 collision, third key would be 2 collisions, and so on. And all the entries which hash to the same value have to be iterated, to check whether we are adding a new key, or overwriting an existing one. This sum is esentially from 1 to n, which equals n*((n+1)/2), which is O(n^2). The best case for n insertions is O(n), since in the best case, each insertion is O(1).

## 10.14

<img src="./ex_10_14.png" >

