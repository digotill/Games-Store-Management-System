import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox

from Database import *
from Subscriptions import *

out = widgets.Output(layout={'border': '1px solid black'})
user_ID_text = widgets.Text(value='', placeholder='e.g. coab', description='User ID:', disabled=False)
game_ID_text = widgets.Text(value='', placeholder='e.g. art01', description='Game ID:', disabled=False)
enter_button = widgets.Button(description='Rent Game', disabled=False, button_style='', tooltip='Click me', icon='check')
renting_text = widgets.HTML(value="", placeholder='', description='', )

widgets_container1 = HBox([out], layout=Layout(display='flex'))
widgets_container2 = VBox([user_ID_text, game_ID_text, enter_button], layout=Layout(display='flex'))
widgets_container3 = HBox([renting_text], layout=Layout(display='flex'))

Renting_Tab = VBox([widgets_container2, widgets_container3, widgets_container1])


def on_enter(b):
          message = ""
          if len(user_ID_text.value) != 4 or len(game_ID_text.value) != 5:
                    message += "<h3>Incorrect User ID or Game ID</h3>"
          else:
                    if not check_subscription(user_ID_text.value):
                              message += "<br><h3>User is not subscribed</h3>"
                    else:
                              if check_availability(game_ID_text.value):
                                        message += "<br><h3>Game has been rented</h3>"
                                        rent_game(game_ID_text.value, user_ID_text.value)
                                        user_ID_text.value = ""
                                        game_ID_text.value = ""
                              else:
                                        message += "<br><h3>Game unavailable to rent</h3>"
          renting_text.value = message


enter_button.on_click(on_enter)
