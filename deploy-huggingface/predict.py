import streamlit as st
import pandas as pd
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load('best_random_forest_model.pkl')

model = load_model()

# Function to predict rating based on user input
def predict_rating(loves_count, reviews, ingredients, price_usd, child_count, primary_category, new, online_only, limited_edition, out_of_stock, sephora_exclusive):
    # Data sesuai format model
    new_data = pd.DataFrame([[
        loves_count, reviews, ingredients, price_usd, child_count, primary_category,
        new, online_only, limited_edition, out_of_stock, sephora_exclusive
    ]], columns=[
        'loves_count', 'reviews', 'ingredients', 'price_usd', 'child_count', 'primary_category',
        'new', 'online_only', 'limited_edition', 'out_of_stock', 'sephora_exclusive'
    ])
    
    return model.predict(new_data)[0]

def run():
    st.title("Skincare Product Rating Prediction")
    
    with st.form("prediction_form"):
        # Create two columns for the layout
        col1, col2 = st.columns(2)

        with col1:
            # User inputs for column 1
            loves_count = st.number_input(
                "Number of Loves", 
                min_value=0, 
                help="The number of people who have marked this product as a favorite."
            )

            reviews = st.number_input(
                "Number of Reviews", 
                min_value=0, 
                help="The number of user reviews for this product."
            )

            ingredients = st.number_input(
                "Number of Ingredients", 
                min_value=0, 
                help="The number of ingredients included in the product."
            )

            price_usd = st.number_input(
                "Product Price (USD)", 
                min_value=0, 
                help="The price of the product in USD."
            )

            primary_category = st.selectbox(
                "Primary Category", 
                ["Facial Cleanser", "Moisturizer", "Serum", "Sunscreen", "Toner"],
                help="The main category of the product."
            )
            
            child_count = st.number_input(
                "Number of Child Products", 
                min_value=0, 
                help="The number of variations available for the product."
            )


        with col2:
            # User inputs for column 2
            new = st.selectbox(
                "New Product?", 
                ["Yes", "No"], 
                help="Indicates whether the product is new or not."
            )

            online_only = st.selectbox(
                "Online Only?", 
                ["Yes", "No"], 
                help="Indicates whether the product is only sold online."
            )

            limited_edition = st.selectbox(
                "Limited Edition?", 
                ["Yes", "No"], 
                help="Indicates whether the product is a limited edition."
            )

            out_of_stock = st.selectbox(
                "Out of Stock?", 
                ["Yes", "No"], 
                help="Indicates whether the product is currently out of stock."
            )

            sephora_exclusive = st.selectbox(
                "Sephora Exclusive?", 
                ["Yes", "No"], 
                help="Indicates whether the product is exclusive to Sephora."
            )

            # Submit button in the second column
            submitted = st.form_submit_button("Predict")
            
            if submitted:
                # Convert inputs
                new = 1 if new == "Yes" else 0
                online_only = 1 if online_only == "Yes" else 0
                limited_edition = 1 if limited_edition == "Yes" else 0
                out_of_stock = 1 if out_of_stock == "Yes" else 0
                sephora_exclusive = 1 if sephora_exclusive == "Yes" else 0

                # Predict the rating
                rating_prediksi = predict_rating(
                    loves_count, reviews, ingredients, price_usd, child_count, primary_category,
                    new, online_only, limited_edition, out_of_stock, sephora_exclusive
                )
                st.success(f"Predicted Rating: {rating_prediksi:.2f}")

# Run the app
if __name__ == "__main__":
    run()
