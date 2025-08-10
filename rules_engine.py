# rules_engine.py
import json
from datetime import datetime, timedelta
from config import RULES_FILE
from dateutil.relativedelta import relativedelta

def load_rules():
    with open(RULES_FILE) as f:
        return json.load(f)

def match_condition(email, condition):
    field = condition['field'].lower()
    predicate = condition['predicate']
    value = condition['value']

    if field == 'from':
        data = email['sender']
    elif field == 'subject':
        data = email['subject']
    elif field == 'message':
        data = email['snippet']
    elif field == 'datereceived':
        date_received = datetime.fromisoformat(email['date_received'])
        if predicate == 'less_than_days':
            threshold = datetime.now() - timedelta(days=int(value))
            return date_received < threshold
        elif predicate == 'greater_than_days':
            threshold = datetime.now() - timedelta(days=int(value))
            return date_received > threshold
        elif predicate == 'less_than_months':
            threshold = datetime.now() - relativedelta(months=int(value))
            return date_received < threshold
        elif predicate == 'greater_than_months':
            threshold = datetime.now() - relativedelta(months=int(value))
            return date_received > threshold
        return False
    else:
        return False

    if predicate == 'contains':
        return value in data
    elif predicate == 'does_not_contain':
        return value not in data
    elif predicate == 'equals':
        return data == value
    elif predicate == 'not_equals':
        return data != value
    return False

def evaluate_rules(email, rules):
    matched_actions = []
    for rule in rules:
        predicate = rule['predicate']
        conditions = rule['conditions']
        if predicate == 'all':
            result = all(match_condition(email, c) for c in conditions)
        else:
            result = any(match_condition(email, c) for c in conditions)

        if result:
            matched_actions.extend(rule['actions'])
    return matched_actions
