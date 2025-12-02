# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: feedbackManager.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-10-28 09:45:20 UTC (1761644720)
import os

cur_path = os.path.dirname(__file__)

"""
feedbackManager.py

This module provides functionalities to manage game feedback for a video game rental system.
It includes functions to load feedback information from a text file and to add new feedback records.

Functions:
    - load_feedback(file_name: str) -> list
        Load feedback information from a text file into a list of dictionaries.

    - add_feedback(game_id: str, rating: int, comments: str, file_name: str)
        Add a new feedback record to the text file.
"""
import csv


def load_feedback(file_name='Game_Feedback.txt'):
          """
          Load feedback information from a text file into a list of dictionaries.

          Parameters:
              file_name (str): The name of the text file containing feedback information.

          Returns:
              list: A list of dictionaries containing game IDs, ratings, and comments.
          """
          feedback_list = []
          with open(os.path.abspath(os.path.join(cur_path, os.pardir)) + '\\' + 'TXT Files' + '\\' + file_name, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                              game_id, rating, comments = row
                              feedback_list.append({'GameID': game_id, 'Rating': int(rating), 'Comments': comments})
                    return feedback_list


def add_feedback(game_id, rating, comments, file_name='Game_Feedback.txt'):
          """
          Add a new feedback record to the text file.

          Parameters:
              game_id (str): The ID of the game.
              rating (int): The rating given to the game.
              comments (str): Any comments about the game.
              file_name (str): The name of the text file to which the feedback will be added.
          """
          with open(file_name, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([game_id, rating, comments])


if __name__ == '__main__':
          feedback_list = load_feedback()
          print(feedback_list)
          add_feedback('fifa02', 5, 'Absolutely amazing!', 'Game_Feedback.txt')
