from person import Person
from salary import Salary
import uuid

id_person1 = uuid.uuid4()

p1 = Person('Guilherme', 30, id_person1)
s1 = Salary(id_person1, 3000)

print(p1.name)
print(p1.age)
print(p1.identify)

print(s1.amount)

s1.increase_salary(1000)

print('New salary for person 1 is: ', s1.amount)

s1.decrease_salary(3000)
print('New salary for person 1 is: ', s1.amount)

print('================================================================')

id_person2 = uuid.uuid4()

p2 = Person('Gustavo', 31, id_person2)
s2 = Salary(id_person2, 10000)

print(p2.name)
print(p2.age)
print(p2.identify)

print(s2.amount)