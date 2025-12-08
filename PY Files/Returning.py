import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox

from database import *
from Feedback import *

out = widgets.Output(layout={'border': '1px solid black'})
game_ID_text = widgets.Text(value='',placeholder='e.g. art01',description='Game ID:',disabled=False)
comment_text = widgets.Text(value='',placeholder='e.g. Pretty Good',description='Comment:',disabled=False)
enter_button = widgets.Button(description='Return Game',disabled=False,button_style='',tooltip='Click me',icon='check')
renting_text = widgets.HTML(value="",placeholder='',description='',)
star_slider = widgets.SelectionSlider(options=['0', '1', '2', '3', '4', '5'],value='0',description='Rating',disabled=False,continuous_update=False,orientation='horizontal',readout=True)

widgets_container1 = HBox([out], layout=Layout(display='flex'))
widgets_container2 = VBox([game_ID_text, comment_text, star_slider, enter_button], layout=Layout(display='flex'))
widgets_container3 = HBox([renting_text], layout=Layout(display='flex'))


Returning_Tab = VBox([widgets_container2, widgets_container3, widgets_container1])


def on_enter(b):
          message = ""
          if return_game(game_ID_text.value):
                    message += "<h3>Game succesfully returned and Feedback added</h3>"
                    add_feedback({'GameID': " " +   game_ID_text.value, 'Rating': " " +   star_slider.value, 'Comments': " " +   comment_text.value})
          else:
                    message += "<h3>The Game ID is incorrect or cannot be returned</h3>"
          renting_text.value = message

enter_button.on_click(on_enter)