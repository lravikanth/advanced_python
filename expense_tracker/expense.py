from dataclasses import dataclass

from tax_calulation import discounts, hello, tx_calc


@dataclass
class Expense:
    id: int
    amount: float
    desc: str

    def total_amount(self) -> float:
        hello()
        return tx_calc.TaxCalc.tax(self.amount) + self.amount

    def price_discount(self) -> float:
        return self.amount * discounts.discounts / 100
