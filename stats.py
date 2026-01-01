def get_book_text(F):
    with open(F) as f:
        file_contents = f.read()
    return file_contents

def count_words(F_content):
    count = len(F_content.split())
    return count

def get_num_words(P):
    cont = get_book_text(P)
    ans = count_words(cont)
    return ans

def get_count_of_each_char(P):
    content = get_book_text(P)
    occurances = dict()
    for char in content:
        if not char.isalpha(): continue
        char = char.lower()
        if char not in occurances:
            occurances[char] = 1
        else:
            occurances[char] += 1
    return occurances

def sort_occurances(D):
    sorted_D = dict(sorted(D.items(), key = lambda item : item[1], reverse = True))
    return sorted_D