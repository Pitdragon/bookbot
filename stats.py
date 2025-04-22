from collections import defaultdict

def read_book(filename):
    """
    Reads the content of a file and returns it as a string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    """
    Counts the number of words in the given text.
    """
    return len(text.split())

def char_count(text):
    """
    Counts the frequency of each character in the given text.
    Returns a dictionary with characters as keys and their counts as values.
    """
    letters_counted = defaultdict(int)
    for char in text:
        char = char.lower()
        letters_counted[char] += 1
    return dict(letters_counted)

def sort_dict(d):
    """
    Sorts a dictionary by its values in descending order.
    Returns a list of tuples (key, value).
    """
    return sorted(d.items(), key=lambda item: item[1], reverse=True)

