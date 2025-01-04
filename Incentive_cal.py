import streamlit as st

def calculate_cash_in_incentive(total_upfront_cash_in):
    conversion_rate = 88  # Conversion value from Euro to INR
    if 499 <= total_upfront_cash_in < 999:
        return 0
    elif 999 <= total_upfront_cash_in < 1499:
        return 0.015 * total_upfront_cash_in * conversion_rate
    elif 1499 <= total_upfront_cash_in < 1999:
        return 0.025 * total_upfront_cash_in * conversion_rate
    elif 1999 <= total_upfront_cash_in < 2499:
        return 0.05 * total_upfront_cash_in * conversion_rate
    elif 2499 <= total_upfront_cash_in < 2999:
        return 0.075 * total_upfront_cash_in * conversion_rate
    elif 2999 <= total_upfront_cash_in < 3499:
        return 0.1 * total_upfront_cash_in * conversion_rate
    elif 3499 <= total_upfront_cash_in < 3999:
        return 0.125 * total_upfront_cash_in * conversion_rate
    elif total_upfront_cash_in >= 3999:
        return 0.15 * total_upfront_cash_in * conversion_rate
    else:
        return 0

def calculate_price_control_incentive(full_payment_cash_in, mrp, deal_source):
    conversion_rate = 88
    if deal_source in ["PM-Search", "PM-Social", "Organic", "Others"]:
        if mrp == 649 and full_payment_cash_in >= 449:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1199 and full_payment_cash_in >= 899:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1999 and full_payment_cash_in >= 1549:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        else:
            return 0
    elif deal_source in ["Referral", "Events", "Goldmine", "DP"]:
        if mrp == 649 and full_payment_cash_in >= 399:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1199 and full_payment_cash_in >= 799:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1999 and full_payment_cash_in >= 1429:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        else:
            return 0
    else:
        return 0

# Streamlit Interface
st.title("Incentive Calculator")

# Upfront Cash-in Section
st.header("Upfront Cash-in Incentive")
total_upfront_cash_in = st.number_input("Enter Total Upfront Cash-in (€):", min_value=0.0, step=0.01)
if st.button("Calculate Upfront Incentive"):
    upfront_incentive = calculate_cash_in_incentive(total_upfront_cash_in)
    st.success(f"Upfront Cash-in Incentive: INR {upfront_incentive:,.2f}")

# Full Payment Section
st.header("Price Control Incentive")
full_payment_cash_in = st.number_input("Enter Full Payment Cash-in (€):", min_value=0.0, step=0.01)
mrp = st.selectbox("Select MRP (€):", options=[119, 349, 649, 1199, 1999])
deal_source = st.selectbox("Select Deal Source:", options=["PM-Search", "PM-Social", "Organic", "Others", "Referral", "Events", "Goldmine", "DP"])
if st.button("Calculate Price Control Incentive"):
    price_control_incentive = calculate_price_control_incentive(full_payment_cash_in, mrp, deal_source)
    st.success(f"Price Control Incentive: INR {price_control_incentive:,.2f}")

# Additional Incentives Section
st.header("Additional Incentives")
d0_cases = st.number_input("D0 Conversion Cases >= €400:", min_value=0, step=1)
within_window_cases = st.number_input("Converted within Window Cases:", min_value=0, step=1)
self_gen_cases = st.number_input("Self Gen Referral Cases:", min_value=0, step=1)
if st.button("Calculate Additional Incentives"):
    additional_incentive = (d0_cases * 300) + (within_window_cases * 4000) + (self_gen_cases * 3000)
    st.success(f"Additional Incentives: INR {additional_incentive:,.2f}")

# Final Calculation Section
st.header("Final Incentive")
if st.button("Calculate Total Incentive"):
    total_upfront_incentive = calculate_cash_in_incentive(total_upfront_cash_in)
    total_additional_incentive = (d0_cases * 300) + (within_window_cases * 4000) + (self_gen_cases * 3000)
    total_incentive = total_upfront_incentive + price_control_incentive + total_additional_incentive
    st.success(f"Overall Total Incentive: INR {total_incentive:,.2f}")
