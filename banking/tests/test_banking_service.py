import unittest
from decimal import Decimal

from ..services import BankingService


class TestBankingService(unittest.TestCase):
    """Unit tests for the BankingService."""

    def setUp(self):
        """Set up a new BankingService instance for each test."""
        self.service = BankingService()
        self.customer1 = self.service.create_customer("Alice", "alice@example.com")
        self.account1 = self.service.open_account(
            self.customer1.customer_id, "checking", Decimal("1000")
        )
        self.customer2 = self.service.create_customer("Bob", "bob@example.com")
        self.account2 = self.service.open_account(
            self.customer2.customer_id, "savings", Decimal("5000")
        )

    def test_create_customer(self):
        """Test creating a new customer."""
        self.assertEqual(len(self.service._customers), 2)
        customer = self.service.create_customer("Charlie", "charlie@example.com")
        self.assertEqual(len(self.service._customers), 3)
        self.assertEqual(customer.name, "Charlie")

    def test_open_account(self):
        """Test opening a new account."""
        self.assertEqual(len(self.service._accounts), 2)
        account = self.service.open_account(self.customer1.customer_id, "savings")
        self.assertEqual(len(self.service._accounts), 3)
        self.assertEqual(account.customer_id, self.customer1.customer_id)

    def test_deposit(self):
        """Test depositing funds."""
        initial_balance = self.account1.balance
        self.service.deposit(self.account1.account_id, Decimal("500"))
        self.assertEqual(self.account1.balance, initial_balance + Decimal("500"))
        self.assertEqual(len(self.service._transactions), 3) # 2 initial, 1 deposit

    def test_withdraw(self):
        """Test withdrawing funds."""
        initial_balance = self.account1.balance
        self.service.withdraw(self.account1.account_id, Decimal("200"))
        self.assertEqual(self.account1.balance, initial_balance - Decimal("200"))
        self.assertEqual(len(self.service._transactions), 3) # 2 initial, 1 withdrawal

    def test_transfer_success(self):
        """Test a successful transfer."""
        balance1 = self.account1.balance
        balance2 = self.account2.balance
        amount = Decimal("500")

        self.service.transfer(self.account1.account_id, self.account2.account_id, amount)

        self.assertEqual(self.account1.balance, balance1 - amount)
        self.assertEqual(self.account2.balance, balance2 + amount)
        self.assertEqual(len(self.service._transactions), 4) # 2 initial, 2 for transfer

    def test_transfer_insufficient_funds(self):
        """Test a transfer with insufficient funds."""
        with self.assertRaises(ValueError):
            self.service.transfer(
                self.account1.account_id, self.account2.account_id, Decimal("2000")
            )


if __name__ == "__main__":
    unittest.main()
