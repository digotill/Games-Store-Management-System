import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox

from Subscriptions import *

users_text = widgets.Text(value='', placeholder='e.g. tygh', description='Enter a User:', disabled=False, continuous_update=True)
basic_checkbox = widgets.Checkbox(value=True, description='Include Basic subscriptions', disabled=False, indent=False)
premium_checkbox = widgets.Checkbox(value=True, description='Include Premium subscriptions', disabled=False, indent=False)
user_buttons = widgets.ToggleButtons(options=[], description='Choose a User:', disabled=False, button_style='', tooltips=[])
user_description = widgets.HTML(value="", placeholder='', description='', )
out = widgets.Output()

widgets_container1 = HBox([users_text, basic_checkbox, premium_checkbox], layout=Layout(display='flex'))
widgets_container3 = HBox([user_buttons], layout=Layout(display='flex'))
widgets_container2 = VBox([user_description, out], layout=Layout(display='flex'))

Subscribers_Tab = VBox([widgets_container1, widgets_container3,  widgets_container2])

def on_search(change):
          Users = load_subscriptions()
          options = []
          search_term = users_text.value.lower()
          for primary_key, inner_dict in Users.items():
                    if search_term in primary_key.lower() or search_term == "":
                              sub_type = inner_dict["SubscriptionType"]
                              is_basic = (sub_type == " Basic" and basic_checkbox.value == True)
                              is_premium = (sub_type == " Premium" and premium_checkbox.value == True)
                              if is_basic or is_premium:
                                        options.append(primary_key)
          options = sorted(options)
          user_buttons.options = options
on_search("")

def choose_user(change):
          Users = load_subscriptions()
          new_description = ""
          inner_dict = Users[change['new']]
          new_description += "<br> User ID: " + change['new']
          for key1 in inner_dict.keys():
                    new_description += "<br>" + key1 + ": " + inner_dict[key1]
          user_description.value = new_description

user_buttons.observe(choose_user, names='value')
users_text.observe(on_search, names='value')
basic_checkbox.observe(on_search, names='value')
premium_checkbox.observe(on_search, names='value')
