import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gmail_service import list_labels

def test_get_labels_map(mock_service):
    """Test that list_labels returns correct list of labels."""
    labels_list = list_labels(mock_service)
    
    work_label = next((label['id'] for label in labels_list if label['name'] == "Work"), None)
    
    assert work_label == "LABEL_1"


