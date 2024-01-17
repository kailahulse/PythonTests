import pytest 
from pytest_mock import mocker
import io
import sys
from main import main as func1
import subprocess
from contextlib import redirect_stdout
import pdb
import logging
import random
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

@pytest.fixture
def mocked_input(mocker):
    # Create a mocker for input function
    return mocker.patch('builtins.input')

@pytest.fixture
def mocked_random_functions(mocker):
    # Create mockers for random module functions
    return {
        'randint': mocker.patch('random.randint'),
        'random': mocker.patch('random.random'),
        'randrange': mocker.patch('random.randrange'),
    }

def test_exit(mocked_input, mocked_random_functions, capsys):
    mocked_input.side_effect = ['a', 'quit']
    for func_mock in mocked_random_functions.values():
        func_mock.return_value = 9
    program_path = 'main.py'
    result = subprocess.run(['python', program_path], capture_output=True, text=True)
    assert result.returncode is not None

def test_successful_game(mocked_input, mocked_random_functions, capsys):
    mocked_input.side_effect = ['a', 'b', 'a', 'c', 'k', 'quit']
    random.seed(9)
    mocked_random_functions['randint'].return_value = 9
    mocked_random_functions['randrange'].return_value = 9
    try:
        func1()
    except SystemExit:
        pass  # Continue execution if SystemExit is raised
    captured_output = capsys.readouterr().out.lower()
    assert 'you win' in captured_output

def test_failed_game(mocked_input, mocked_random_functions, capsys):
    mocked_input.side_effect = ['x', 'y', 'f', 'l', 'o', 'quit']
    random.seed(9)
    mocked_random_functions['randint'].return_value = 9
    mocked_random_functions['randrange'].return_value = 9
    try:
        func1()
    except SystemExit:
        pass  # Continue execution if SystemExit is raised
    captured_output = capsys.readouterr().out.lower()
    assert 'you lose' in captured_output

