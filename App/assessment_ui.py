import streamlit as st
from enum import Enum


class Action(Enum):
    BUY = "Buy"
    SELL = "Sell"
    NOTHING = "Nothing"

    def __str__(self):
        return self.value


def calculate_shares(total: float, target: float, current: float, unit_price: float):
    variance = current - target

    if variance < 0:
        action = Action.BUY
    elif variance == 0:
        action = Action.NOTHING
    else:
        action = Action.SELL

    shares = round(abs(variance) * total / (100 * unit_price), 2)
    return action, shares


st.title("Rebalancing Tool")

security = st.text_input("Security name", value="", key="security_text_input")

total_asset = st.number_input("Total asset value", min_value=0.0, value=10000.0, key="total_asset_number_input")
target = st.number_input("Target allocation (%)", min_value=0.0, max_value=100.0, value=50.0, key="target_number_input")
current = st.number_input("Current allocation (%)", min_value=0.0, max_value=100.0, value=50.0, key="current_number_input")
unit_price = st.number_input("Unit price", min_value=0.0, value=1.0, key="unit_price_number_input")

if st.button("Calculate"):
    if not security:
        st.error("Please enter security name.")
    elif unit_price == 0:
        st.error("Unit price cannot be zero.")
    else:
        action, shares = calculate_shares(total_asset, target, current, unit_price)
        st.info(f"{security} action: {action} number of shares: {shares}")