# The coin game.
# This game is played between 2 players, player 1 and player 2. There are two piles of coins.
# The values of a coin can be any integer. Both players know the values of all coins in both
# piles. Player 1 makes the first move, and play alternates between the players. A move
# consists of taking a coin from the top of either of the piles (either player can take from
# either pile). The game ends when both piles are empty. A player’s score is the sum of the
# values of all the coins they took during the game. The player with the higher score wins.


def best_score(pile1, pile2):
    """
    This function will calculate the best possible score for the player 1.
    :param pile1: List that contains numbers, last number in this list is equivalent to the coin on top of the pile.
    :param pile2: List that contains numbers, last number in this list is equivalent to the coin on top of the pile.
    :return: The highest possible score for player 1 and its corresponding sequence of moves for both players.
    :aux_space_complexity: O(NM) where N is the number of elements in pile 1 and M is the number of elements in pile 2.
    :time_complexity: O(NM)where N is the number of elements in pile 1 and M is the number of elements in pile 2.
    """
    first_pile = len(pile1)
    second_pile = len(pile2)
    turns = []

    memo = [[] for i in range(second_pile+1)]
    for i in range(len(memo)):
        memo[i] = [0]*(first_pile+1)

    # base case for the DP solution
    memo[0][0] = 0
    for rows in range(second_pile + 1):
        for columns in range(first_pile + 1):
            if rows == 0 and columns == 0:
                pass
            elif columns < 3 and rows == 0:
                memo[rows][columns] = pile1[columns - 1]
            elif rows < 3 and columns == 0:
                memo[rows][columns] = pile2[rows - 1]
            elif columns >= 3 and rows == 0:
                memo[rows][columns] = pile1[columns - 1] + memo[rows][columns - 2]
            elif rows >= 3 and columns == 0:
                memo[rows][columns] = pile2[rows - 1] + memo[rows - 2][columns]
            elif rows == 1 and columns == 1:
                memo[rows][columns] = max(pile1[columns - 1], pile2[rows - 1])
            elif rows == 1 and columns >= 2:
                memo[rows][columns] = max(pile1[columns - 1] + min(memo[rows][columns - 2], memo[rows - 1][columns-1]), pile2[rows - 1] + memo[rows-1][columns-1])
            elif rows >= 2 and columns == 1:
                memo[rows][columns] = max(pile1[columns - 1] + memo[rows-1][columns-1], pile2[rows - 1] + min(memo[rows-2][columns], memo[rows-1][columns-1]))
            else:
                memo[rows][columns] = max(pile1[columns - 1] + min(memo[rows - 1][columns - 1], memo[rows][columns - 2]), pile2[rows - 1] + min(memo[rows - 1][columns - 1], memo[rows-2][columns]))

    while first_pile > 0 or second_pile > 0:
        if second_pile == 0:
            minimum = memo[second_pile][first_pile - 1]
        elif first_pile == 0:
            minimum = memo[second_pile-1][first_pile]
        else:
            minimum = min(memo[second_pile][first_pile - 1], memo[second_pile - 1][first_pile])

        if minimum == memo[second_pile - 1][first_pile]:
            turns.append(2)
            second_pile -= 1

        else:
            turns.append(1)
            first_pile -= 1

    result = (memo[len(pile2)][len(pile1)], turns)

    return result