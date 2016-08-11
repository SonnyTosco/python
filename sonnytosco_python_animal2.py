from sonnytosco_python_animal import Animal
class Dog(Animal):
    def __init__(self,name, health):
        self.name=name
        self.health=150
    def pet(self):
        self.health+=5
        return self
dog1=Dog("Debo",150)
dog1.walk().walk().walk().run().run().pet().displayHealth()
