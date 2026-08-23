from models.budget_model import Budget


class BudgetController:

    def __init__(self, database):

        self.database = database


    # -----------------------------------------------------
    # SAVE BUDGET
    # -----------------------------------------------------

    def save_budget(self, budget: Budget):

        if budget.monthly_limit <= 0:

            raise ValueError(
                "Budget must be greater than 0."
            )


        if budget.category.strip() == "":

            raise ValueError(
                "Category cannot be empty."
            )


        query = """
            INSERT INTO budgets
            (
                category,
                monthly_limit
            )

            VALUES (?, ?)

            ON CONFLICT(category)

            DO UPDATE SET
                monthly_limit = excluded.monthly_limit
        """


        self.database.execute(
            query,
            (
                budget.category,
                budget.monthly_limit
            )
        )


    # -----------------------------------------------------
    # GET BUDGETS
    # -----------------------------------------------------

    def get_all_budgets(self):

        query = """
            SELECT *
            FROM budgets
            ORDER BY category
        """

        return self.database.fetch_all(query)


    # -----------------------------------------------------
    # DELETE BUDGET
    # -----------------------------------------------------

    def delete_budget(self, budget_id):

        query = """
            DELETE FROM budgets
            WHERE id = ?
        """

        self.database.execute(
            query,
            (budget_id,)
        )


    # -----------------------------------------------------
    # GET CURRENT SPENDING
    # -----------------------------------------------------

    def get_category_spending(self, category):

        query = """
            SELECT
                COALESCE(SUM(amount), 0) AS total

            FROM transactions

            WHERE transaction_type = 'Expense'

            AND LOWER(category) = LOWER(?)

            AND substr(transaction_date, 1, 7)
                = strftime('%Y-%m', 'now')
        """

        result = self.database.fetch_all(
            query,
            (category,)
        )

        return float(result[0]["total"])