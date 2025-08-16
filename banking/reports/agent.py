from datetime import date
from decimal import Decimal
from typing import List

from ..models import Transaction


class Agent:
    """The AI agent for analyzing banking data and generating reports."""

    def generate_daily_report(
        self, report_date: date, transactions: List[Transaction]
    ) -> str:
        """
        Generates a daily financial report for a given date.

        Args:
            report_date: The date for which to generate the report.
            transactions: A list of all transactions to be considered.

        Returns:
            A formatted string containing the daily report.
        """
        daily_transactions = [
            t for t in transactions if t.timestamp.date() == report_date
        ]

        total_deposits = sum(
            t.amount
            for t in daily_transactions
            if t.transaction_type in ["deposit", "transfer_in"]
        )
        total_withdrawals = sum(
            t.amount
            for t in daily_transactions
            if t.transaction_type in ["withdrawal", "transfer_out"]
        )
        net_flow = total_deposits - total_withdrawals

        # AI-powered insight (currently rule-based)
        if net_flow > 10000:
            ai_summary = "A strong day with significant positive cash flow."
        elif net_flow > 0:
            ai_summary = "A positive cash flow day."
        elif net_flow == 0 and daily_transactions:
            ai_summary = "A balanced day with no net change in cash flow."
        elif net_flow < -10000:
            ai_summary = "A day with significant negative cash flow."
        else:
            ai_summary = "A negative cash flow day."

        if not daily_transactions:
            ai_summary = "No transactions recorded for this day."

        report = f"""
        --- Daily Financial Report for {report_date.isoformat()} ---

        AI Summary: {ai_summary}

        Key Metrics:
        - Total Transactions: {len(daily_transactions)}
        - Total Deposits: {total_deposits:,.2f}
        - Total Withdrawals: {total_withdrawals:,.2f}
        - Net Cash Flow: {net_flow:,.2f}

        ----------------------------------------------------
        """
        return report.strip()
