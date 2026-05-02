
from unittest import TestCase
import py_bank
class TestEmail(TestCase):
    def test_that_email_exists(self):
        py_bank.email('yums@yomis.com')
        
    def that_email_length_is_minimm_of_8_characters(self):
        is_an_email = py_bank.email('yums@yomis.com')
        yum_yum = True
        self.assertEqual(is_an_email, yum_yum)
    def that_email_length_is_less_8_characters_return_false(self):
        is_an_email = py_bank.email('yu@yo.m')
        yum_yum = False
        self.assertEqual(is_an_email, yum_yum)
    def test_that_invalid_email_raise_value_error(self):
        self.assertRaises(ValueError, py_bank.email, 'yumsyomis.com')
    def test_that_valid_email_have_special_character(self):
        is_an_email = py_bank.email('yums@yomis.com')
        yum_yum = True
        self.assertEqual(is_an_email, yum_yum)
    def test_that_valid_email_does_not_have_special_character(self):
        message = py_bank.email('@yumsyomis.com')
        yum_yum = message
        self.assertEqual(yum_yum, 'Invalid email')
    def test_that_valid_email_does_not_end_with_special_character(self):
        message = py_bank.email('@yumsyomis.com@')
        yum_yum = message
        self.assertEqual(yum_yum, 'Invalid email')
    def test_that_valid_email_does_not_end_with_special_character_and_emoji(self):
        message = py_bank.email('@yumsyomis.com@😄️')
        yum_yum = message
        self.assertEqual(yum_yum, 'Invalid email')
    def test_that_email_exists_and_dont_have_emoji(self):
        py_bank.email('😃️yums@😄️yomis.😌️com😃️')
class TestCalculatedBalance(TestCase):
    def test_that_calculated_balance_returns_correct_balance(self):
        actual = py_bank.calculated_balance([4000, 2000])
        expected = 6000
        self.assertEqual(actual, expected)
        actual = py_bank.calculated_balance([500, 5000])
        expected = 5500
        self.assertEqual(actual, expected)
        actual = py_bank.calculated_balance([5000, -2000, 3000, -1000])
        expected = 5000
        self.assertEqual(actual, expected)
    def  test_that_calculated_balance_returns_0_with_empty_transaction(self):
        actual = py_bank.calculated_balance([]) 
        expected = 0
        self.assertEqual(actual, expected)
class TestStrongPassword(TestCase):
  def test_that_is_strong_password_return_true_with_minimum_of_8_characters(self):
        is_strong = pybank.is_strong_password("password")
        self.assertTrue(is_strong)
    def test_that_is_strong_password_return_false_with_minimum_of_8_characters(self):
        is_strong = pybank.is_strong_password("passwor")
        self.assertFalse(is_strong)
class TestApplyInterest(TestCase):   
    def test_that_apply_interest_function_return_correct_balance(self):
        actual = pybank.apply_interest(5000, 0.05, 10)
        expected = 8144.47
        self.assertEqual(actual, expected)
    def test_that_apply_interest_function_rate_can_not_be_negative(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(5000, -0.05, 10)
    def test_that_apply_interest_function_years_can_not_be_less_than_one(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(5000, 0.05, 0.2)
class TestGetTransactionSummary(TestCase):
    def test_that_get_transaction_summary_function_return_correct_summary(self):
        transactions = [["credit", 2000], ["debit", 500], ["credit", 1000]]
        actual = pybank.get_transaction_summary(transactions)
        expected = [["total_credits", 3000], ["total_debits", 500], ["net_balance", 2500], ["transaction_count", 3]]
        self.assertEqual(actual, expected)
    
    
    
