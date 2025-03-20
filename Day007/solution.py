import random
import vidas

word_list = ["adriana", "alexandre", "matheus", "miguel"]

chosen_word = random.choice(word_list)

print(chosen_word)

guessed_letters = []

for letter in chosen_word:
    guessed_letters.append("_")

print (vidas.logo)

print("".join(guessed_letters))

vida = 5

while vida > 0:

    print(vidas.HANGMANPICS[vida])
    print("".join(guessed_letters))

    guess_letter = input("\nAdivinhe uma letra: ").lower()
    if guess_letter in guessed_letters:
        print("Você já escolheu essa letra, tente outra.")
    print(guess_letter)

    index = 0
    acertou = False

    for letter in chosen_word:
        if letter == guess_letter:
            guessed_letters[index]=letter
            acertou = True
        index += 1

    if not acertou:
        vida -= 1

    if "".join(guessed_letters) == chosen_word:
        print("Parabéns, você acertou. A palavra é: " + chosen_word)
        break



if vida == 0:
    print(vidas.HANGMANPICS[vida])
    print("Você foi enforcado.")
