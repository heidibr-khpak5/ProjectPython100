class Person:
    first_name: str = ''
    last_name: str = ''
person1 = Person()
person1.first_name = "Vic"
person1.last_name = "Vu"
person2 = Person()
person2.first_name = "Sue"
person2.last_name = "Jones"
print(person1.first_name, person1.last_name, person1)
print(person2.first_name, person2.last_name, person2)
