import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Function to load data
def load_data():
    # Replace with your dataset path
    data = pd.read_csv('product_info.csv')
    return data

# Main function
def run():
    st.title("Exploratory Data Analysis (EDA)")

    # Load Data
    data = load_data()

    # **TOP SECTION**
    st.write("## Data Filter")
    rating_filter = st.slider('Select Minimum Rating:', 1.0, 5.0, 3.0, step=0.1)
    filtered_data = data[data['rating'] >= rating_filter]
    st.write(f"### Products with Rating >= {rating_filter}")
    st.dataframe(filtered_data)

    # **BOTTOM SECTION (3 Columns)**
    st.write("## Data Visualization")
    col1, col2, col3 = st.columns(3)

    # **Column 1: Distribution of Products by Main Category**
    with col1:
        st.write("### Distribution of Products")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(data=filtered_data, y='primary_category', palette='viridis', ax=ax)
        ax.set_facecolor("none")  # Transparent
        st.pyplot(fig)

    # **Column 2: Rating vs Price (Updated)**
    with col2:
        st.write("### Rating vs Price")
        
        # Create scatter plot using seaborn
        fig, ax = plt.subplots(figsize=(8, 5.3))
        sns.scatterplot(data=filtered_data, x='price_usd', y='rating', hue='primary_category', palette='viridis', ax=ax)
        
        # Set title and transparent background
        ax.set_facecolor("none")  # Transparent
        ax.set_xlabel("Price (USD)")
        ax.set_ylabel("Rating")
        
        # Display plot
        st.pyplot(fig)

    # **Column 3: Average Rating by Main Category**
    with col3:
        st.write("### Average Rating")
        avg_rating = (
            filtered_data.groupby('primary_category', as_index=False)['rating']
            .mean()
            .sort_values(by='rating', ascending=False)
        )
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(data=avg_rating, x='rating', y='primary_category', palette='viridis', ax=ax)
        ax.set_facecolor("none")  # Transparent
        st.pyplot(fig)

    # **Conclusion Section**
    st.write("## Conclusion")

    st.markdown("""
    Based on the exploratory data analysis, we can conclude the following:
    
    - **Product Category**: Popular product categories like facial skincare tend to have more reviews and customer attention, which may influence the rating.
    - **Price vs Rating**: Price does not always correlate directly with ratings. However, higher-priced products may slightly receive higher ratings.
    - **Product Categories with Higher Ratings**: Categories with higher average ratings provide valuable insights for the company to focus on improving quality and product development within those categories.
    """)

# Run the application
if __name__ == "__main__":
    run()
