"""Integration tests configuration file."""

import pytest
import webtest

from mctweetyface import views


@pytest.fixture
def client(tmpdir):
    """Test client for the API."""
    tmpdir.chdir()
    views.app.catchall = False
    return webtest.TestApp(views.app)
