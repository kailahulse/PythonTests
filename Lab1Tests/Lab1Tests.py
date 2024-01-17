import unittest
from unittest import mock
from main import main as func1
import main
import sys
import io
from io import StringIO

class SimpleTests(unittest.TestCase):
    # word is aback
   # @mock.patch('random.*', 9)
    # @mock.patch('builtins.input', create=True)
    # def test_Exit(self, mocked_input):
    #      # Set up the incorrect input
    #     mocked_input.side_effect = ['quit']

    #     with self.assertRaises(SystemExit) as cm:
    #         func1()
    #         pass

    #     # Check the exit code if needed
    #     if cm.exception.code is not None:
    #         self.fail(f"Unexpected SystemExit with code: {cm.exception.code}")
    
    # Define a lambda function that takes two arguments and returns 9
    mocked_random_choice = lambda a, b: 9
    # Define a lambda function that takes no arguments and returns 9
    mocked_random_random = lambda: 9
    # Patch the functions that take two arguments with the lambda function
    @mock.patch('random.randint', mocked_random_choice) 
    @mock.patch('random.randrange', mocked_random_choice) 
    # Patch the function that takes no arguments with the lambda function
    @mock.patch('random.random', mocked_random_random)
    @mock.patch('builtins.input', side_effect = ['a', 'b', 'a', 'c', 'k', ])
    def test_SuccessfulGame(self, mocked_input):
        # Redirect stdout to capture the output
       # with mock.patch('sys.stdout', new = StringIO()) as fake_out:
            # with self.assertRaises(SystemExit) as cm:
        with mock.patch('sys.stdout') as mock_stdout:
        # Call your func1 function
            with self.assertRaises(SystemExit) as cm:
                func1()
               # sys.exit()
                # Get the output from the mock object
                output_string = mock_stdout.getvalue().strip()
                # Assert that the output contains "You Win"
                
                self.assertIn("You Win", output_string)

    # @mock.patch('random.randint', 9) 
    # @mock.patch('random.random', 9)
    # @mock.patch('random.randrange', 9)    
    # @mock.patch('builtins.input', create=True)
    # def test_FailedGame(self, mocked_input):
    #     mocked_input.side_effect = ['z', 'y', 'n', 'w']
    #     capturedOutput = StringIO.StringIO()
    #     sys.stdout = capturedOutput
    #     main()
    #     sys.stdout = sys.__stdout__  
    #     print('Captured')
    #     capturedOutput.getvalue()
    #     self.assertIn("You lose", capturedOutput.getvalue())
                
    # # Patch the functions that take two arguments with the lambda function
    # @mock.patch('random.randint', mocked_random_choice) 
    # @mock.patch('random.randrange', mocked_random_choice) 
    # # Patch the function that takes no arguments with the lambda function
    # @mock.patch('random.random', mocked_random_random)
    # @mock.patch('builtins.input', side_effect = ['a', 'b', 'a', 'c', 'k', 'quit'])
    # def test_FailedGame




if __name__ == "__main__":
    unittest.main() # run all tests