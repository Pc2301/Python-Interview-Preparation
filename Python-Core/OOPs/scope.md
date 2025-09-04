
1. Understanding class attrbute and scope of variable -> Public Variable 

```python
class Dog:

    species = "Canine"    # Class Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)


print(dog1.species)       # Canine
print(dog1.name)          # Buddy
print(dog2.name)          # Charlie

dog1.name = "Max"

Dog.species = "Feline"

print(dog1.species)       # Feline
print(dog2.species)       # Feline

```



2 . Understanding class attrbute and scope of variable - Protected

-> Protected is convention only 
-> Can be accessed outside class but not recommended


```python

class Dog:

    _species = "Canine"    # Class Attribute- protected 

    def __init__(self, name, age):
        self._name = name
        self._age = age


dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)


print(dog1._species)       # Canine
print(dog1._name)          # Buddy
print(dog2._name)          # Charlie

dog1._name = "Max"

Dog._species = "Feline"

print(dog1._species)       # Feline
print(dog2._species)       # Feline

```



3 . Understanding class attrbute and scope of variable - Private

-> Private -> name mangling 
-> Harder to access outside class , can be accessed by name mangling this prevents accidental override 

``` python
class Dog:

    __species = "Canine"    # Class Attribute- protected 

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_species(self):
        return Dog.__species


dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)


#print(dog1.__species)           # AttributeError: 'Dog' object has no attribute '__species'.
print(dog1._Dog__species)        # Canine   (Name Mangling : __species has been name mangled to _Dog__species)
#print(dog1.__name)               # AttributeError: 'Dog' object has no attribute '__name'.
print(dog1._Dog__name)           # Buddy
#print(dog2.__name)               # # AttributeError: 'Dog' object has no attribute '__name'.

#dog1._name = "Max"

#Dog._species = "Feline"

#print(dog1._species)       
#print(dog2._species)       

```