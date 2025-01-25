import unittest
from tests.test_bankAccount import bankAccount_tests

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(bankAccount_tests("test_deposit"))
    suite.addTest(bankAccount_tests("test_withdraw"))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())



    

