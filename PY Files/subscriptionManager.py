# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: subscriptionManager.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-10-28 09:45:22 UTC (1761644722)

import os

cur_path = os.path.dirname(__file__)

"""
subscriptionManager.py

This module provides functionalities to manage customer subscriptions for a video game rental system.
It includes functions to load subscription information from a text file, to check the status of a customer's subscription,
and to get the rental limit based on the subscription type.

Functions:
    - load_subscriptions(file_name: str) -> dict
        Load subscription information from a text file into a dictionary.

    - check_subscription(customer_id: str, subscriptions: dict) -> bool
        Check if a customer's subscription is active based on the current date.

    - get_rental_limit(subscription_type: str) -> int
        Get the rental limit based on the subscription type.
"""
import csv
from datetime import datetime

BASIC_LIMIT = 2
PREMIUM_LIMIT = 7


def load_subscriptions(file_name='Subscription_Info.txt'):
          """
          Load subscription information from a text file into a dictionary.

          Parameters:
              file_name (str): The name of the text file containing subscription information.

          Returns:
              dict: A dictionary containing customer IDs as keys and their subscription details as values.
          """
          subscriptions = {}
          with open(os.path.abspath(os.path.join(cur_path, os.pardir)) + '\\' + 'TXT Files' + '\\' + file_name, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                              customer_id, subscription_type, start_date, end_date = row
                              subscriptions[customer_id] = {'SubscriptionType': subscription_type,
                                                            'StartDate': datetime.strptime(start_date, '%Y-%m-%d'),
                                                            'EndDate': datetime.strptime(end_date, '%Y-%m-%d')}
                    return subscriptions


def check_subscription(customer_id, subscriptions):
          """
          Check if a customer's subscription is active based on the current date.

          Parameters:
              customer_id (str): The ID of the customer.
              subscriptions (dict): A dictionary containing subscription information.

          Returns:
              bool: True if the subscription is active, False otherwise.
          """
          current_date = datetime.now()
          if customer_id in subscriptions:
                    start_date = subscriptions[customer_id]['StartDate']
                    end_date = subscriptions[customer_id]['EndDate']
                    return start_date <= current_date <= end_date
          return False


def get_rental_limit(subscription_type):
          """
          Get the rental limit based on the subscription type.

          Parameters:
              subscription_type (str): The type of the subscription ("Basic" or "Premium").

          Returns:
              int: The rental limit for the given subscription type.
          """
          if subscription_type == 'Basic':
                    return BASIC_LIMIT
          if subscription_type == 'Premium':
                    return PREMIUM_LIMIT
          return 0


if __name__ == '__main__':
          subscriptions = load_subscriptions()
          print(check_subscription('coai', subscriptions))
          print(get_rental_limit('Basic'))
          print(get_rental_limit('Premium'))
