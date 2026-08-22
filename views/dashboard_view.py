import streamlit as st


def show_dashboard(controller):

    st.title(
        "📊 Personal Expense Dashboard"
    )


    st.caption(
        "Track your financial health "
        "and understand your spending."
    )


    # =====================================================
    # SUMMARY CARDS
    # =====================================================

    summary = controller.get_summary()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "💵 Total Income",
            f"৳{summary['income']:,.2f}"
        )


    with col2:

        st.metric(
            "💸 Total Expenses",
            f"৳{summary['expenses']:,.2f}"
        )


    with col3:

        st.metric(
            "💰 Current Balance",
            f"৳{summary['balance']:,.2f}"
        )


    st.divider()


    # =====================================================
    # EXPENSE BY CATEGORY
    # =====================================================

    st.subheader(
        "🍕 Expenses by Category"
    )


    category_data = (
        controller.get_category_expenses()
    )


    if category_data.empty:

        st.info(
            "Add some expenses to see analytics."
        )

    else:

        col1, col2 = st.columns(2)


        with col1:

            st.bar_chart(
                category_data.set_index(
                    "category"
                )["total"],
                color="#2DD4BF"
            )


        with col2:

            st.dataframe(
                category_data,
                use_container_width=True,
                hide_index=True
            )


    st.divider()


    # =====================================================
    # MONTHLY TREND
    # =====================================================

    st.subheader(
        "📈 Monthly Spending Trend"
    )


    monthly_data = (
        controller.get_monthly_expenses()
    )


    if monthly_data.empty:

        st.info(
            "Not enough data for a monthly trend."
        )

    else:

        st.line_chart(
            monthly_data.set_index(
                "month"
            )["total"],
            color="#2DD4BF"
        )


    st.divider()


    # =====================================================
    # INSIGHTS
    # =====================================================

    st.subheader(
        "💡 Spending Insights"
    )


    top_category = (
        controller.get_top_category()
    )


    if top_category:

        st.markdown(
            f"""
            <div class="app-card" style="border-left: 3px solid #2DD4BF;">
                <div style="color: #9CA3AF; font-size: 0.85rem;
                            font-weight: 600; margin-bottom: 0.3rem;">
                    TOP SPENDING CATEGORY
                </div>
                <div style="font-size: 1.4rem; font-weight: 800;
                            color: #2DD4BF;">
                    {top_category}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.info(
            "Add transactions to generate insights."
        )