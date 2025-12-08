import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox

from database import *

out = widgets.Output(layout={'border': '1px solid black'})
game_ID_text = widgets.Text(value='',placeholder='e.g. art01',description='Game ID:',disabled=False)
enter_button = widgets.Button(description='Return Game',disabled=False,button_style='',tooltip='Click me',icon='check')
renting_text = widgets.HTML(value="",placeholder='',description='',)

widgets_container1 = HBox([out], layout=Layout(display='flex'))
widgets_container2 = HBox([game_ID_text, enter_button], layout=Layout(display='flex'))
widgets_container3 = HBox([renting_text], layout=Layout(display='flex'))


Returning_Tab = VBox([widgets_container2, widgets_container3, widgets_container1])


def on_enter(b):
          message = ""
          if return_game(game_ID_text.value):
                    message += "<h3>Game succesfully returned</h3>"
          else:
                    message += "<h3>The Game ID is incorrect or cannot be returned</h3>"
          renting_text.value = message

enter_button.on_click(on_enter)