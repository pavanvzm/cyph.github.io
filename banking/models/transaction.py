import uuid
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal

@dataclass
class Transaction:
    """Represents a single transaction."""
    account_id: uuid.UUID
    transaction_type: str
    amount: Decimal
    transaction_id: uuid.UUID = field(default_factory=uuid.uuid4)
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def __str__(self):
        return (
            f"Transaction(id='{self.transaction_id}', account_id='{self.account_id}', "
            f"type='{self.transaction_type}', amount={self.amount:.2f}, "
            f"timestamp='{self.timestamp.isoformat()}')"
        )
