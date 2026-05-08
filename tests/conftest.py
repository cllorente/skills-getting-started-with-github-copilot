import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities as app_activities, app, activities as activities_state


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(autouse=True)
def reset_activities():
    original = copy.deepcopy(app_activities)
    yield
    activities_state.clear()
    activities_state.update(copy.deepcopy(original))
