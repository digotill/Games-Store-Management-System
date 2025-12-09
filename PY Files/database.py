import os
import csv
from datetime import datetime
import random
import string
from datetime import datetime, timedelta
from IPython.display import display
cur_path = os.path.dirname(__file__)
now = datetime.now()

def loadGameSearch(gameType):
          Games = {}

          if "digital" in gameType:
                    with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', 'DigitalGames.txt'), 'r', encoding="UTF-8") as file:
                              reader = csv.reader(file)
                              next(reader)
                              for row in reader:
                                        game_id, title, platform, genre, purchase_date = row
                                        Games[game_id] = {'Type': 'Digital', 'Title': title, 'Platform': platform, 'Genre': genre, 'Purchase Date': purchase_date}
          if "board" in gameType:
                    with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', 'BoardGames.txt'), 'r', encoding="UTF-8") as file:
                              reader = csv.reader(file)
                              next(reader)
                              for row in reader:
                                        game_id, title, players, genre, purchase_date = row
                                        Games[game_id] = {'Type': 'Board', 'Title': title, 'Players': players, 'Genre': genre, 'Purchase Date': purchase_date}

          return Games


def loadRental():
          Rentals = {}
          with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', 'Rentals.txt'), 'r', encoding="UTF-16") as file:
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
          rentals[game_id]["Start"] = now.strftime("%Y-%m-%d")
          rentals[game_id]["End"] = " "
          rentals[game_id]["User ID"] = user_id
          write_dict_to(rentals, "Rentals.txt")

def return_game(game_id):
          rentals = loadRental()
          if game_id in rentals and rentals[game_id]["End"].strip() == "":
                    rentals[game_id]["End"] = now.strftime("%Y-%m-%d")
                    write_dict_to(rentals, "Rentals.txt")
                    return True
          return False

def loadGame(gameName):
          all_games = loadGameSearch(["digital", "board"])
          for game_id, game_data in all_games.items():
                    if game_data['Title'] == gameName:
                              return game_id, game_data
          return None

def load_bookings():
          Bookings = {}
          with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', 'Booking.txt'), 'r', encoding="UTF-16") as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                              user_id, date, time, guests= row
                              Bookings[user_id] = {'Date': date, 'Time': time, 'Guests': guests}
          return Bookings

def make_booking(user_id, new_dict):
          rentals = load_bookings()
          rentals[user_id] = new_dict
          write_dict_to(rentals, "Booking.txt")

def g_dates():
    start_bound = datetime(2024, 1, 1)
    end_bound = datetime(2028, 12, 31)

    time_difference_days = (end_bound - start_bound).days
    random_days = random.randrange(time_difference_days)

    start_date = start_bound + timedelta(days=random_days)

    end_date = start_date + timedelta(days=365)

    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')




def g_sub_type():
          if random.random() < 0.5:
                    return "Basic"
          else:
                    return "Premium"

def g_user(length=4):
    characters = string.ascii_lowercase
    return ''.join(random.choice(characters) for _ in range(length))