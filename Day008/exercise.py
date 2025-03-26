def life_in_weeks(age, name):
    weeks_left=(90-age)*52
    print(f"{name}, you have {weeks_left} weeks left.")


life_in_weeks(name="Adriana",age=41)


def calculate_love_score(name1, name2):
    quantity_letters_true=0
    quantity_letters_love=0

    for letter_true in "true":

        for letter_name1 in name1:
            if letter_true == letter_name1:quantity_letters_true += 1

        for letter_name2 in name2:
            if letter_true == letter_name2:quantity_letters_true += 1

    for letter_love in "love":

        for letter_name1 in name1:
            if letter_love == letter_name1: quantity_letters_love += 1

        for letter_name2 in name2:
            if letter_love == letter_name2: quantity_letters_love += 1

    print(f"{quantity_letters_true}{quantity_letters_love}")

calculate_love_score("matheus","brasilia")