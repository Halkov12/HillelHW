#1.
# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

def scramble(str1, str2):
    letter_counts = {}

    for char in str1:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    for char in str2:
        if char not in letter_counts or letter_counts[char] == 0:
            return False
        letter_counts[char] -= 1

    return True


#2.
# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"

#3.
#https://www.codewars.com/kata/587136ba2eefcb92a9000027/train/python

class SnakesLadders:
    def __init__(self):
        self.players = [0, 0]
        self.current_player = 0
        self.finished = False

        self.ladders = {
            2: 38, 7: 14, 8: 31, 15: 26, 21: 42,
            28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94
        }


        self.snakes = {
            16: 6, 46: 25, 49: 11, 62: 19, 64: 60,
            74: 53, 89: 68, 92: 88, 95: 75, 99: 80
        }

    def play(self, die1, die2):
        if self.finished:
            return "Game over!"

        move = die1 + die2
        player = self.current_player

        self.players[player] += move

        if self.players[player] > 100:
            self.players[player] = 100 - (self.players[player] - 100)

        self.players[player] = self.ladders.get(self.players[player], self.players[player])
        self.players[player] = self.snakes.get(self.players[player], self.players[player])

        if self.players[player] == 100:
            self.finished = True
            return f"Player {player + 1} Wins!"

        result = f"Player {player + 1} is on square {self.players[player]}"

        if die1 != die2:
            self.current_player = 1 - self.current_player

        return result


#4.
#https://www.codewars.com/kata/5629db57620258aa9d000014/train/python
from collections import Counter


def mix(s1, s2):
    count1 = Counter(c for c in s1 if 'a' <= c <= 'z')
    count2 = Counter(c for c in s2 if 'a' <= c <= 'z')

    result = []

    for char in 'abcdefghijklmnopqrstuvwxyz':
        max_count = max(count1[char], count2[char])

        if max_count > 1:
            if count1[char] == max_count and count2[char] == max_count:
                result.append(f"=:{char * max_count}")
            elif count1[char] == max_count:
                result.append(f"1:{char * max_count}")
            elif count2[char] == max_count:
                result.append(f"2:{char * max_count}")

    result.sort(key=lambda x: (-len(x), x))

    return '/'.join(result)

#5.
#https://www.codewars.com/kata/520446778469526ec0000001/train/python
def same_structure_as(arr1, arr2):
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        return False

    if len(arr1) != len(arr2):
        return False

    for a, b in zip(arr1, arr2):
        if isinstance(a, list) != isinstance(b, list):
            return False
        if isinstance(a, list) and isinstance(b, list):
            if not same_structure_as(a, b):
                return False

    return True
