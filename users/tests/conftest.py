import pytest

from .factories.users import UserFactory

@pytest.fixture
def user():
    return UserFactory()