class Plan:
    def __init__(self, name , height, age):
        self.name = name 
        self.height = height
        self.age = age 
class Flower(Plan):
    def __init__(self, name,height,age ,color):
        super().__init__(name,height,age)
        self.color = color

    def geet(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color.")
    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

class Tree(Plan):
    def __init__(self,name,height,age,trunk_diameter):
        super().__init__(name,height,age)
        self.trunk_diameter = trunk_diameter

        self.trunk_diameter /=10
        self.trunk_diameter *= self.trunk_diameter
        self.trunk_diameter *= 3.14  

    def geet(self):
        print(f"{self.name} (Tree): {self.height}cm, 1825 days, {self.age}cm diameter")
    def produce_shade(self):
        print(f"{self.name} provides {self.trunk_diameter} square meters of shade")

class Vegetable(Plan):
    def __init__(self, name , height, age,harvest_season,nutritional_value):
        super().__init__(name,height,age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def geet(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, summer harvest")
    def display_benefits(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

def main():
    
    f = Flower("Tomato", 25, 30, "red")
    f.geet()
    f.bloom()

main()