import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox

from Feedback import *

out = widgets.Output()
comment_text = widgets.HTML(value="<h3>Below shows the top 5 games that were rented the longest ago </h3><h3>Select any 5 of the Games to be Pruned</h3>", placeholder='', description='', )

checkboxes = [widgets.Checkbox(value=False, description='', disabled=False, indent=False) for i in range(5)]

enter_button = widgets.Button(description='Prune Games', disabled=False, button_style='', tooltip='Click me', icon='check')
renting_text = widgets.HTML(value="", placeholder='', description='', )

widgets_container1 = HBox([out], layout=Layout(display='flex'))
widgets_container4 = VBox(checkboxes, layout=Layout(display='flex'))
widgets_container2 = VBox([comment_text], layout=Layout(display='flex'))
widgets_container5 = VBox([enter_button], layout=Layout(display='flex'))
widgets_container3 = HBox([renting_text], layout=Layout(display='flex'))

Pruning_Tab = VBox([widgets_container2, widgets_container4, widgets_container5, widgets_container3, widgets_container1])


def eval_games():
          rentals = loadRental()
          top = earliest_returns(rentals, 5)
          games = loadGameSearch(["digital", "board"])
          count = 0
          for box in checkboxes:
                    box.value = False
                    box.description = games[top[count][0]]["Title"]
                    count += 1
eval_games()


def on_enter(b):
          digitals = loadGameSearch(["digital"], False)
          board = loadGameSearch(["board"], False)
          rentals = loadRental()
          for box in checkboxes:
                    if box.value:
                              renting_text.value = "<h3>Games succesfully Pruned</h3>"
                              for key, value in digitals.copy().items():
                                        if box.description == value["Title"]:
                                                  del digitals[key]
                                                  del rentals[key]
                                                  write_dict_to(rentals, "Rentals.txt")
                              for key, value in board.copy().items():
                                        if box.description == value["Title"]:
                                                  del board[key]
                                                  del rentals[key]
          write_dict_to(digitals, "DigitalGames.txt")
          write_dict_to(board, "BoardGames.txt")
          write_dict_to(rentals, "Rentals.txt")
          eval_games()


enter_button.on_click(on_enter)
