import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gmail_service import modify_message 

def test_modify_message(mock_service):
    """Test modifying a message."""
    modify_message(mock_service, "MSG_123", add_labels=["LABEL_1"], remove_labels=["UNREAD"])

    mock_service.users().messages().modify.assert_called_once()
    args, kwargs = mock_service.users().messages().modify.call_args
    assert kwargs["body"]["addLabelIds"] == ["LABEL_1"]
    assert kwargs["body"]["removeLabelIds"] == ["UNREAD"]
