import streamlit as st

from models.budget_model import Budget


CATEGORIES = [

    "Food",

    "Transport",

    "Education",

    "Shopping",

    "Entertainment",

    "Bills",

    "Healthcare",

    "Other"

]


def show_budgets(controller):

    st.title("🎯 Monthly Budgets")


    # =====================================================
    # ADD BUDGET
    # =====================================================

    st.subheader("➕ Set Budget")

    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    with st.form("budget_form"):

        category = st.selectbox(
            "Category",
            CATEGORIES
        )


        amount = st.number_input(
            "Monthly Budget (৳)",
            min_value=1.0,
            value=5000.0,
            step=500.0
        )


        submit = st.form_submit_button(
            "💾 Save Budget",
            use_container_width=True
        )


        if submit:

            budget = Budget(

                category=category,

                monthly_limit=amount

            )


            try:

                controller.save_budget(
                    budget
                )

                st.success(
                    "Budget saved successfully!"
                )

                st.rerun()


            except ValueError as error:

                st.error(str(error))

    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()


    # =====================================================
    # BUDGET STATUS
    # =====================================================

    st.subheader(
        "📊 Current Budget Status"
    )


    budgets = controller.get_all_budgets()


    if not budgets:

        st.info(
            "No budgets configured."
        )

        return


    for budget in budgets:

        spent = controller.get_category_spending(
            budget["category"]
        )


        limit = float(
            budget["monthly_limit"]
        )


        percentage = spent / limit


        if percentage > 1:

            progress = 1

        else:

            progress = percentage


        st.markdown('<div class="app-card">', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(
            [2, 4, 1]
        )


        with col1:

            st.markdown(
                f"""
                <div style="font-weight: 700; font-size: 1.1rem;
                            margin-bottom: 0.25rem;">
                    {budget['category']}
                </div>
                <div style="color: #9CA3AF; font-size: 0.9rem;">
                    ৳{spent:,.2f} <span style="color: #4B5563;">/</span>
                    ৳{limit:,.2f}
                </div>
                """,
                unsafe_allow_html=True
            )


        with col2:

            st.progress(progress)


            if percentage >= 1:

                st.error(
                    "⚠️ Budget exceeded!"
                )

            elif percentage >= 0.8:

                st.warning(
                    "🔔 Approaching budget limit"
                )

            else:

                st.success(
                    "✅ Within budget"
                )


        with col3:

            if st.button(
                "🗑️",
                key=f"budget_{budget['id']}"
            ):

                controller.delete_budget(
                    budget["id"]
                )

                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)