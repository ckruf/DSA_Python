# Object oriented programming

## Goals of object oriented programming

### Robustness

Ability to gracefully handle unexpected inputs.

### Adaptibility

Make it easy to make changes to the software over time.

### Reusability

Write the code in such a way that it can be reused in the future in other programs.

## Object oriented design principles

### Modularity

The organizing principle in which different components of a software system are divided into functional units. 

### Abstraction

Distilling a complicated system down to its most fundamental parts - naming and explaining functionality, but not implementation. 

### Encapsulation

Putting together the data and the functions which operate on that data, and restricting access to the data only through designated functions. 

---

Encapsulation and abstraction are quite similar, and certain sources describe both in the same way. The main difference, as described in an StackOverflow [thread](https://stackoverflow.com/questions/742341/difference-between-abstraction-and-encapsulation) is that **encapsulation is about information hiding**, whereas **abstraction is about implementation hiding**.


## Design patterns

Design patterns are solutions to 'typical' software problems. A desing pattern consists of a name, which identifies the patten, a context, which describes how the pattern is applied and a result, which describes and analyzes what the pattern produces. The design patterns in this book fall into two general categories - algorithm design patterns and software engineering desing patterns.

### Algorithm design patterns

- Recursion 
- Amortization
- Divide and conquer 
- Prune and search (decrease and conquer)
- Brute force
- Dynamic programming
- The greedy method

### Software engineering design patterns

- Iterator
- Adapter 
- Position 
- Composition
- Template method
- Locator
- Factory method

### Design process

During the design process, we decide how to divide our program into classes, how they interact, what data each class will store, and what actions each class will perform. 

Some general principles:

1. Responsibilites: Divide the work into different actors, each with a different responsibility. Try to describe responsibilities using action verbs. These actors will form the classes for the program.

2. Independence: Define the work for each class to be as independent from other classes as possible. Subdivide responsibilities between classes so that each class has autonomy over some aspect of the program. Give data (as instance variables) to the class that has jurisdiction over the actions that require access to this data

3. Behaviors: Define the behaviors for each class carefully and precisely, so that the consequences of each action performed by a class will be well understood by other classes that interact with it. These behaviors will define the methods that this class performs, and the set of behaviors for a class are the interface to the class, as these form the means for other pieces of code to interact with objects from the class.


### Inheritance and abstract base classes 

In order to reduce repetition of code and to define the expected methods of related classes, it is common to define a common base class. A base class can either be abstract, or concrete. Abstract base classes cannot be instantiated. They contain abstract methods, which are methods without an implementation, only a function signature. In statically typed languages, abstract base classes are used to support polymorphism, as a variable can have the abstract base class as its declared type, even though it is an instance of a concrete subclass. In Python, since there are no declared types, abstract base classes are not needed to achieve polymorphism, and as such they are less common in Python than in languages like Java or C++.

Python's `collections` module contains several abstract base classes that help us define custom data structures which share a common interface with some of Python's built in data structures. These rely on the **template method pattern**. The template method pattern is when an abstract base class provides concrete behaviors which rely upon calls to other abstract behavior. As soon as a sub-class provides definitions for the missing abstract behavior, the inherited concrete behaviors are well defines. One example is Python's `Sequence` abstract base class, which provides methods `__contains__`, `index` and `count`, as long as definitions for `__getitem__` and `__len__` are provided. Here is an example of how Sequence could be defined:

```
class Sequence(metaclass=ABCMeta):
    
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""
    
    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence"""

    def __contains__(self, val):
        """Return True if val is found in sequence, False otherwise"""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False 
    
    def index(self, val):
        """Return the leftmost index at which val is found, or raise ValueError"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("value not in sequence")

    def count(self, val):
        """Return the number of elements equal to given value"""
        count = 0
        for j in range(len(self)):
            if self[j] == val:
                count += 1
        return count
```

By declaring the metaclass to be `ABCMeta`, Python then ensures that the abstract base class can not be instantiated, and that classes inheriting from it can not be instantiated if they do not provide implementations for the abstract methods.