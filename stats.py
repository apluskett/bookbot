def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    from collections import Counter
    letters = [char.lower() for char in text if char.isalpha()]
    counts = Counter(letters)
    return sort_letter_counts(counts)

def sort_letter_counts(counts):
    letter_list = [{"char": char, "num": num} for char, num in counts.items()]
    letter_list.sort(key=lambda x: x["num"], reverse=True)
    return letter_list