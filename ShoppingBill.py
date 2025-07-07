import streamlit as st

st.title("🧾 Total Cost Calculator with Tax")

# Input for item prices
item1 = st.number_input("Enter price of Item 1", min_value=0.0, format="%.2f")
item2 = st.number_input("Enter price of Item 2", min_value=0.0, format="%.2f")
item3 = st.number_input("Enter price of Item 3", min_value=0.0, format="%.2f")

# Input for tax percentage
tax_percent = st.number_input("Enter Tax Percentage (%)", min_value=0.0, format="%.2f")

# Calculate total
subtotal = item1 + item2 + item3
tax_amount = subtotal * (tax_percent / 100)
total = subtotal + tax_amount

# Show results
st.write(f"Subtotal: ₹{subtotal:.2f}")
st.write(f"Tax Amount: ₹{tax_amount:.2f}")
st.success(f"Total Cost (including tax): ₹{total:.2f}")
