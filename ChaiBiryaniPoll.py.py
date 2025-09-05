# LAYOUT
import streamlit as st

st.title("Biryani Taste Poll")

col1, col2 = st.columns(2)

with col1:
    biryani = st.selectbox("Select your favourite biryani", ["Hyderabadi", "Lucknowi", "Kolkata"])
    st.write(f"You selected {biryani} biryani")
    
    if biryani == "Hyderabadi":
        st.image("https://www.foodfusion.com/wp-content/uploads/2021/02/Lucknowi-biryani-Recipe-by-Food-fusion-1-300x225.jpg?v=1612346444")
    elif biryani == "Lucknowi":
        st.image("https://www.licious.in/blog/wp-content/uploads/2022/03/Licious-Holi-2022-009-1-min-1024x1024-1.jpg", width=300)
    else:
        st.image("https://images.slurrp.com/prod/recipe_images/better-butter/kolkata-style-chicken-biriyani_9SLCVPDZ5PGROGV5DJA5.webp",width=300)




with col2:
    rating = st.slider("Rate the biryani", 1, 5, 3)
    st.write(f"You rated {biryani} {rating} out of 5")

st.divider()

st.title("Chai Taste Poll")
col3, col4 = st.columns(2)
with col3:
    st.header("Masala Chai")
    st.image("https://media.gettyimages.com/id/1141990365/photo/masala-chai-tea.jpg?s=612x612&w=gi&k=20&c=Ejn6uESTVEAumUf71mV8stc6CIeX1A69vBaAksz_GKc=", width=300)
    vote_masala = st.button("Vote for Masala Chai")
    if vote_masala:
        st.success("Thanks for voting Masala Chai")

with col4:
    st.header("Adrak Chai")
    st.image("https://swachhtea.com/cdn/shop/files/1_13f36ba5-a4bd-47bd-b588-484f0ac3cbbf_1080x.jpg?v=1719233375", width=200)

    vote_adrak = st.button("Vote for Adrak Chai")
    if vote_adrak:
        st.success("Thanks for voting Adrak Chai")        

name = st.sidebar.text_input("Please enter your name")
biryani_name = st.sidebar.selectbox("Please enter your favrourite biryani", ["Hyderabadi", "Lucknowi", "Malabar"])
tea_name = st.sidebar.selectbox("Please enter your favrourite tea", ["Masala", "Adrak", "Elaichi"])
st.sidebar.write(f"Hello {name}, you like {biryani_name} biryani and {tea_name} tea")

with st.expander("Show Chai Making Inastructions"):
    st.write("""
    1. Boil water
    2. Add tea leaves
    3. Add ginger and masala
    4. Add milk and sugar
    5. Strain and serve hot
    """)

st.markdown('### WELCOME TO CHAI AND BIRYANI POLL APP')
    

