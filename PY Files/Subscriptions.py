# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Subscriptions.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-10-28 09:45:22 UTC (1761644722)

"""
Subscriptions.py

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
import os

cur_path = os.path.dirname(__file__)
BASIC_LIMIT = 2
PREMIUM_LIMIT = 7


def load_subscriptions(file_name='Subscription_Info.txt'):
          subscriptions = {}
          with open(os.path.join(os.path.abspath(os.path.join(cur_path, os.pardir)), 'TXT Files', file_name), 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                              customer_id, subscription_type, start_date, end_date = row
                              subscriptions[customer_id] = {'SubscriptionType': subscription_type,
                                                            'StartDate': datetime.strptime(start_date, '%Y-%m-%d'),
                                                            'EndDate': datetime.strptime(end_date, '%Y-%m-%d')}
                    return subscriptions


def check_subscription(customer_id):
          subscriptions = load_subscriptions()
          current_date = datetime.now()
          if customer_id in subscriptions:
                    start_date = subscriptions[customer_id]['StartDate']
                    end_date = subscriptions[customer_id]['EndDate']
                    return start_date <= current_date <= end_date
          return False

def get_rental_limit(subscription_type):
          if subscription_type == 'Basic':
                    return BASIC_LIMIT
          if subscription_type == 'Premium':
                    return PREMIUM_LIMIT
          return 0


if __name__ == '__main__':
          subscriptions = load_subscriptions()


