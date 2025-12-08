import os
import csv
from database import *
cur_path = os.path.dirname(__file__)


def load_feedback(file_name='Feedback.txt'):
          feedback_list = {}
          with open(os.path.abspath(os.path.join(cur_path, os.pardir)) + '\\' + 'TXT Files' + '\\' + file_name, 'r', encoding="UTF-16") as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                              comment_id, game_id, rating, comments = row
                              feedback_list[comment_id] = {'GameID': game_id, 'Rating': int(rating), 'Comments': comments}
                    return feedback_list

def add_feedback(new_dict):
          feedback_list = load_feedback()
          key1 = int(sorted(feedback_list.keys())[-1]) + 1
          feedback_list[key1] = new_dict
          write_dict_to(feedback_list, "Feedback.txt")