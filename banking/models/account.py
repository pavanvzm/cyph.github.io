import uuid
from dataclasses import dataclass, field
from decimal import Decimal

@dataclass
class Account:
    """Represents a bank account."""
    customer_id: uuid.UUID
    account_type: str
    balance: Decimal = Decimal("0.0")
    account_id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __str__(self):
        return f"Account(type='{self.account_type}', balance={self.balance:.2f}, id='{self.account_id}')"

    def deposit(self, amount: Decimal):
        """Deposits a positive amount into the account."""
        if amount <= Decimal("0"):
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: Decimal):
        """Withdraws a positive amount from the account if funds are sufficient."""
        if amount <= Decimal("0"):
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
