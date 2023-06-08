from unittest import TestCase

from nhs_number import is_valid
from nhs_number import REGION_ENGLAND_WALES_IOM


class ValidationTests(TestCase):
    def test_is_valid_good_one(self):
        self.assertTrue(is_valid("9876543210"))

    def test_is_valid_bad_one(self):
        self.assertFalse(is_valid("1234567890"))

    def test_is_valid_good_one_pad_right(self):
        self.assertTrue(is_valid("9876543210 "))

    def test_is_invalid_wrong_format(self):
        self.assertFalse(is_valid("123 456 789"))

    def test_is_valid_randomly_generated(self):
        self.assertTrue(is_valid("9990000018"))

    def test_is_valid_leading_zero_chi(self):
        self.assertTrue(is_valid("0607230002"))

    def test_valid_england_wales_number(self):
        self.assertTrue(is_valid("4000000632",
                                 for_region=REGION_ENGLAND_WALES_IOM))

    def test_invalid_england_wales_number(self):
        self.assertFalse(is_valid("9876543210",
                                  for_region=REGION_ENGLAND_WALES_IOM))
