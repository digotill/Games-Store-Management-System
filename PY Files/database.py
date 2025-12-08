import os
import csv
from datetime import datetime
cur_path = os.path.dirname(__file__)
now = datetime.now()

def loadGameSearch(gameType):
          Games = {}

          if "digital" in gameType:
                    with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', 'digitalGameInfo.txt'), 'r', encoding="UTF-16") as file:
                              reader = csv.reader(file)
                              next(reader)
                              for row in reader:
                                        game_id, title, platform, genre, purchase_date = row
                                        Games[game_id] = {'Type': 'digital', 'Title': title, 'Platform': platform, 'Genre': genre, 'Purchase Date': purchase_date}
          if "board" in gameType:
                    with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', 'boardGameInfo.txt'), 'r', encoding="UTF-16") as file:
                              reader = csv.reader(file)
                              next(reader)
                              for row in reader:
                                        game_id, title, players, genre, purchase_date = row
                                        Games[game_id] = {'Type': 'board', 'Title': title, 'Players': players, 'Genre': genre, 'Purchase Date': purchase_date}

          return Games

def loadRental():
          Rentals = {}
          with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', 'Rental.txt'), 'r', encoding="UTF-16") as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                              game_id, start, end, user_id  = row
                              Rentals[game_id] = {'Start': start, 'End': end, 'User ID': user_id}
          return Rentals

def write_dict_to(new_dict, filename):
          with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', filename), 'w', newline='', encoding="UTF-16") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([])
                    for primary_key, inner_dict in new_dict.items():
                              row = [primary_key]
                              row.extend(inner_dict.values())
                              writer.writerow(row)

def check_availability(game_id):
          rentals = loadRental()
          if rentals[game_id]["End"] != " ":
                    return True
          else:
                    return False

def rent_game(game_id, user_id):
          rentals = loadRental()
          print(rentals)
          rentals[game_id]["Start"] = now.strftime("%Y-%m-%d")
          rentals[game_id]["End"] = " "
          rentals[game_id]["User ID"] = user_id
          write_dict_to(rentals, "Rental.txt")

def return_game(game_id):
          rentals = loadRental()
          if game_id in rentals and rentals[game_id]["End"].strip() == "":
                              rentals[game_id]["End"] = now.strftime("%Y-%m-%d")
                              write_dict_to(rentals, "Rental.txt")

return_game("pkm07")

def loadGame(gameName):
          all_games = loadGameSearch(["digital", "board"])
          for game_id, game_data in all_games.items():
                    if game_data['Title'] == gameName:
                              return game_id, game_data
          return None


def error():
          with out:
                    try:
                              pass
                    except Exception as e:
                              print(f"An unexpected error occurred: {type(e).__name__}")

