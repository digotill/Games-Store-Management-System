import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox
from setuptools.package_index import user_agent

from database import *
from SubscriptionManager import *



out = widgets.Output(layout={'border': '1px solid black'})
user_ID_text = widgets.Text(value='', placeholder='e.g. coab', description='User ID:', disabled=False)
game_ID_text = widgets.Text(value='',placeholder='e.g. art01',description='Game ID:',disabled=False)
enter_button = widgets.Button(description='Rent Game',disabled=False,button_style='',tooltip='Click me',icon='check')
renting_text = widgets.HTML(value="",placeholder='',description='',)
rent_button = widgets.Button(description='Rent Game',disabled=False,button_style='',tooltip='Click me',icon='check')

widgets_container1 = HBox([out], layout=Layout(display='flex'))
widgets_container2 = HBox([user_ID_text, game_ID_text, enter_button], layout=Layout(display='flex'))
widgets_container3 = HBox([renting_text], layout=Layout(display='flex'))
widgets_container4 = HBox([rent_button], layout=Layout(display='none'))

Renting_Tab = VBox([widgets_container2, widgets_container3, widgets_container4, widgets_container1])

subscriptions = load_subscriptions()
rentals = loadRental()

def on_enter(b):
                                        message = ""
                                        if len(user_ID_text.value) != 4 or len(game_ID_text.value) != 5:
                                                            message += "<h3>Incorrect: User ID must be 4 characters long and Game ID 5 characters long</h3>"
                                                            widgets_container4.layout.display = "none"
                                        else:
                                                            if not check_subscription(user_ID_text.value, subscriptions):
                                                                                message += "<br><h3>User is not subscribed</h3>"
                                                                                widgets_container4.layout.display = "none"
                                                            else:
                                                                                if check_availability(game_ID_text.value):
                                                                                          message += "<br><h3>Game available to rent</h3>"
                                                                                          widgets_container4.layout.display = "flex"
                                                                                else:
                                                                                          message += "<br><h3>Game unavailable to rent</h3>"
                                                                                          widgets_container4.layout.display = "none"
                                        renting_text.value = message

def on_game_rent(b):
          rent_game(game_ID_text.value)
          widgets_container4.layout.display = "none"
          message = "Game Sucessfully Rented"
          renting_text.value = message



rent_button.on_click(on_game_rent)
enter_button.on_click(on_enter)

