from unittest import TestCase
import occuring_count
class digitAdder(TestCase):
    def test_digit_adder_exists(self):
        occuring_count.digit_adder([1,2,2,2,3])
#    def test_occur_number_counts(self):
#        actual_value = occuring_count.occur_number([1,2,2,2,3])
#        expect_value = 3
#        self.assertEqual(actual_value, expect_value)
