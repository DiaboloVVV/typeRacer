import time
import os
import json
from re import findall
from datetime import date
from random import randint, randrange


def leaderboards_after_game(time_score, wpm):
    how_long = time.time() - time_score
    data = {'leaderboards': []}
    data['leaderboards'].append({
        'howLong': round(how_long),
        'wpm': wpm,
        'date': date.today().strftime("%d/%m/%Y")
    })
    with open('leaderboards.txt', 'a') as file:
        json.dump(data, file)


def calculate_wpm(started_time, amount_of_words):
    how_long = time.time() - started_time
    if how_long < 60:
        wpm = (amount_of_words/how_long)*60
    else:
        wpm = amount_of_words/(how_long/60)
    return round(wpm)


def timer(t=5):
    while t:
        print(str(t), end="\r")
        time.sleep(1)
        t -= 1
    print("START", end="\r")


def reading_file():
    start_time = time.time()
    amount_of_words = 0
    # reading text and clearing the text
    clean_lines = []
    with open('dataPolish.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        clean_lines.append(line.strip())
    clean_lines = list(filter(None, clean_lines))
    # picking random lines from the text
    random_paragraph = randrange(0, len(clean_lines))
    random_amount = randint(3, 7)
    final_lines = clean_lines[random_paragraph:random_paragraph+random_amount]
    for elem in final_lines:
        print(elem)
        amount_of_words += len(findall(r'\w+', elem))
    print(amount_of_words)
    timer()
    return start_time, amount_of_words


def main():
    start_time = time.time()
    os.system('color 0a')

    reading_file_timer, amount_of_words = reading_file()
    print(f"You had: {calculate_wpm(reading_file_timer,amount_of_words)} words per minute")
    leaderboards_after_game(reading_file_timer, calculate_wpm(reading_file_timer, amount_of_words))

    print(f"\nProgram took: {time.time()-start_time}s")
    os.system('color 07')


if __name__ == '__main__':
    main()
