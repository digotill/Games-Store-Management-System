import csv
from datetime import datetime
import os

cur_path = os.path.dirname(__file__)
BASIC_LIMIT = 2
PREMIUM_LIMIT = 7


def load_subscriptions(file_name='Subscriptions.txt'):
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




