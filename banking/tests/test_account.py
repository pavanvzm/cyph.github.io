import unittest
import uuid
from decimal import Decimal

from ..models import Account


class TestAccount(unittest.TestCase):
    """Unit tests for the Account model."""

    def test_deposit_success(self):
        """Test a successful deposit."""
        account = Account(customer_id=uuid.uuid4(), account_type="checking")
        account.deposit(Decimal("100.00"))
        self.assertEqual(account.balance, Decimal("100.00"))

    def test_withdraw_success(self):
        """Test a successful withdrawal."""
        account = Account(
            customer_id=uuid.uuid4(),
            account_type="checking",
            balance=Decimal("100.00"),
        )
        account.withdraw(Decimal("50.00"))
        self.assertEqual(account.balance, Decimal("50.00"))

    def test_withdraw_insufficient_funds(self):
        """Test withdrawing more than the balance."""
        account = Account(
            customer_id=uuid.uuid4(),
            account_type="checking",
            balance=Decimal("100.00"),
        )
        with self.assertRaises(ValueError) as context:
            account.withdraw(Decimal("150.00"))
        self.assertEqual(str(context.exception), "Insufficient funds.")

    def test_deposit_negative_amount(self):
        """Test depositing a negative amount."""
        account = Account(customer_id=uuid.uuid4(), account_type="checking")
        with self.assertRaises(ValueError) as context:
            account.deposit(Decimal("-50.00"))
        self.assertEqual(str(context.exception), "Deposit amount must be positive.")

    def test_withdraw_negative_amount(self):
        """Test withdrawing a negative amount."""
        account = Account(
            customer_id=uuid.uuid4(),
            account_type="checking",
            balance=Decimal("100.00"),
        )
        with self.assertRaises(ValueError) as context:
            account.withdraw(Decimal("-50.00"))
        self.assertEqual(str(context.exception), "Withdrawal amount must be positive.")


if __name__ == "__main__":
    unittest.main()
