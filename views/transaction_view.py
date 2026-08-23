import streamlit as st
from datetime import date

from models.transaction_model import Transaction


CATEGORIES = [

    "Food",

    "Transport",

    "Education",

    "Shopping",

    "Entertainment",

    "Bills",

    "Healthcare",

    "Salary",

    "Freelance",

    "Other"

]


def show_transactions(controller):

    st.title("💳 Transactions")


    # =====================================================
    # ADD TRANSACTION
    # =====================================================

    st.subheader("➕ Add Transaction")

    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    with st.form("transaction_form"):

        col1, col2 = st.columns(2)


        with col1:

            transaction_type = st.selectbox(
                "Transaction Type",
                [
                    "Expense",
                    "Income"
                ]
            )


            amount = st.number_input(
                "Amount (৳)",
                min_value=0.01,
                value=100.0,
                step=50.0
            )


            category = st.selectbox(
                "Category",
                CATEGORIES
            )


        with col2:

            transaction_date = st.date_input(
                "Date",
                value=date.today()
            )


            description = st.text_input(
                "Description",
                placeholder="Example: Lunch"
            )


        submit = st.form_submit_button(
            "💾 Save Transaction",
            use_container_width=True
        )


        if submit:

            transaction = Transaction(

                transaction_type=transaction_type,

                amount=amount,

                category=category,

                description=description,

                transaction_date=transaction_date

            )


            try:

                controller.add_transaction(
                    transaction
                )

                st.success(
                    "Transaction added successfully!"
                )

                st.rerun()


            except ValueError as error:

                st.error(str(error))

    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()


    # =====================================================
    # TRANSACTION HISTORY
    # =====================================================

    st.subheader("📋 Transaction History")


    transactions = controller.get_all_transactions()


    if not transactions:

        st.info(
            "No transactions available."
        )

        return


    for transaction in transactions:

        is_income = (
            transaction["transaction_type"] == "Income"
        )

        accent_color = "#34D399" if is_income else "#F87171"

        sign = "+" if is_income else "-"

        description = (
            transaction["description"]
            or "-"
        )

        col1, col2 = st.columns([9, 1])

        with col1:

            st.markdown(
                f"""
                <div class="app-card-tight"
                     style="border-left: 3px solid {accent_color};
                            display: flex; justify-content: space-between;
                            align-items: center; flex-wrap: wrap; gap: 0.5rem;">
                    <div>
                        <span style="font-weight: 700; color: {accent_color};
                                     font-size: 1.05rem;">
                            {sign}৳{transaction['amount']:,.2f}
                        </span>
                        <span style="color: #6B7280; margin: 0 0.4rem;">·</span>
                        <span style="font-weight: 600;">
                            {transaction['category']}
                        </span>
                    </div>
                    <div style="color: #9CA3AF; font-size: 0.85rem;">
                        {transaction['transaction_date']} · {description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            if st.button(
                "🗑️",
                key=f"delete_{transaction['id']}"
            ):

                controller.delete_transaction(
                    transaction["id"]
                )

                st.rerun()