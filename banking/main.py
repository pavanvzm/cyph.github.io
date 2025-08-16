from datetime import date
from decimal import Decimal

from .reports import Agent
from .services import BankingService


def run_demonstration():
    """
    Runs a demonstration of the banking system,
    simulating transactions and generating a report.
    """
    print("--- Starting Banking System Demonstration ---")

    # 1. Initialize services
    service = BankingService()
    agent = Agent()

    # 2. Create customers
    print("\nCreating customers...")
    customer1 = service.create_customer("Alice", "alice@example.com")
    customer2 = service.create_customer("Bob", "bob@example.com")
    print(f"Created: {customer1}")
    print(f"Created: {customer2}")

    # 3. Open accounts
    print("\nOpening accounts...")
    account1 = service.open_account(
        customer1.customer_id, "checking", initial_deposit=Decimal("1000.00")
    )
    account2 = service.open_account(
        customer2.customer_id, "savings", initial_deposit=Decimal("5000.00")
    )
    print(f"Opened: {account1} for {customer1.name}")
    print(f"Opened: {account2} for {customer2.name}")

    # 4. Simulate transactions
    print("\nSimulating transactions...")
    service.deposit(account1.account_id, Decimal("500.00"))
    print(f"Deposited 500.00 into Alice's checking. New balance: {account1.balance:.2f}")

    service.withdraw(account2.account_id, Decimal("200.00"))
    print(f"Withdrew 200.00 from Bob's savings. New balance: {account2.balance:.2f}")

    service.transfer(account2.account_id, account1.account_id, Decimal("1000.00"))
    print(
        "Transferred 1000.00 from Bob to Alice. "
        f"Final balances: Alice: {account1.balance:.2f}, Bob: {account2.balance:.2f}"
    )

    # 5. Generate daily report
    print("\n--- Generating Daily Report ---")
    today = date.today()
    report = agent.generate_daily_report(today, service._transactions)
    print(report)

    print("--- Demonstration Finished ---")


if __name__ == "__main__":
    run_demonstration()
