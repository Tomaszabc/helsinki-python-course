# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return 0
   

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = ["a", "e", "i", "o", "u"]
        vowels_player1 = 0
        vowels_player2 = 0

        for char in player1_word.lower():
            if char in vowels:
                vowels_player1 += 1

        for char in player2_word.lower():
            if char in vowels:
                vowels_player2 += 1

        if vowels_player1 > vowels_player2:
            return 1
        elif vowels_player1 < vowels_player2:
            return 2
        else: 
            return 0

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # Sprawdź czy oba wpisy są poprawne
        valid = ["rock", "paper", "scissors"]
        
        if player1_word not in valid and player2_word not in valid:
            return 0  # obaj niepoprawni → remis
        
        if player1_word not in valid:
            return 2  # gracz 1 niepoprawny → wygrywa gracz 2
        
        if player2_word not in valid:
            return 1  # gracz 2 niepoprawny → wygrywa gracz 1
        
        # Obaj gracze wpisali poprawnie
        if player1_word == player2_word:
            return 0  # remis
        
        # Zasady gry
        if player1_word == "rock" and player2_word == "scissors":
            return 1
        if player1_word == "paper" and player2_word == "rock":
            return 1
        if player1_word == "scissors" and player2_word == "paper":
            return 1
        
        # W przeciwnym razie wygrywa gracz 2
        return 2
