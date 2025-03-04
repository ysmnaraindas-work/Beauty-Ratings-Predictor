import streamlit as st
import pandas as pd

def run():
    st.title("Sephora Skincare Product Rating Analysis")
    st.image("https://images.ctfassets.net/afluk6wxa60f/4moe80ZukgKYcEisAIscsK/86a0ae253336642825ca718022a7530a/Sephora-1600x300-desktop-evergreen.jpg")
    
    st.markdown("""
    ## **Introduction**
    
    Welcome to the Skincare Product Rating Prediction tool. This model predicts product ratings based on various factors such as product features, price, category, and customer reviews. With insights drawn from extensive data analysis, this tool helps you understand what drives customer satisfaction and how to improve your product offerings.

    ## **Key Insights**

    Our analysis has highlighted several important factors that influence product ratings:      
    - **Product Category:** Products in categories like facial skincare and haircare tend to receive higher ratings than makeup products.
    - **Number of Reviews:** Products with more than 500 reviews generally have higher ratings, suggesting that customer engagement impacts overall satisfaction.
    - **Product Features:** Features like being a "new product" or "Sephora Exclusive" can positively affect ratings, as customers are drawn to the latest and exclusive items.

    ## **Best Performing Model**

    Our best-performing model, **Random Forest**, accurately predicts ratings based on these factors, achieving reliable performance even with complex data structures. Through hyperparameter tuning, we have optimized the model to improve prediction accuracy.
    """)

    # Displaying the data table
    st.markdown("""
    ## **Product Data Table**

    Below is a sample of the dataset used for predicting product ratings. It contains various features such as product category, number of reviews, price, and product ratings.
    """)

    # Example: Replace this with the actual dataset you're working with
    data = pd.read_csv('product_info.csv')

    st.dataframe(data)

# Run the app
if __name__ == "__main__":
    run()
