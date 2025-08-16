import uuid
from decimal import Decimal
from typing import Dict, List

from ..models import Account, Customer, Transaction


class BankingService:
    """Provides services for managing bank accounts and transactions."""

    def __init__(self):
        self._customers: Dict[uuid.UUID, Customer] = {}
        self._accounts: Dict[uuid.UUID, Account] = {}
        self._transactions: List[Transaction] = []

    def create_customer(self, name: str, email: str) -> Customer:
        """Creates a new customer and adds them to the system."""
        if not name or not email:
            raise ValueError("Name and email are required.")
        customer = Customer(name=name, email=email)
        self._customers[customer.customer_id] = customer
        return customer

    def open_account(
        self,
        customer_id: uuid.UUID,
        account_type: str,
        initial_deposit: Decimal = Decimal("0.0"),
    ) -> Account:
        """Opens a new account for a customer."""
        if customer_id not in self._customers:
            raise ValueError("Customer not found.")
        if initial_deposit < Decimal("0.0"):
            raise ValueError("Initial deposit cannot be negative.")

        account = Account(
            customer_id=customer_id,
            account_type=account_type,
            balance=initial_deposit,
        )
        self._accounts[account.account_id] = account

        if initial_deposit > Decimal("0.0"):
            self._log_transaction(account.account_id, "deposit", initial_deposit)

        return account

    def get_account(self, account_id: uuid.UUID) -> Account:
        """Retrieves an account by its ID."""
        if account_id not in self._accounts:
            raise ValueError("Account not found.")
        return self._accounts[account_id]

    def deposit(self, account_id: uuid.UUID, amount: Decimal) -> Transaction:
        """Deposits funds into an account."""
        account = self.get_account(account_id)
        account.deposit(amount)
        return self._log_transaction(account_id, "deposit", amount)

    def withdraw(self, account_id: uuid.UUID, amount: Decimal) -> Transaction:
        """Withdraws funds from an account."""
        account = self.get_account(account_id)
        account.withdraw(amount)
        return self._log_transaction(account_id, "withdrawal", amount)

    def transfer(
        self, from_account_id: uuid.UUID, to_account_id: uuid.UUID, amount: Decimal
    ) -> tuple[Transaction, Transaction]:
        """Transfers funds between two accounts."""
        from_account = self.get_account(from_account_id)
        to_account = self.get_account(to_account_id)

        from_account.withdraw(amount)
        to_account.deposit(amount)

        from_transaction = self._log_transaction(
            from_account_id, "transfer_out", -amount
        )
        to_transaction = self._log_transaction(to_account_id, "transfer_in", amount)

        return from_transaction, to_transaction

    def get_transactions_for_account(self, account_id: uuid.UUID) -> List[Transaction]:
        """Gets all transactions for a specific account."""
        return [t for t in self._transactions if t.account_id == account_id]

    def _log_transaction(
        self, account_id: uuid.UUID, transaction_type: str, amount: Decimal
    ) -> Transaction:
        """Logs a transaction and adds it to the transaction list."""
        transaction = Transaction(
            account_id=account_id,
            transaction_type=transaction_type,
            amount=amount,
        )
        self._transactions.append(transaction)
        return transaction
