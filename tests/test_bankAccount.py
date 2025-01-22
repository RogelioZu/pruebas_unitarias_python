import unittest
import os
from src.bankAccount import bank_account

class bankAccount_tests(unittest.TestCase):

    def setUp(self):
        self.account = bank_account(balance=1000, log_file='transaction_log.txt')

    def tearDown(self):
        if os.path.exists('transaction_log.txt'):
            os.remove(self.account.log_file)


    def _count_lines(self,path):
        with open(path,'r')as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(1000)
        assert new_balance == 0

    def test_get_balance(self):
        assert self.account.check_balance() == 1000


    def test_transfer(self):
        new_balance = self.account.transfer(1000)
        assert new_balance == 0

    def test_tranfer_error(self):
        try:
            self.account.transfer(1200)
        except ValueError as e:
            assert isinstance(e,ValueError)
            print("Se capturó y verificó un ValueError correctamente.", e)
        else:
            assert False, "Fallo la excepcion ValueError "

    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists('transaction_log.txt'))

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2

