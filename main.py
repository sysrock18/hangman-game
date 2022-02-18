import i18n
import stickman
from unidecode import unidecode
from services import get_random_word, print_guessed_chars
from helpers import clear_screen, print_double_space

def init_translations(language):
    i18n.set('file_format', 'json')
    i18n.set('locale', language.lower())
    i18n.set('fallback', 'en')
    i18n.load_path.append('./i18n')

def display_result(word, tries_left):
    print_double_space()
    if tries_left == 0:
        print(i18n.t('foo.lost'))
        print(i18n.t('foo.the_word_was') + word)
    else:
        print(i18n.t('foo.win'))

def get_char_entered():
    print_double_space()
    print(i18n.t('foo.enter_char'))
    print(i18n.t('foo.type_to_exit'))
    return input("")

def run():
    try:
        clear_screen()
        selected_language = input("Type your language (en: English, es: Español): ")
        init_translations(selected_language)

        word = unidecode(get_random_word(selected_language))
        word = word.replace(" ", "").lower()
        EMPTY_SPACE = "__"

        typed_char = ""
        guessed_chars = [EMPTY_SPACE] * len(word)
        tries_left = len(stickman.get_stickmen()) - 1

        while typed_char != "0":
            clear_screen()
            print(i18n.t('foo.guess'), "\n")
            lower_typed_char = typed_char.lower()

            if lower_typed_char not in word and typed_char:
                tries_left -= 1
            else:
                for count, value in enumerate(word):
                    if lower_typed_char == value:
                        guessed_chars[count] = value
                
            print_guessed_chars(guessed_chars)

            print_double_space()
            stickman.display(tries_left)
            
            if EMPTY_SPACE in guessed_chars and tries_left > 0:
                typed_char = get_char_entered()
            else:
                break
        
        if typed_char != "0":
            display_result(word, tries_left)

    except:
        print(i18n.t('foo.closed'))


if __name__ == '__main__':
    run()