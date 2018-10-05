# Test each function of the app.py file

import pytest
import sys
sys.path.append('/app')  # Import the app no matter where the testsing directory is located
from app import *


def test_sample_function():
    """Test the sample function"""
    assert sample_function() == "Hello World"