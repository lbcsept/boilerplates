import unittest
from unittest.mock import patch, MagicMock
from src.alexa_handler import handle_alexa_request

class TestAlexaHandler(unittest.TestCase):

    @patch('src.alexa_handler.logging')
    def test_handle_alexa_request_success(self, mock_logging):
        # Setup
        test_request = {"type": "test_request", "data": "test_data"}
        expected_response = {"status": "success", "message": "Request processed"}

        # Execute
        response = handle_alexa_request(test_request)

        # Assert
        mock_logging.info.assert_called_once_with(f"Handling Alexa request: {test_request}")
        self.assertEqual(response, expected_response)

    @patch('src.alexa_handler.logging')
    def test_handle_alexa_request_failure(self, mock_logging):
        # Setup
        test_request = {"type": "invalid_request", "data": "invalid_data"}
        expected_response = {"status": "error", "message": "Invalid request"}

        # Mock the function to simulate a failure
        with patch('src.alexa_handler.handle_alexa_request', return_value=expected_response):
            # Execute
            response = handle_alexa_request(test_request)

            # Assert
            mock_logging.info.assert_called_once_with(f"Handling Alexa request: {test_request}")
            self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()