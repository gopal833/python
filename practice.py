a=[1,2,3]
b=a
b.append(4)
print(a) # [1,2,3,4]
print(b) # [1,2,3,4]
# What is the output of this code?



class animal:
    def __init__(self, name,breed):
        self.name = name
        self.breed = breed

    def behavior(self):
        return f"{self.name},which is {self.breed} makes a loud sound."
animal1 = animal("dog","labrador")
print(animal1.behavior())


i = 0
while i <= 3 :
    i += 2
    print("*")

i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")
     