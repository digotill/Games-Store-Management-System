import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox
from psutil import users
from setuptools.package_index import user_agent

from database import *
from Subscriptions import *


users_text = widgets.Text(value='', placeholder='e.g. minecraft', description='Enter a game:', disabled=False, continuous_update=True)
user_buttons = widgets.ToggleButtons(options=[], description='Choose a game:', disabled=False, button_style='', tooltips=[])
user_description = widgets.HTML(value="", placeholder='', description='', )
out = widgets.Output(layout={'border': '1px solid black'})

Search_Tab = VBox([users_text, user_buttons, user_description, out], layout=Layout(display='flex'))

def on_search(change):
          Users = load_subscriptions()
          options = []
          for game in Users.values():
                    if users_text.value.lower() in game['Title'].lower() or users_text.value == "":
                              options.append(game['Title'])
          user_buttons.options = options
on_search("")

rentals = loadRental()

def choose_game(change):
          new_description = ""
          game_id, game_data = loadGame(change['new'])
          new_description += "<br> Game ID: " + game_id
          for key in game_data.keys():
                    new_description += "<br>" + key + ": " + game_data[key]
          if check_availability(game_id):
                    new_description += "<br>" + "Availability" + ": " + "True"
          else:
                    new_description = new_description + "<br>" + "Availability" + ": " + "False"
          user_description.value = new_description

user_buttons.observe(choose_game, names='value')
users_text.observe(on_search, names='value')

for key, value in load_subscriptions().items():
          customer_id = key
          subscription_type = value['SubscriptionType']
          start_date = value['StartDate'].strftime('%d/%m/%Y')
          end_date = value['EndDate'].strftime('%d/%m/%Y')