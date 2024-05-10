import random
import sys

def read_file(file_name):
    file = open(file_name,'r') #it opens a file and read inside the txt file.
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word #selected word
 

def random_fill_word(word):
    random_fill = random.randint(0, len (word) -1)
    i = 0
    temp = "" 
    while i < len(word): #iterate on each character of the word
        if i == random_fill:
            temp = temp + word[random_fill]
        else:
            temp = temp + '_'
        i = i + 1
    return temp


def is_missing_char(original_word, answer_word, char):
    if char in original_word and char not in answer_word: #char in original_word check if characters are in original word
        return True#if true  it means its missing chars
                 #char not in answer word checks if characters is not in original word
    else:
        return False

def fill_in_char(original_word, answer_word, char):
    for i in range(0, len(answer_word)):
        if char == original_word[i]:
            answer_word = answer_word[:i] + char + answer_word[i + 1:]
    return answer_word  

def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# update to use number of remaining guessesu
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


#:  draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print('/----\n|\n|\n|\n|\n_______')
    elif number_guesses == 3:
        print('/----')
        print('|   0')
        print('|\n'* 3)
    elif number_guesses == 2:
        print('/----')
        print('|   0')
        print('|  / \\')
        print('|\n' * 2)
    elif number_guesses == 1:
        print('/----')
        print('|   0')
        print('|  /|\\')
        print('|   |')
        print('|')
    else:
        print('/----')
        print('|   0')
        print('|  /|\\')
        print('|   |')
        print('|  / \\')
        print('_' * 7)
    
def run_game_loop(word, answer): #main function
    print("Guess the word: "+answer)
    number_of_guesses = 5
    while not word == answer:
        if number_of_guesses == 0:
            print('Sorry, you are out of guesses. The word was: '+ word)
            break
        guess = get_user_input()
        if guess == 'exit' or  guess == 'quit':
            print('Bye!')
            break
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            number_of_guesses = number_of_guesses - 1
            do_wrong_answer(answer, number_of_guesses)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        words_file = "short_words.txt"
    else:
        words_file= sys.argv[1]
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)
