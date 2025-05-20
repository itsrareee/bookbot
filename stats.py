def count_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in char_count:
                char_count[lower_char] += 1
            else:
                char_count[lower_char] = 1
    return char_count

def sort_on(char_count):
    return char_count["num"]

def start_sorting(char_count):
    sorting_list = []
    for char in char_count:
        num = char_count[char]
        sorting_list.append({'char': char, 'num': num})
    sorting_list.sort(reverse=True, key=sort_on)
    return sorting_list