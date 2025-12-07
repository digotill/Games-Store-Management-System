import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox
from database import *
cur_path = os.path.dirname(__file__)


game_text = widgets.Text(value='', placeholder='e.g. minecraft', description='Enter a game:', disabled=False,continuous_update=True)
bg_checkbox = widgets.Checkbox(value=True, description='Include board games', disabled=False, indent=False)
dg_checkbox = widgets.Checkbox(value=True, description='Include digital games', disabled=False, indent=False)
game_buttons = widgets.ToggleButtons(options=[],description='Choose a game:',disabled=False,button_style='', tooltips=[])
game_description = widgets.HTML(value="",placeholder='',description='',)
out = widgets.Output(layout={'border': '1px solid black'})

def on_search(change):
          digitalGameSearch = loadGameSearch(["board" if bg_checkbox.value else None, "digital" if dg_checkbox.value else None])
          options = []
          for game in digitalGameSearch.values():
                    if game_text.value.lower() in game['Title'].lower() or game_text.value == "":
                              options.append(game['Title'])
          game_buttons.options = options
on_search("")


def choose_game(change):
          new_description = ""
          game_id, game_data = loadGame(change['new'])
          for key in game_data.keys():
                    new_description = new_description + "<br>" + key + ": " + game_data[key]
          rentals = loadRental()
          if rentals[game_id]["End"] == " ":
                    new_description = new_description + "<br>" + "Availability" + ": " + "True"
          else:
                    new_description = new_description + "<br>" + "Availability" + ": " + "False"
          game_description.value = new_description

game_buttons.observe(choose_game, names='value')
bg_checkbox.observe(on_search, names='value')
dg_checkbox.observe(on_search, names='value')
game_text.observe(on_search, names='value')

widgets_container1 = HBox([game_text, bg_checkbox, dg_checkbox], layout=Layout(display='flex'))
widgets_container2 = HBox([game_buttons], layout=Layout(display='flex'))
widgets_container3 = HBox([game_description], layout=Layout(display='flex'))
widgets_container4 = HBox([out], layout=Layout(display='flex'))

Search_Tab = VBox([widgets_container1, widgets_container2, widgets_container3, widgets_container4])

