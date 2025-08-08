# Gmail-task-automation-script
Python script using Gmail API, SQLite, and JSON-defined rules to fetch, store, and process emails with automated actions.
This project automates Gmail actions like modifying messages, listing labels, and applying custom rules based on conditions you define in `rules.json`.

## 🚀 Features
- Authenticate with Gmail API using OAuth 2.0
- List and fetch Gmail labels
- Apply rules to incoming emails automatically
- Easily customizable rules in `rules.json`


# Project Setup

## 1️⃣ Clone the repository

clone the repository , usig git clone command

## 2️⃣ Create a Python virtual environment (recommended)

python -m venv venv

Activate it:

  source venv/bin/activate

## 3️⃣ Install dependencies

pip install -r requirements.txt

---

## 🔑 How to Create OAuth 2.0 Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. **Create a project**:
   * Click the project dropdown → "New Project" → give it a name → "Create".
   * 
3. **Enable Gmail API**:
   * In the search bar, search for "Gmail API".
   * Click on "Gmail API" → "Enable".
   * 
4. **Create OAuth consent screen**:
   * Go to **APIs & Services → OAuth consent screen**.
   * Choose **External** (if personal) or **Internal** (if using within an organization).
   * Fill in required fields → Save.
   * if external , add your mail id in test users
     
5. **Create OAuth credentials**:
   * Go to **APIs & Services → Credentials**.
   * Click **Create Credentials → OAuth client ID**.
   * Application type: **Desktop app**.
   * Name it → Create.
     
6. **Download credentials**:
   * Click the download icon next to your OAuth client.
   * Save the file as `credentials.json` in the project folder.

---

## ▶️ Running the Script

Once you have your `credentials.json` file and have installed dependencies:



* On first run,python token_creation_script.py , a browser window will open asking you to log into your Google account and grant permissions.
* A `token.json` file will be created for future authentication (you won’t have to log in every time).
  
```bash
python main.py
```
---


## ⚙️ Adjusting `rules.json`

The `rules.json` file defines how incoming emails should be filtered and what actions should be taken.

---

### 📂 **Example:**
````markdown
```json
[
  {
    "predicate": "any",
    "conditions": [
      { "field": "From", "predicate": "contains", "value": "donotreply@angelbroking.com" },
      { "field": "From", "predicate": "contains", "value": "contract.notes@angeltrade.in" }
    ],
    "actions": ["mark_read", "move_to:angelone"]
  },
  {
    "predicate": "any",
    "conditions": [
      { "field": "From", "predicate": "contains", "value": "noreply@dare2compete.news" },
      { "field": "Message", "predicate": "contains", "value": "Important" }
    ],
    "actions": ["mark_read", "move_to:test2"]
  }
]
````

---

### 🔍 **Rule Structure**

Each rule contains:

| Key          | Description                                                                                                                                                                                                                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `predicate`  | Defines how multiple conditions are evaluated. Possible values:<br>• `"any"` → Match if **any** condition is true.<br>• `"all"` → Match if **all** conditions are true.                                                                                                                                                        |
| `conditions` | A list of individual conditions to check. Each condition has: <br>• `field` → Which email attribute to check (`From`, `To`, `Subject`, `Message`, `DateReceived`).<br>• `predicate` → How to compare the field (e.g., `contains`, `equals`, `less_than_days`, `greater_than_days`).<br>• `value` → The value to match against. |
| `actions`    | A list of actions to apply when the rule matches.                                                                                                                                                                                                                                                                              |

---

### 📝 **Available Fields for `conditions`**

| Field          | Example Value                                      | Description               |
| -------------- | -------------------------------------------------- | ------------------------- |
| `From`         | `"donotreply@example.com"`                         | Sender email address.     |
| `To`           | `"myemail@example.com"`                            | Recipient email address.  |
| `Subject`      | `"Invoice"`                                        | Email subject.            |
| `Message`      | `"urgent"`                                         | Email body text.          |
| `DateReceived` | `"less_than_days": 7` or `"greater_than_days": 30` | Age of the email in days. |

---

### 🔍 **Predicates for Conditions**

| Predicate           | Example                            | Description                                                            |
| ------------------- | ---------------------------------- | ---------------------------------------------------------------------- |
| `contains`          | `"predicate": "contains"`          | True if field contains the value (case-insensitive).                   |
| `equals`            | `"predicate": "equals"`            | True if field exactly matches the value.                               |
| `less_than_days`    | `"predicate": "less_than_days"`    | True if the email was received within the given number of days.        |
| `greater_than_days` | `"predicate": "greater_than_days"` | True if the email was received more than the given number of days ago. |

---

### 🎯 **Available Actions**

| Action                 | Example                  | Description                             |
| ---------------------- | ------------------------ | --------------------------------------- |
| `mark_read`            | `"mark_read"`            | Marks email as read.                    |
| `mark_unread`          | `"mark_unread"`          | Marks email as unread.                  |
| `move_to:<Label>`      | `"move_to:Work"`         | Moves email to the given Gmail label.   |
| `apply_label:<Label>`  | `"apply_label:Finance"`  | Adds the given label to the email.      |
| `remove_label:<Label>` | `"remove_label:Finance"` | Removes the given label from the email. |

---



## 🧪 Running Tests

We use **pytest** for testing.

```bash
pytest
```

---

## 📌 Notes

* Do **not** share `credentials.json` or `token.json` publicly.
* You can update `rules.json` anytime — the script will apply the latest rules when run again.
* Make sure you have labels created in Gmail before applying them in rules.

---

```
