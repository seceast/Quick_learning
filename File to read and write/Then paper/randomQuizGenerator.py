# -*- coding: utf-8 -*-
# @author: yangyd
# @file: randomQuizGenerator.py
# @time: 2020/5/25 22:51


import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiz_num in range(35):
    quiz_file = open(f'capitals{quiz_num+1}.txt', 'w')
    answer_key_file = open(f'capitals_answer{quiz_num+1}.txt', 'w')

    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' '*20) + f'State Capitals Quiz{quiz_num+1}')
    quiz_file.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for question_num in range(50):
        correct_answer = capitals[states[question_num]]
        wrong_answer = list(capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer = random.sample(wrong_answer, 3)

        answer = wrong_answer + [correct_answer]
        random.shuffle(answer)

        quiz_file.write('%s. What is the capital of %s?\n' % (question_num + 1, states[question_num]))
        for i in range(4):
            quiz_file.write(' %s. %s\n' % ('ABCD'[i], answer[i]))
        quiz_file.write('\n')
        # Write the answer key to a file.
        answer_key_file.write('%s. %s\n' % (question_num + 1, 'ABCD'[
            answer.index(correct_answer)]))
    quiz_file.close()
    answer_key_file.close()
