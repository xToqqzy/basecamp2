import os
import sys
import json
import sqlite3

from datetime import datetime
from basecamp2.week14.transaction import Transaction


class FinanceApp:
    def __init__(self, db_name='finance.db'):
        self.connection = sqlite3.connect(os.path.join(sys.path[0], db_name))
        self.cursor = self.connection.cursor()

    def build_database(self):
        self.cursor.execute("DROP TABLE IF EXISTS transactions")
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY,
                            date TEXT,
                            description TEXT,
                            category TEXT,
                            amount REAL)''')
        self.connection.commit()

    def load_transactions_from_json(self, json_file):
        with open('/Users/dilshad/source/basecamp2/basecamp2/week14/transactions.json', 'r') as file:
            json_data = json.load(file)

            raise NotImplementedError

    def add_transaction(self, date, description, category, amount) -> Transaction:
        self.cursor.execute('''
            INSERT INTO transactions (date, description, category, amount)
            VALUES (?, ?, ?, ?)
        ''', (date, description, category, amount))
        self.connection.commit()

        transaction_id = self.cursor.lastrowid
        return Transaction(transaction_id, date, description, category, amount)

    def update_transaction(self, transaction_id, date, description, category, amount) -> bool:
        self.cursor.execute('''
                UPDATE transactions (id,date, description, category, amount)
                VALUES (?,?, ?, ?, ?)
            ''', (transaction_id, date, description, category, amount))

        if self.cursor.rowcount == 0:
            return False
        else:
            self.connection.commit()
            return True

    def delete_transaction(self, transaction_id) -> bool:
        self.cursor.execute(
            "SELECT * FROM transactions WHERE id = ?", (transaction_id,))
        row = self.cursor.fetchone()
        if row is not None:
            self.cursor.execute(
                "DELETE FROM transactions WHERE id = ?", (transaction_id,))
            self.connection.commit()
            return True
        else:
            return False

    def search_transactions(self, term: str) -> list[Transaction]:
        pass

    def get_transactions(self, year: int | None = None) -> list[Transaction]:
        raise NotImplementedError

    def get_expenses(self) -> list[tuple[str, float]]:
        raise NotImplementedError

    def get_savings(self) -> list[tuple[str, float]]:
        raise NotImplementedError

    def count_transactions(self, year: int | None = None) -> int:
        raise NotImplementedError

    def get_report(self, year: int | None = None) -> dict[str, float]:
        raise NotImplementedError
