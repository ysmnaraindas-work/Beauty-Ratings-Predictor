# Beauty Ratings Predictor: Insights from Sephora Reviews

## **Project Overview**
This project focuses on analyzing and predicting the ratings of skincare products on Sephora. The analysis considers various factors such as price, active ingredients, brand name, and product categories to understand what drives customer satisfaction. The project utilizes machine learning models like **Random Forest Regressor** to make predictions based on historical review data.

## **Key Features**
- **Data Analysis**: Cleaning and processing Sephora skincare product data.
- **Rating Prediction**: Using machine learning models to predict product ratings.
- **Feature Engineering**: Encoding categorical features and handling missing values.
- **Technology Stack**:
  - Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
  - Jupyter Notebooks
  - Random Forest Regressor
  - Data Cleaning & Feature Engineering

## **Dataset**
- `product_info.csv`

## **How to Run the Project**
1. Clone this repository:
   ```bash
   git clone https://github.com/username/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook SephoraRatingReview.ipynb
   ```

## **Directory Structure**
```
Beauty_Ratings_Predictor/
├── deploy-huggingface/
│   ├── README.md
│   ├── app.py
│   ├── best_random_forest_model.pkl
│   ├── eda.py
│   ├── home.py
│   ├── predict.py
│   ├── product_info.csv
│   ├── requirements.txt
├── README.md
├── SephoraRatingReview.ipynb
├── SephoraRatingReview_inf.ipynb
├── best_random_forest_model.pkl
├── product_info.csv
```

## **Results and Insights**
- **Main Factors Influencing Ratings:** Product category, number of reviews, and product popularity significantly influence ratings.
- **Best Model:** **Gradient Boosting Regressor** showed the best performance with an **MAE** of **0.3442** and an **R²** of **0.1233**.
- **Business Recommendations:** Focus on popular product categories, increase the number of reviews, and ensure product availability to improve ratings.

## **Project Link**
- **SephoraSkincareRating on Hugging Face:** [Project Link](https://huggingface.co/spaces/yasminenaraindas/SephoraSkincareRating)

## **Contact**
For any inquiries, reach out via [LinkedIn](https://www.linkedin.com/in/yasminenaraindas-setiadi/) or email at ysmnaraindas.work@gmail.com.

---
⭐ Don't forget to star this repository if you found it useful!

