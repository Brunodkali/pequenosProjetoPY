import string
import random
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letras na palavra
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #letras que você usou
    print("Lembrete: Todas as palavras dessa forca estão em inglês. Divirta-se!")
    lives = 15

    while len(word_letters) > 0 and lives > 0:
        #letras usadas
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("Você possui", lives, "vidas e já usou essas letras:", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Palavra atual: ", " ".join(word_list))

        user_letter = input("Escolha a letra: ").upper()
        if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                
                else:
                    lives = lives -1 #diminui as vidas
                    print("Letra incorreta.")

        elif user_letter in used_letters:
            print("Escolha outra letra.")
        
        else:
            print("Letra inválida.")

    if lives == 0:
        print("Você perdeu! A palavra era", word)
    else:
        print("Parabéns grande guerreiro, você acertou a palavra", word)

hangman()
