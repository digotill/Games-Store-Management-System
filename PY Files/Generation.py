import ipywidgets as widgets
from ipywidgets import VBox, Layout

from Database import *
from Subscriptions import *

out = widgets.Output()
button = widgets.Button(description='Generate files', disabled=False, button_style='', tooltip='Click me', icon='check')
sub_text = widgets.Text(value='100', placeholder='', description='Ne Subs', disabled=False)
book_text = widgets.Text(value='50', placeholder='e.g. coab', description='N Bookings', disabled=False)
rent_text = widgets.Text(value='0.5', placeholder='e.g. coab', description='Rental Chance', disabled=False)
renting_text = widgets.HTML(value="", placeholder='', description='')

generation_widget = VBox([sub_text, book_text, rent_text, button, renting_text, out], layout=Layout(display='flex'))


def g_subscriptions(n_subs):
          subscriptions = {}
          for i in range(n_subs):
                    start_date, end_date = g_dates()
                    subscriptions[g_user()] = {'SubscriptionType': " " + g_sub_type(), 'StartDate': " " + start_date, 'EndDate': " " + end_date}
          write_dict_to(subscriptions, "Subscriptions.txt")


def g_bookings(n_bookings):
          bookings = {}
          for i in range(n_bookings):
                    user_id = random.choice(list(load_subscriptions().keys()))
                    bookings[user_id] = {'Date': " " + g_dates()[0], 'Time': " " + g_time(), 'Guests': " " + g_guests()}
          write_dict_to(bookings, "Booking.txt")


def g_rentals(rental_chance):
          Games = loadGameSearch(["digital", "board"])
          new_dict = {}
          for key in Games.keys():
                    user_id = random.choice(list(load_subscriptions().keys()))
                    dates = g_dates()
                    date2 = dates[1] if random.random() < rental_chance else " "
                    new_dict[key] = {"Start": " " + dates[0], "End": " " + date2, "UserID": " " + user_id}
          write_dict_to(new_dict, "Rentals.txt")


def on_enter(b):
          g_subscriptions(int(sub_text.value))
          g_bookings(int(book_text.value))
          g_rentals(float(rent_text.value))
          renting_text.value = "<h3>Genration Successful</h3>"


button.on_click(on_enter)
