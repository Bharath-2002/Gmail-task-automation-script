# main.py
from gmail_service import authenticate_gmail, list_messages, get_message, modify_message, list_labels
from database import create_table, save_email, fetch_emails
from rules_engine import load_rules, evaluate_rules
from config import GMAIL_QUERY, MAX_RESULTS
from datetime import datetime

def parse_email(msg):
    headers = msg['payload'].get('headers', [])
    header_dict = {h['name']: h['value'] for h in headers}

    sender = header_dict.get('From', '')
    recipients = header_dict.get('To', '')
    subject = header_dict.get('Subject', '')
    date_received = datetime.fromtimestamp(int(msg['internalDate'])/1000).isoformat()
    snippet = msg.get('snippet', '')

    return {
        'gmail_id': msg['id'],
        'thread_id': msg['threadId'],
        'sender': sender,
        'recipients': recipients,
        'subject': subject,
        'date_received': date_received,
        'snippet': snippet,
        'labels': ','.join(msg.get('labelIds', []))
    }

def main():
    create_table()
    service = authenticate_gmail()
    print("Authenticated successfully.")
    messages = list_messages(service, GMAIL_QUERY, MAX_RESULTS)
    print(f"Found {len(messages)} messages matching the query.")
    for msg_meta in messages:
        msg = get_message(service, msg_meta['id'])
        parsed = parse_email(msg)
        save_email(parsed)
    print("Emails saved to the database.")
    rules = load_rules()
    emails = fetch_emails()
    
    
    labels_list = list_labels(service)
    labels_map = {lbl['name']: lbl['id'] for lbl in labels_list}
    for email in emails:
        actions = evaluate_rules(dict(email), rules)
        if actions:
            add_labels = []
            remove_labels = []
            for action in actions:
                if action == 'mark_read':
                    remove_labels.append('UNREAD')
                elif action == 'mark_unread':
                    add_labels.append('UNREAD')
                elif action.startswith('move_to:'):
                    label_name = action.split(':', 1)[1]
                    if label_name in labels_map:
                        # Label already exists
                        add_labels.append(labels_map[label_name])
                    else:
                        # Create new label
                        label_object = {
                            "name": label_name,
                            "labelListVisibility": "labelShow",
                            "messageListVisibility": "show"
                        }
                        try:
                            label = service.users().labels().create(userId='me', body=label_object).execute()
                            label_id = label['id']
                            labels_map[label_name] = label_id 
                            add_labels.append(label_id)
                        except Exception as e:
                            print(f"Failed to create label '{label_name}':", e)
            modify_message(service, email['gmail_id'], add_labels, remove_labels)
    print("Rules evaluated and actions applied to emails.")
if __name__ == '__main__':
    main()
