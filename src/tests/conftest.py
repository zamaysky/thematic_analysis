import os
import sys

import pytest

abspath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(abspath)

from client import Client


@pytest.fixture
def client():
    return Client()
