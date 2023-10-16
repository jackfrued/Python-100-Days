import random

class Army:
    def __init__(self, name, units, resources):
        self.name = name
        self.units = units
        self.resources = resources

    def attack(self, enemy):
        if self.units > enemy.units:
            enemy.units -= random.randint(1, 5)
            return f"{self.name} wins the battle!"
        elif self.units < enemy.units:
            self.units -= random.randint(1, 5)
            return f"{enemy.name} wins the battle!"
        else:
            return "It's a draw!"

    def gather_resources(self):
        gathered = random.randint(1, 10)
        self.resources += gathered
        return f"{self.name} gathered {gathered} resources."

    def __str__(self):
        return f"{self.name}: {self.units} units, {self.resources} resources"


def main():
    player_army = Army("Player's Army", 100, 50)
    enemy_army = Army("Enemy Army", 100, 50)

    while player_army.units > 0 and enemy_army.units > 0:
        print(player_army)
        print(enemy_army)

        action = input("Choose an action (attack/gather/quit): ").lower()

        if action == "attack":
            result = player_army.attack(enemy_army)
            print(result)
        elif action == "gather":
            player_army.gather_resources()
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

    if player_army.units <= 0:
        print("Player's Army has been defeated.")
    if enemy_army.units <= 0:
        print("Player's Army wins the game!")

if __name__ == "__main__":
    main()
