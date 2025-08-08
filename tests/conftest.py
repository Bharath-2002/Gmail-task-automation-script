import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_service():
    """Mock Gmail API service object."""
    service = MagicMock()
    service.users().labels().list().execute.return_value = {
        "labels": [
            {"id": "LABEL_1", "name": "Work"},
            {"id": "LABEL_2", "name": "Personal"}
        ]
    }
    return service
