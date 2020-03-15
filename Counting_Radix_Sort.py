def radix_sort(list_of_words):
    """
    Sorts the words contained in the list in alphabetical order.
    :param list_of_words: List of words that need to be sorted
    :return: None
    :space_complexity: O(N) where N is the size of list_of_words
    """

    # Locates and stores the length of longest word in the list
    my_max = len(list_of_words[0][1])
    for j in range(1, len(list_of_words)):
        if my_max < len(list_of_words[j][1]):
            my_max = len(list_of_words[j][1])

    # Starts the counting sort of each letter from the longest word
    while my_max > 0:
        counting_sort(list_of_words, my_max)
        my_max -= 1


def counting_sort(list_of_words, column):
    """
    This function will modify the original list that has been passed in. ***
    A counting sort for letters.
    :param list_of_words: List of words that need to be sorted
    :param column: Index of letter(in word) to be sorted
    :return: None
    :space_complexity: O(N) where N is the size of list_of_words
    """
    output = []

    count = [[] for _ in range(26)]

    # sort each letter in a given column
    for j in range(len(list_of_words)):
        # accessing the lyric and checking if its longer than current column
        if len(list_of_words[j][1]) >= column:
            count_position = count[ord(list_of_words[j][1][column - 1]) - 97]
            count_position.append(list_of_words[j])
        # if it is then just append to front of list as it doesnt concern us for now
        else:
            count[0].append(list_of_words[j])

    # pop everything from the list to maintain stability
    for i in range(len(count)):
        while len(count[i]) != 0:
            output.append(count[i].pop(0))

    # copying the output list to the input list
    for i in range(len(output)):
        list_of_words[i] = output[i]