def get_word_count(text):
    return len(text.split())

def count_characters(text:str):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def list_of_dicts(dict):
    dicts = []
    for key, value in dict.items():
        dicts.append({'char' :key, 'num' : value})

    dicts.sort(key=lambda x: x['num'], reverse=True)
    return dicts
