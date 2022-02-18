import requests, platform, os
import i18n
import constants

def get_random_word(language):
    lang_param = constants.LANG_PARAM.format(language) if language in constants.OTHER_LANGUAGES else ""
    url = constants.API + lang_param
    response = requests.get(url)
    word = response.json()
    return word[0]

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def init_translations(language):
    i18n.set('file_format', 'json')
    i18n.set('locale', language)
    i18n.set('fallback', 'en')
    i18n.load_path.append('./i18n')

def run():
    try:
        clear_screen()
        selected_language = input("Type your language (en: English, es: Español): ")
        init_translations(selected_language)
        word = get_random_word(selected_language)

        typed_char = ""
        guessed_chars = ['__'] * len(word)
        wrong_tries = 0
        is_game_started = False

        while typed_char != "0":
            clear_screen()
            print(i18n.t('foo.guess'), "\n")

            if typed_char not in word and is_game_started:
                wrong_tries += 1

            for count, value in enumerate(word):
                if typed_char.lower() == value.lower():
                    guessed_chars[count] = value
            
            for char in guessed_chars:
                print(char.upper(), end=' ')

            print("\n\n")
            print(i18n.t('foo.enter_char'))
            print(i18n.t('foo.type_to_exit'))
            typed_char = input("")
            is_game_started = True
        
        print(i18n.t('foo.the_word_was') + word)

    except:
        print(i18n.t('foo.closed'))


if __name__ == '__main__':
    run()