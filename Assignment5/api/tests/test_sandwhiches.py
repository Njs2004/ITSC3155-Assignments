import pytest # type: ignore
from unittest.mock import MagicMock
from api.controllers import sandwiches
from api.models import schemas


@pytest.fixture
def mock_db():
    return MagicMock()


def test_create_sandwich(mock_db):
    sandwich_data = schemas.SandwichCreate(sandwich_name="BLT", price=5.99)

    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    result = sandwiches.create(mock_db, sandwich_data)

    assert result.sandwich_name == "BLT"
    assert result.price == 5.99
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()


def test_read_all_sandwiches(mock_db):
    mock_db.query().all.return_value = ["sandwich1", "sandwich2"]
    result = sandwiches.read_all(mock_db)
    assert result == ["sandwich1", "sandwich2"]


def test_read_one_sandwich_found(mock_db):
    sandwich_mock = MagicMock()
    mock_db.query().filter().first.return_value = sandwich_mock
    result = sandwiches.read_one(mock_db, 1)
    assert result == sandwich_mock


def test_read_one_sandwich_not_found(mock_db):
    mock_db.query().filter().first.return_value = None
    with pytest.raises(Exception) as exc:
        sandwiches.read_one(mock_db, 999)
    assert "Sandwich not found" in str(exc.value)


def test_update_sandwich(mock_db):
    mock_query = mock_db.query().filter.return_value
    mock_query.first.return_value = schemas.Sandwich(id=1, sandwich_name="Old", price=3.99)

    updated_data = schemas.SandwichUpdate(price=6.99)
    result = sandwiches.update(mock_db, 1, updated_data)

    mock_query.update.assert_called_once()
    mock_db.commit.assert_called_once()
    assert result == mock_query.first.return_value


def test_delete_sandwich(mock_db):
    mock_query = mock_db.query().filter.return_value
    mock_query.first.return_value = MagicMock()

    result = sandwiches.delete(mock_db, 1)

    mock_query.delete.assert_called_once()
    mock_db.commit.assert_called_once()
    assert result.status_code == 204
