import json, random, os
from types import SimpleNamespace

class GTASumoRandom():
    def __init__(self):
        self.classes = []
        self.players = ["Adam", "Alex", "Matt", "Taylor", "Courtney"]

        with open("GTA-Sumo.json", "r") as json_file:
            data = json_file.read()
            self.classes = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        
    def ListRandomCar(self, player):
        current_class = self.GetRandomClass()
        car = random.choice(current_class.cars)
        print_string = "Player: " + player + "\n" "Class: " + current_class.name + "\n" + "Car: " + car.name + "\n\n"
        print(print_string)

    def GetRandomClass(self):
        return random.choice(self.classes)

    
#hickity hasckity you smell nasity
if __name__ == "__main__":
    Rando = GTASumoRandom()
    
    solo = input("Enter the solo player: ")
    
    if (solo.lower() in (string.lower() for string in Rando.players)):
        Rando.players.remove(solo.capitalize())

        class_input = input("Enter the solo players car class: ")

        os.system('clear')

        current_class = next((x for x in Rando.classes if x.name.lower() == class_input.lower()), None)
        car = random.choice(current_class.cars)
        print("Solo player: " + solo.capitalize() + "\n" "Car: " + car.name + "\n\n")
    
    for player in Rando.players:
        Rando.ListRandomCar(player)
        