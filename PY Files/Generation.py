import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox


from database import *

out = widgets.Output()
button = widgets.Button(description='Generate files',disabled=False,button_style='',tooltip='Click me',icon='check')
renting_text = widgets.HTML(value="",placeholder='',description='',)

generation_widget = VBox([button, renting_text, out], layout=Layout(display='flex'))

def g_subscriptions(n_subs):
          subscriptions = {}
          for i in range(n_subs):
                    start_date, end_date = g_dates()
                    subscriptions[g_user()] = {'SubscriptionType': " " + g_sub_type(),'StartDate': " " +  start_date,'EndDate': " " +  end_date}
          write_dict_to(subscriptions, "Subscriptions.txt")

def g_bookings(n_bookings):
          pass

def g_rentals():
          pass

def g_games():
          pass

def on_enter(b):
          renting_text.value = "<h3>Genration Successful</h3>"

button.on_click(on_enter)
