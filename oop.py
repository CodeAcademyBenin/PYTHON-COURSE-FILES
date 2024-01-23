# OBJECT ORIENTED PROGRAMMING
"""
- Classes
- Objects
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

A class is identified by a name, attribute/properties, behaviours/methods.
"""

# Defining a Model/Class
"""
SYNTAX:
class name_of_class:
    attributes = ''         >>> Variable

    def name_of_method():   >>> Functions
        codes_under_method...
"""
class Person:
    number_of_persons = 0

    def __init__(self, name=None, age=None, complexion=None, height=None):
        self.name = name
        self.age = age
        self.complexion = complexion
        self.height = height

        Person.number_of_persons = Person.number_of_persons + 1
        

    # def __call__(self):
    #     Person.number_of_persons = Person.number_of_persons + 1
        

    def talking(self, words):
        print(f'\t {self.name}: {words}')

# Acessing Attributes
person1 = Person('John Diggle',45,'Dark','6ft')
# print('\t',person1.name)
# print(f'\t {Person.number_of_persons} persons created!!!')

person2 = Person('Oliver Queen',43,'Light','6ft')
person3 = Person('Felicity Babe',34,'Light','5ft')
# print(f'\t {Person.number_of_persons} persons created!!!')

# # Assigning values self defined to parameters.
person4 = Person(age=50)
person4.name = "John Doe"
person4.complexion = "Light"
# print('\t',person4.name)
# print('\t',person4.age)

# # Acessing Methods/Behaviour
# person1.talking("what's happening in Nigeria peeps!!!")
# person3.talking("We just rounded off the presidential election.")
# person2.talking("Guys, i think the election has been concluded")

# INHERITANCE
class Employee(Person):
    def __init__(self, role=None):
        self._role = role  
        # Encapsulation
        # The _ helps python interpreter identify role as an encapsulated attribute
        # While it does'nt have any special feature it performs on it, it flags a 
        # message to other programmers to restrict direct action on it.

    # Polymorphism
    # Here the inherited talking method was used in describing an employee.
    def about(self, words):
        return super().talking(words)


employee1 = Employee(role="staff")
employee1.name = "Micheal Todd"
employee1.height = "5.6ft"

print('\t', employee1.name)
employee1.talking("I just got a job in the company")
employee1.about("""
    I am a passionate individual with over 4 years experience managing teams for
    increased productivity. I have a degree in Management Science from the University
    of Ibadan. 
""")

# print(f'\t {Person.number_of_persons} persons created!!!')
