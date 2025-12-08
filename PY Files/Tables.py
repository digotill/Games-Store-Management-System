import ipywidgets as widgets
from ipywidgets import VBox, Layout, HBox

from Subscriptions import *
from database import *

out = widgets.Output()
text = widgets.HTML(value="",placeholder='',description='',)

widgets_container1 = HBox([out], layout=Layout(display='flex'))
widgets_container2 = HBox([text], layout=Layout(display='flex'))


with out:
          print("{:<20} {:<20} {:<20} {:<20}".format('Customer ID', 'Subscription Type', 'Start Date', 'End Date'))
          for key, value in load_subscriptions().items():
                    customer_id = key
                    subscription_type = value['SubscriptionType']
                    start_date = value['StartDate'].strftime('%d/%m/%Y')
                    end_date = value['EndDate'].strftime('%d/%m/%Y')
                    print("{:<20} {:<20} {:<20} {:<20}".format(customer_id, subscription_type, start_date, end_date))

Subscribers_Tab = VBox([widgets_container2, widgets_container1])
