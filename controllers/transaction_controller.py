from models.transaction_model import Transaction


class TransactionController:

    def __init__(self, database):

        self.database = database


    # -----------------------------------------------------
    # ADD TRANSACTION
    # -----------------------------------------------------

    def add_transaction(self, transaction: Transaction):

        if transaction.amount <= 0:

            raise ValueError(
                "Amount must be greater than 0."
            )


        if transaction.category.strip() == "":

            raise ValueError(
                "Category cannot be empty."
            )


        if transaction.transaction_type not in [
            "Income",
            "Expense"
        ]:

            raise ValueError(
                "Invalid transaction type."
            )


        query = """
            INSERT INTO transactions
            (
                transaction_type,
                amount,
                category,
                description,
                transaction_date
            )

            VALUES (?, ?, ?, ?, ?)
        """


        values = (

            transaction.transaction_type,

            transaction.amount,

            transaction.category,

            transaction.description,

            transaction.transaction_date.isoformat()

        )


        return self.database.insert(
            query,
            values
        )


    # -----------------------------------------------------
    # GET ALL TRANSACTIONS
    # -----------------------------------------------------

    def get_all_transactions(self):

        query = """
            SELECT *
            FROM transactions
            ORDER BY transaction_date DESC, id DESC
        """

        return self.database.fetch_all(query)


    # -----------------------------------------------------
    # DELETE TRANSACTION
    # -----------------------------------------------------

    def delete_transaction(self, transaction_id):

        query = """
            DELETE FROM transactions
            WHERE id = ?
        """

        self.database.execute(
            query,
            (transaction_id,)
        )