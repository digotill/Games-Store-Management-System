import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox

from Subscriptions import *
from database import *

out = widgets.Output()
user_ID_text = widgets.Text(value='', placeholder='e.g. coab', description='User ID:', disabled=False)
time_text = widgets.Dropdown(options=['~PM', '2 PM', '6PM'], description='Pick a Time',disabled=False,)
timer_picker = widgets.DatePicker(description='Pick a Date',disabled=False)
enter_button = widgets.Button(description='Book Time Slot',disabled=False,button_style='',tooltip='Click me',icon='check')
guests_slider = widgets.SelectionSlider(options=['0', '1', '2', '3'],value='0',description='Guests',disabled=False,continuous_update=False,orientation='horizontal',readout=True)
renting_text = widgets.HTML(value="",placeholder='',description='',)

widgets_container1 = HBox([out], layout=Layout(display='flex'))
widgets_container2 = VBox([user_ID_text, time_text, timer_picker, guests_slider, enter_button], layout=Layout(display='flex'))
widgets_container3 = HBox([renting_text], layout=Layout(display='flex'))

Booking_Tab = VBox([widgets_container2, widgets_container3,widgets_container1])


def on_enter(b):
          if not check_subscription(user_ID_text.value):
                    renting_text.value = "<h3>Incorrect User ID</h3>"
          elif time_text.value == '~PM':
                    renting_text.value = "<h3>Choose a Time</h3>"
          elif timer_picker.value is None:
                    renting_text.value = "<h3>Choose a Date</h3>"
          else:
                    make_booking(user_ID_text.value, {'Date': " " +  str(timer_picker.value), 'Time': " " + time_text.value, 'Guests': " " +  guests_slider.value})
                    timer_picker.value = None
                    user_ID_text.value = ""
                    guests_slider.value = "0"
                    renting_text.value = "<br><h3>Booking Confirmed</h3>"



enter_button.on_click(on_enter)

