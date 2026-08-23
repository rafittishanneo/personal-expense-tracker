import streamlit as st

from styles import inject_custom_css, render_theme_toggle

from models.database import Database
from controllers.transaction_controller import TransactionController
from controllers.budget_controller import BudgetController
from controllers.dashboard_controller import DashboardController

from views.dashboard_view import show_dashboard
from views.transaction_view import show_transactions
from views.budget_view import show_budgets


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)

inject_custom_css()


# ---------------------------------------------------------
# DATABASE
# ---------------------------------------------------------

@st.cache_resource
def create_database():
    return Database()


database = create_database()


# ---------------------------------------------------------
# CONTROLLERS
# ---------------------------------------------------------

transaction_controller = TransactionController(database)
budget_controller = BudgetController(database)
dashboard_controller = DashboardController(database)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.markdown(
    """
    <div style="padding: 0.4rem 0 1rem 0;">
        <div style="font-size: 1.5rem;">💰</div>
        <div style="font-size: 1.3rem; font-weight: 800;
                    letter-spacing: -0.02em; margin-top: 0.2rem;
                    background: var(--gradient-brand);
                    -webkit-background-clip: text;
                    background-clip: text;
                    -webkit-text-fill-color: transparent;">
            Expense Tracker
        </div>
        <div style="font-size: 0.85rem; color: var(--text-muted);">
            Personal finance, simplified
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

render_theme_toggle()

page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Dashboard",
        "💳 Transactions",
        "🎯 Budgets"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Track your income, expenses, budgets and spending patterns."
)


# ---------------------------------------------------------
# PAGE ROUTING
# ---------------------------------------------------------

if page == "📊 Dashboard":

    show_dashboard(dashboard_controller)

elif page == "💳 Transactions":

    show_transactions(transaction_controller)

elif page == "🎯 Budgets":

    show_budgets(budget_controller)
