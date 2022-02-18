import requests, constants

def get_random_word(language):
    lang_param = constants.LANG_PARAM.format(language) if language in constants.OTHER_LANGUAGES else ""
    url = constants.API + lang_param
    response = requests.get(url)
    word = response.json()
    return word[0]

def print_guessed_chars(guessed_chars):
    for char in guessed_chars: print(char.upper(), end=' ')