"""Tests"""

import unittest
from unittest.mock import patch
from what_is_year_now import what_is_year_now, main


class TestWhatIsYearNow(unittest.TestCase):
    """Tests fot what is year now function"""

    def test_year_format_ymd(self):
        """Test year format in YMD"""

        datetime_str = '2022-08-25T18:30Z'
        with patch('urllib.request.urlopen') as mock_urlopen:
            (
                mock_urlopen.return_value
                .__enter__.return_value
                .read.return_value
            ) = '{"currentDateTime": "' + datetime_str + '"}'
            year = what_is_year_now()
            self.assertEqual(year, 2022)

    def test_year_format_dmy(self):
        """Test year format in DMY"""

        datetime_str = '25.08.2022T18:30Z'
        with patch('urllib.request.urlopen') as mock_urlopen:
            (
                mock_urlopen.return_value
                .__enter__.return_value
                .read.return_value
            ) = '{"currentDateTime": "' + datetime_str + '"}'
            year = what_is_year_now()
            self.assertEqual(year, 2022)

    def test_invalid_format(self):
        """Test invalid format"""

        datetime_str = '2022/08/25T18:30Z'
        with patch('urllib.request.urlopen') as mock_urlopen:
            (
                mock_urlopen.return_value
                .__enter__.return_value
                .read.return_value
            ) = '{"currentDateTime": "' + datetime_str + '"}'
            with self.assertRaises(ValueError):
                what_is_year_now()

    def test_api_error(self):
        """Test unexpected error"""

        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.side_effect = Exception('API is down')
            with self.assertRaises(Exception):
                what_is_year_now()

    def test_main(self):
        """Test entry for script"""
        with patch(
            'what_is_year_now.what_is_year_now', return_value=2019
        ):
            try:
                main()
            except AssertionError as exc:
                raise ValueError('Unexpected behaviour') from exc
