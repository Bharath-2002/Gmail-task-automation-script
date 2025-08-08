import json
import sys
import os
import tempfile
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rules_engine import load_rules
import rules_engine

def test_load_rules():
    """Test loading rules.json."""
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    rules_data = [
        {"conditions": {"from": "test@example.com"}, "actions": ["mark_read"]}
    ]
    with open(temp_file.name, 'w') as f:
        json.dump(rules_data, f)

    # Patch RULES_FILE so load_rules uses our temp file
    rules_engine.RULES_FILE = temp_file.name
    loaded_rules = load_rules()
    assert loaded_rules == rules_data