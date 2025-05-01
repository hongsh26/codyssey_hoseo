class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def info(self):
        print(f"name is {self.name}")
        print(f"weight is {self.weight}")

cat = Animal('cat', 10)
dog = Animal('dog', 15)

cat.info()
print()
dog.info()

