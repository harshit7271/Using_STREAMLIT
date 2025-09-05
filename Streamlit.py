import streamlit as st
st.title("My first streamlit webpage")
st.subheader("Select your colour")
st.text("three options are available")
st.write("Select your favourite colour from the dropdown")

colour = st.selectbox("Your fav colour:",["Red", "Green","Blue"])
st.write(f"Your fav colour is {colour}. And good choice")
st.success("Your colour has been selected")









st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your chai is being bwred")

add_masala = st.checkbox("Add masala")
if add_masala:
    st.write("Masala added")

tea_type = st.radio("Select your type of tea", ["Ginger", "Elaichi", "Normal"])
st.write(f"You have selected {tea_type} tea")
flavour = st.selectbox("Select flavour", ["Sweet", "Less Sweet", "Normal"])

st.slider("Select sugar level", 0, 10, 5)

st.number_input("Enter number of cups", 1, 10, 1)
st.write(f"You have selected {flavour} flavour tea")

name = st.text_input("Please enter your name")
if name:
    st.write(f"Hello {name}, your {tea_type} with {flavour} flavour is being brewed")

dob = st.date_input("Enter your date of birth")
st.write(f"Your date of birth is {dob}")    
