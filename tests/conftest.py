"""Integration tests configuration file."""

import pytest
import webtest

from mctweetface.test.conftest import pytest_configure  # pylint: disable=unused-import
from mctweetface import views


@pytest.fixture
def client(tmpdir):
    """Test client for the API."""
    tmpdir.chdir()
    return webtest.TestApp(views.app)
