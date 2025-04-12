def get_num_words(text):
    words = text.split()
    return f"Found {len(words)} total words"

def group_by_character(text):
    group = {}
    for word in text.lower():
        for letter in word:
            if letter not in group:
                group[letter] = 1
            else:
                group[letter] += 1
    
    sorted_group = sort_character_group(group)
    return sorted_group



def sort_character_group(group):
    return sorted(group.items(), key=lambda item: item[1], reverse=True)
