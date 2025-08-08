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

The `rules.json` file contains your automation rules.
Each rule has **conditions** and **actions**.

### Example:

```json
[
    {
        "conditions": {
            "from": "newsletter@example.com"
        },
        "actions": [
            "mark_read",
            "apply_label:Work"
        ]
    },
    {
        "conditions": {
            "subject": "Invoice"
        },
        "actions": [
            "apply_label:Finance"
        ]
    }
]
```

### Available Conditions:

* `"from"` → Match sender email.
* `"subject"` → Match subject text.
* `"contains"` → Match keyword in email body.

### Available Actions:

* `"mark_read"` → Marks email as read.
* `"mark_unread"` → Marks email as unread.
* `"apply_label:<LabelName>"` → Applies a Gmail label to the email.
* `"remove_label:<LabelName>"` → Removes a Gmail label.

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
