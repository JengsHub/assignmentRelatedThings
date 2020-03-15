# Snakey Words problem description
# This game is played on n × n grid of lowercase English letters, and involves finding words
# in this grid. We say this grid contains a word if the word exists as a chain in the grid.
# A chain is a sequence of letters a1, a2, ...an in the grid which are sequentially adjacent. In
# other words, the i+1th letter is vertically, horizontally or diagonally adjacent to the i
# th letter.
# You may not use the same grid cell for letter i and letter i + 1, however, you are allowed
# to re-use a letter in a chain.


def is_in(grid, word):
    """
    Function will check if the given word can be located in the letters grid.
    :param grid: List of lists where the outer list is N number long while each inner list contains N number of letters.
    :param word: This will be the word in query.
    :return: list of tuples containing a sequence of coordinates which will produce the given word when traced.
    :aux_space_complexity: 0(KN^2) where K is the number of characters in word and N is the length of grid.
    :time_complexity: 0(KN^2) where K is the number of characters in word and N is the length of grid.
    """

    len_of_grid = len(grid)
    result = []
    word_info = [0, 0, 0]
    memo = [[] for i in range(len_of_grid + 1)]
    for i in range(len(memo)):
        for j in range(len_of_grid + 1):
            memo[i].append([0])

    for i in range(1, len(word) + 1):
        # rows
        for y in range(1, len_of_grid + 1):
            # columns
            for x in range(1, len_of_grid + 1):
                # only run if the letter is the same
                if word[i - 1] == grid[y - 1][x - 1]:

                    # case when we reach bottom corner of grid
                    if y == len_of_grid and x == len_of_grid:
                        x_rotate = 1
                        y_rotate = 1
                        # keep rotating and find any count that is one lesser than the current count, then increment the
                        # current column if conditions are right. The current column will have its count
                        # incremented(appended) once
                        while y_rotate != -2 and x_rotate != -2:
                            if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate])-1] + 1 == i:
                                if memo[y][x][len(memo[y][x]) - 1] != i:
                                    memo[y][x].append(memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1)
                                    # when the count is higher than current max then update the info to word_info
                                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1 > word_info[0]:
                                        word_info[0] = memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1
                                        word_info[1] = y
                                        word_info[2] = x
                                # special condition check to see if the letter that caused the current slot to be
                                # incremented also carries the same value. If they are the same that means that both
                                # letters can come in either sequence.
                                if grid[y-1][x-1] == grid[y-1-y_rotate][x-1-x_rotate] and memo[y - y_rotate][x - x_rotate][len(memo[y-y_rotate][x - x_rotate])-1] == memo[y][x][len(memo[y][x])-2]:
                                    memo[y - y_rotate][x - x_rotate].append(memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1)

                            # conditions to check all three columns surrounding current column
                            if y_rotate == 0 and x_rotate == 1:
                                y_rotate = -2
                                x_rotate = -2
                            elif x_rotate != 0:
                                x_rotate -= 1
                            elif y_rotate == 1 and x_rotate == 0:
                                y_rotate = 0
                                x_rotate = 1

                    # case when we reach the last vertical side of grid
                    elif x == len_of_grid and y < len_of_grid:
                        x_rotate = 1
                        y_rotate = 1

                        # this loop's logic follows everything stated above
                        while x_rotate != -2 and y_rotate != -2:
                            if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate])-1] + 1 == i:
                                if memo[y][x][len(memo[y][x]) - 1] != i:
                                    memo[y][x].append(memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1)
                                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1 > word_info[0]:
                                        word_info[0] = memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1
                                        word_info[1] = y
                                        word_info[2] = x

                                if grid[y-1][x-1] == grid[y-1-y_rotate][x-1-x_rotate] and memo[y - y_rotate][x - x_rotate][len(memo[y-y_rotate][x - x_rotate])-1] == memo[y][x][len(memo[y][x])-2]:
                                    memo[y - y_rotate][x - x_rotate].append(memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1)

                            if y_rotate == 0 and x_rotate == 1:
                                x_rotate = 1
                                y_rotate = -1

                            elif x_rotate != 0:
                                x_rotate -= 1
                            elif y_rotate == -1 and x_rotate == 0:
                                x_rotate = -2
                                y_rotate = -2
                            else:
                                y_rotate -= 1
                                x_rotate = 1

                    # case when we reach the last horiontal side of grid
                    elif y == len_of_grid and x < len_of_grid:
                        x_rotate = 1
                        y_rotate = 1
                        # this loops logic follows everything stated above
                        while y_rotate != -2 and x_rotate != -2:
                            if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate])-1] + 1 == i:
                                if memo[y][x][len(memo[y][x]) - 1] != i:
                                    memo[y][x].append(memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1)
                                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1 > word_info[0]:
                                        word_info[0] = memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1
                                        word_info[1] = y
                                        word_info[2] = x
                                if grid[y-1][x-1] == grid[y-1-y_rotate][x-1-x_rotate] and memo[y - y_rotate][x - x_rotate][len(memo[y-y_rotate][x - x_rotate])-1] == memo[y][x][len(memo[y][x])-2]:
                                    memo[y - y_rotate][x - x_rotate].append(memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1)
                            if y_rotate == 1 and x_rotate == -1:
                                y_rotate = 0
                                x_rotate = 1
                            elif y_rotate == 0 and x_rotate == 1:
                                x_rotate -= 2
                            elif x_rotate != -1:
                                x_rotate -= 1
                            elif y_rotate == 0 and x_rotate == -1:
                                y_rotate = -2
                                x_rotate = -2

                    # case when column is in the middle and all eight columns need to be checked
                    else:
                        x_rotate = 1
                        y_rotate = 1
                        # this loops logic follows everything stated above
                        while y_rotate != -2 and x_rotate != -2:
                            if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1 == i:
                                if memo[y][x][len(memo[y][x])-1] != i:
                                    memo[y][x].append(memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1)
                                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1 > word_info[0]:
                                        word_info[0] = memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1
                                        word_info[1] = y
                                        word_info[2] = x
                                if grid[y-1][x-1] == grid[y-1-y_rotate][x-1-x_rotate] and memo[y - y_rotate][x - x_rotate][len(memo[y-y_rotate][x - x_rotate])-1] == memo[y][x][len(memo[y][x])-2]:
                                    memo[y - y_rotate][x - x_rotate].append(memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] + 1)

                            if y_rotate == 1 and x_rotate == -1:
                                y_rotate -= 1
                                x_rotate = 1
                            elif y_rotate == 0 and x_rotate == 1:
                                x_rotate -= 2
                            elif y_rotate == 0 and x_rotate == -1:
                                y_rotate -= 1
                                x_rotate = 1
                            elif y_rotate == 1 and x_rotate != -1:
                                x_rotate -= 1
                            elif y_rotate == -1 and x_rotate != -1:
                                x_rotate -= 1
                            elif y_rotate == -1 and x_rotate == -1:
                                y_rotate = -2
                                x_rotate = -2

    # if final length is not equal to word then the word is not found
    if word_info[0] != len(word):
        return False
    else:
        # back tracking process begins here
        result.append((word_info[1] - 1,word_info[2] - 1))
        while word_info[0] > 1:
            # set the y and x value here
            y = word_info[1]
            x = word_info[2]
            found = False

            # case when column is in the bottom corner
            if y == len_of_grid and x == len_of_grid:
                x_rotate = 1
                y_rotate = 1

                # keep rotating through columns to check
                while y_rotate != -2 and x_rotate != -2:
                    # rotate through each column to check if they have equal values, if they do means they should be
                    # popped off as the value is being handled with in this iteration. All surrounding columns
                    # are checked
                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] == word_info[0]:
                        memo[y-y_rotate][x-x_rotate].pop(len(memo[y - y_rotate][x-x_rotate]) - 1)

                    # if a value of (current value -1) is found, update the word info and append the y and x value as
                    # a tuple into the results list and changed found to be true. This step will only happen once as
                    # found is True after the first running iteration
                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] == word_info[0]-1 and found == False:
                        result.insert(0, (y - y_rotate - 1, x - x_rotate-1))
                        word_info[1] = y - y_rotate
                        word_info[2] = x - x_rotate
                        found = True

                    if y_rotate == 0 and x_rotate == 1:
                        y_rotate = -2
                        x_rotate = -2
                    elif x_rotate != 0:
                        x_rotate -= 1
                    elif y_rotate == 1 and x_rotate == 0:
                        y_rotate = 0
                        x_rotate = 1

                # decrements the word count in word_info each time a letter is found. The current column will also have
                # its value popped as the word might be reused in the sequence
                if found:
                    word_info[0] -= 1
                    memo[y][x].pop(len(memo[y][x]) - 1)

            # case when we reach the last vertical side of grid
            elif x == len_of_grid and y < len_of_grid:
                x_rotate = 1
                y_rotate = 1
                found = False

                # logic follows that of mentioned above (in the tracking back)
                while x_rotate != -2 and y_rotate != -2:
                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] == word_info[0]:
                        memo[y - y_rotate][x - x_rotate].pop(len(memo[y - y_rotate][x - x_rotate]) - 1)

                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] == word_info[0] - 1 and found == False:
                        result.insert(0, (y - y_rotate - 1, x - x_rotate-1))
                        word_info[1] = y - y_rotate
                        word_info[2] = x - x_rotate
                        found = True

                    if y_rotate == 0 and x_rotate == 1:
                        x_rotate = 1
                        y_rotate = -1

                    elif x_rotate != 0:
                        x_rotate -= 1
                    elif y_rotate == -1 and x_rotate == 0:
                        x_rotate = -2
                        y_rotate = -2
                    else:
                        y_rotate -= 1
                        x_rotate = 1

                if found:
                    word_info[0] -= 1
                    memo[y][x].pop(len(memo[y][x]) - 1)

            elif y == len_of_grid and x < len_of_grid:
                x_rotate = 1
                y_rotate = 1
                found = False
                # logic follows that of mentioned above (in the tracking back)
                while y_rotate != -2 and x_rotate != -2:
                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] == word_info[0]:
                        memo[y - y_rotate][x - x_rotate].pop(len(memo[y - y_rotate][x - x_rotate]) - 1)

                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] == word_info[0] - 1 and found == False:
                        result.insert(0, (y - y_rotate - 1, x - x_rotate-1))
                        word_info[1] = y - y_rotate
                        word_info[2] = x - x_rotate
                        found = True

                    if y_rotate == 1 and x_rotate == -1:
                        y_rotate = 0
                        x_rotate = 1
                    elif y_rotate == 0 and x_rotate == 1:
                        x_rotate -= 2
                    elif x_rotate != -1:
                        x_rotate -= 1
                    elif y_rotate == 0 and x_rotate == -1:
                        y_rotate = -2
                        x_rotate = -2

                if found:
                    word_info[0] -= 1
                    memo[y][x].pop(len(memo[y][x]) - 1)

            else:
                x_rotate = 1
                y_rotate = 1
                found = False
                # logic follows that of mentioned above (in the tracking back)
                while y_rotate != -2 and x_rotate != -2:
                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] == word_info[0]:
                        memo[y - y_rotate][x - x_rotate].pop(len(memo[y - y_rotate][x - x_rotate]) - 1)

                    if memo[y - y_rotate][x - x_rotate][len(memo[y - y_rotate][x - x_rotate]) - 1] == word_info[0] - 1 and found == False:
                        result.insert(0, (y - y_rotate - 1, x - x_rotate-1))
                        word_info[1] = y - y_rotate
                        word_info[2] = x - x_rotate
                        found = True

                    if y_rotate == 1 and x_rotate == -1:
                        y_rotate -= 1
                        x_rotate = 1
                    elif y_rotate == 0 and x_rotate == 1:
                        x_rotate -= 2
                    elif y_rotate == 0 and x_rotate == -1:
                        y_rotate -= 1
                        x_rotate = 1
                    elif y_rotate == 1 and x_rotate != -1:
                        x_rotate -= 1
                    elif y_rotate == -1 and x_rotate != -1:
                        x_rotate -= 1
                    elif y_rotate == -1 and x_rotate == -1:
                        y_rotate = -2
                        x_rotate = -2

                if found:
                    word_info[0] -= 1
                    memo[y][x].pop(len(memo[y][x]) - 1)
    return result