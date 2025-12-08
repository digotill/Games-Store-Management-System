import os
import csv
cur_path = os.path.dirname(__file__)


def load_feedback(file_name='Game_Feedback.txt'):
          feedback_list = []
          with open(os.path.abspath(os.path.join(cur_path, os.pardir)) + '\\' + 'TXT Files' + '\\' + file_name, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                              game_id, rating, comments = row
                              feedback_list.append({'GameID': game_id, 'Rating': int(rating), 'Comments': comments})
                    return feedback_list


def add_feedback(game_id, rating, comments, file_name='Game_Feedback.txt'):
          with open(file_name, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([game_id, rating, comments])
