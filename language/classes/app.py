class Employee(object):
    # class variables
    return_value = 12

    # init: the class constructor
    def __init__(self, name):
        self.name = name
    
    # the instance is always 
    def class_method_example(self):
        new_var1 = Employee.return_value # option 1: use the className, this way the class variables is the same for every instance of that class
        new_var2 = self.return_value # option 2: use the self, this way the class variable can be overriden on a per instance base
        return new_var2

# A parameter is a variable listed inside the parentheses in the function definition.
# An argument is a value that is passed to the function when it is called.

employee1 = Employee(name="test")
employee1.job = "teacher"
print(employee1.job)

# Python let's you add attributes to an object
# even if they are not part of the blueprint
employee1.pay = 10000

print(employee1.class_method_example())
print(Employee.class_method_example(employee1)) # the same as above