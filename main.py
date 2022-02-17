import requests, platform, os
import constants

def get_random_word():
    response = requests.get(constants.API)
    word = response.json()
    return word[0]

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def run():
    try:
        word = get_random_word()
        guessed_char = ""
        guessed_chars = ['__'] * len(word)

        while guessed_char != "0":
            clear_screen()
            print("Guess the word!", "\n")

            for count, value in enumerate(word):
                if guessed_char.lower() == value.lower():
                    guessed_chars[count] = value
            
            for char in guessed_chars:
                print(char.upper(), end=' ')

            print("\n\n")
            guessed_char = input("Enter a char (type 0 to finish): ")

    except:
        print("Closed unexpectedly")


if __name__ == '__main__':
    run()