#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony',
    'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    import copy
    from collections import deque

    dictionary = []
    with open(dictionary_file, 'r') as f:
        text = f.read()
        dictionary = text.split()

    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)
    previous = []

    if len(start_word) != len(end_word):
        return None

    if start_word == end_word:
        return stack

    while len(queue) != 0:
        a = queue.popleft()
        for x in dictionary:
            if _adjacent(x, a[-1]):
                if x == end_word:
                    print("You are done!")
                    a.append(x)
                    return a
                if x not in previous:
                    newStack = copy.copy(a)
                    newStack.append(x)
                    queue.append(newStack)
                    previous.append(x)

    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    if len(ladder) == 0:
        return False

    elif len(ladder) == 1:
        if ladder[0] == '':
            return False
        else:
            return True

    if _adjacent(ladder[0], ladder[1]):
        return verify_word_ladder(ladder[1:])

    if _adjacent(ladder[0], ladder[1]):
        return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) == len(word2):
        iteration = 0
        for i in range(len(word1)):
            if word2[i] != word1[i]:
                iteration += 1
        if iteration == 1:
            return True
        else:
            return False


_adjacent("phone", "phony")
verify_word_ladder(["stone", "shone", "phone"])
