import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox

from database import *

out = widgets.Output()
button = widgets.Button(description='Generate files',disabled=False,button_style='',tooltip='Click me',icon='check')
renting_text = widgets.HTML(value="",placeholder='',description='',)

generation_widget = VBox([button, renting_text, out], layout=Layout(display='flex'))


def on_enter(b):

          renting_text.value = "<h3>Genration Successful</h3>"

button.on_click(on_enter)

