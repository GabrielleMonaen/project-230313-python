import random


class Character:
    def __init__(self, name, health, energy, attack, defense, special_attack):
        self.name = name
        self.health = health
        self.energy = energy
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack

    def __str__(self):
        return f"{self.name} (HP: {self.health}, EP: {self.energy})"

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_move(self):
        return random.randint(1, self.attack)

    def defense_move(self):
        return random.randint(1, self.defense)

    def special_attack_move(self):
        self.energy -= 20
        return random.randint(self.attack, self.attack + 10)


class Game:
    def __init__(self):
        self.characters = [
            Character("Character 1", 100, 50, 10, 5, 25),
            Character("Character 2", 150, 30, 8, 8, 30),
            Character("Character 3", 120, 40, 12, 4, 20),
            Character("Character 4", 80, 60, 15, 3, 35),
            Character("Character 5", 200, 20, 6, 10, 40)
        ]
        self.player1 = None
        self.player2 = None
        self.current_round = 0

    def select_characters(self):
        print("Please select your characters:")
        for index, character in enumerate(self.characters):
            print(f"{index+1}. {character}")
        choice1 = int(input("Player 1, choose your character (1-5): "))
        choice2 = int(input("Player 2, choose your character (1-5): "))
        self.player1 = self.characters[choice1-1]
        self.player2 = self.characters[choice2-1]

    def play(self):
        self.select_characters()
        print(f"Player 1: {self.player1}")
        print(f"Player 2: {self.player2}")
        while True:
            self.current_round += 1
            print(f"\nRound {self.current_round}")
            print("Player 1, what do you want to do?")
            print("1. Attack")
            print("2. Defend")
            print("3. Special Attack")
            choice1 = int(input("Enter your choice (1-3): "))
            print("Player 2, what do you want to do?")
            print("1. Attack")
            print("2. Defend")
            print("3. Special Attack")
            choice2 = int(input("Enter your choice (1-3): "))
            if choice1 == 1:
                p1_move = self.player1.attack_move()
                print(f"Player 1 attacks with {p1_move} power")
                if choice2 == 1:
                    p2_move = self.player2.attack_move()
                    print(f"Player 2 attacks with {p2_move} power")
                    if p1_move > p2_move:
                        damage = p1_move - p2_move
                        print(f"Player 2 takes {damage} damage")
                        self.player2.take_damage(damage)
                    else:
                        print("Player 2 defends successfully")
                elif choice2 == 2:
                    p2_move = self.player2.defense_move()
                    print(f"Player 2 defends with {p2_move} power")
                    if p1_move > p2_move:
                        damage = p1_move - p2_move
                        print(f"Player 2 takes {damage} damage")
                        self.player2.take_damage(damage)
                    else:
                        print("Player 2 defends successfully")
                elif choice2 == 3:
                    p2_move = self.player2.special_attack_move()
                    print(
                        f"Player 2 uses special attack with {p2_move} power")
                    if p1_move > p2_move:
                        damage = p1_move - p2_move
                        print(f"Player 2 takes {damage} damage")
                        self.player2.take_damage(damage)
                    else:
                        print("Player 2 defends successfully")
                        self.player1.take_damage(p2_move)
            elif choice1 == 2:
                p1_move = self.player1.defense_move()
                print(f"Player 1 defends with {p1_move} power")
                if choice2 == 1:
                    p2_move = self.player2.attack_move()
                    print(f"Player 2 attacks with {p2_move} power")
                    if p2_move > p1_move:
                        damage = p2_move - p1_move
                        print(f"Player 1 takes {damage} damage")
                        self.player1.take_damage(damage)
                    else:
                        print("Player 1 defends successfully")
                elif choice2 == 2:
                    p2_move = self.player2.defense_move()
                    print(f"Player 2 defends with {p2_move} power")
                elif choice2 == 3:
                    p2_move = self.player2.special_attack_move()
                    print(
                        f"Player 2 uses special attack with {p2_move} power")
                    if p2_move > p1_move:
                        damage = p2_move - p1_move
                        print(f"Player 1 takes {damage} damage")
                        self.player1.take_damage(damage)
                    else:
                        print("Player 1 defends successfully")
            elif choice1 == 3:
                if self.player1.energy >= 20:
                    p1_move = self.player1.special_attack_move()
                    print(f"Player 1 uses special attack with {p1_move} power")
                    if choice2 == 1:
                        p2_move = self.player2.attack_move()
                        print(f"Player 2 attacks with {p2_move} power")
                        if p1_move > p2_move:
                            damage = p1_move - p2_move
                            print(f"Player 2 takes {damage} damage")
                            self.player2.take_damage(damage)
                        else:
                            print("Player 2 defends successfully")
                    elif choice2 == 2:
                        p2_move = self.player2.defense_move()
                        print(f"Player 2 defends with {p2_move} power")
                    elif choice2 == 3:
                        p2_move = self.player2.special_attack_move()
                        print(f"Player 2 uses special attack with {p2_move} power")
                        if p1_move > p2_move:
                            damage = p1_move - p2_move
                            print(f"Player 2 takes {damage} damage")
                            self.player2.take_damage(damage)
                        else:
                            print("Player 2 defends successfully")
                            self.player1.take_damage(p2_move)
                    self.player1.energy -= 20
                else:
                    print("Player 1 does not have enough energy to use special attack")
            else:
                print("Invalid choice. Please choose again.")
                continue

            # Check if either player has lost all their health points
            if self.player1.health == 0:
                print(f"{self.player1.name} is unconscious")
                print(f"{self.player2.name} wins the game!")
                break
            elif self.player2.health == 0:
                print(f"{self.player2.name} is unconscious")
                print(f"{self.player1.name} wins the game!")
                break

            # Check if maximum number of rounds has been reached
            if self.current_round == 10:
                if self.player1.health > self.player2.health:
                    print(f"{self.player1.name} wins the game!")
                elif self.player2.health > self.player1.health:
                    print(f"{self.player2.name} wins the game!")
                else:
                    print("The game is a tie!")
                break

            # Display updated player information for next round
            print(f"\n{self.player1} (EP: {self.player1.energy})")
            print(f"{self.player2} (EP: {self.player2.energy})")


if __name__ == '__main__':
    game = Game()
    game.play()

