# regular/class/static methods
- use a function decorator to assign class or static methods

## instance methods
- An instance method can access and even modify the value of attributes of an instance.
- It takes the instance as first argument. The default parameter is named `self`.


## class methods
- A class method is a method which is bound to the class and not the object/instance of the class.
- They have access to the state of the class as it takes a class parameter that points to the class and not the object instance.

- It can modify a class state that would apply across all the instances of the class.
    - For example, it can modify a class variable that would be applicable to all the instances.

- A class method receives the class as the implicit first argument (just like an instance method receives the instance.)
    - Class as first argument (naming convention: `cls`)

> You can use a class method as an alternative constructor


## static methods
- A static method does not receive an implicit first argument.
- A static method is also a method which is bound to the class and not the object of the class.
- A static method can’t access or modify class state.
- The function has some relevance to the class

> For example: You can use static methods to group functions together by organizing them in class.
