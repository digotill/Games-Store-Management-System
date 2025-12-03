import os

cur_path = os.path.dirname(__file__)

def loadGameSearch(gameType):
          Games = {}

          if "digital" in gameType:
                    with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', 'digitalGameInfo.txt'), 'r', encoding='utf-8') as file:
                              reader = csv.reader(file)
                              next(reader)
                              for row in reader:
                                        game_id, title, platform, genre, purchase_date = row
                                        Games[game_id] = {'title': title, 'platform': platform, 'genre': genre, 'purchase_date': purchase_date}
          if "board" in gameType:
                    with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', 'boardGameInfo.txt'), 'r', encoding='utf-8') as file:
                              reader = csv.reader(file)
                              next(reader)
                              for row in reader:
                                        game_id, title, players, genre, purchase_date = row
                                        Games[game_id] = {'title': title, 'players': players, 'genre': genre, 'purchase_date': purchase_date}

          return Games
