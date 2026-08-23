import pandas as pd


class DashboardController:

    def __init__(self, database):

        self.database = database


    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    def get_summary(self):

        query = """
            SELECT

                COALESCE(
                    SUM(
                        CASE
                            WHEN transaction_type = 'Income'
                            THEN amount
                            ELSE 0
                        END
                    ),
                    0
                ) AS income,

                COALESCE(
                    SUM(
                        CASE
                            WHEN transaction_type = 'Expense'
                            THEN amount
                            ELSE 0
                        END
                    ),
                    0
                ) AS expenses

            FROM transactions
        """


        result = self.database.fetch_all(query)

        income = float(result[0]["income"])

        expenses = float(result[0]["expenses"])

        balance = income - expenses


        return {

            "income": income,

            "expenses": expenses,

            "balance": balance

        }


    # -----------------------------------------------------
    # CATEGORY EXPENSES
    # -----------------------------------------------------

    def get_category_expenses(self):

        query = """
            SELECT

                category,

                SUM(amount) AS total

            FROM transactions

            WHERE transaction_type = 'Expense'

            GROUP BY category

            ORDER BY total DESC
        """


        rows = self.database.fetch_all(query)


        return pd.DataFrame(
            [dict(row) for row in rows]
        )


    # -----------------------------------------------------
    # MONTHLY EXPENSES
    # -----------------------------------------------------

    def get_monthly_expenses(self):

        query = """
            SELECT

                substr(transaction_date, 1, 7)
                AS month,

                SUM(amount) AS total

            FROM transactions

            WHERE transaction_type = 'Expense'

            GROUP BY month

            ORDER BY month
        """


        rows = self.database.fetch_all(query)


        return pd.DataFrame(
            [dict(row) for row in rows]
        )


    # -----------------------------------------------------
    # TOP CATEGORY
    # -----------------------------------------------------

    def get_top_category(self):

        data = self.get_category_expenses()


        if data.empty:

            return None


        return data.iloc[0]["category"]