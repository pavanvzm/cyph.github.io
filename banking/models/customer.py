import uuid
from dataclasses import dataclass, field

@dataclass
class Customer:
    """Represents a customer of the bank."""
    name: str
    email: str
    customer_id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __str__(self):
        return f"Customer(name='{self.name}', email='{self.email}', id='{self.customer_id}')"
