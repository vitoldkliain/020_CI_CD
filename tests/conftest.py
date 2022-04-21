import sys
import os

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(sys.path[0])))

from app.main import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
