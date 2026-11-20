# TensorFlowed: Spaceship Titanic

TensorFlowed is a student data science project based on Kaggle's **Spaceship Titanic** competition. We used passenger information to predict whether each passenger was transported to another dimension after a fictional space-time anomaly.

Our project demonstrates an end-to-end machine learning workflow, including data exploration, missing-value handling, feature engineering, model training, validation, visualization, and Kaggle submission preparation.

## Project highlights

- Explored passenger outcomes and relationships between variables
- Created features from cabin information, passenger groups, age, and spending
- Prepared categorical and numerical data for modeling
- Compared Logistic Regression, Random Forest, and XGBoost
- Evaluated models using validation results
- Created interactive visualizations for our final presentation
- Built an interactive Streamlit website to showcase our work

## Interactive frontend

The frontend is a Streamlit website with three main areas:

- **Mission Control:** Project overview, pipeline summary, and key project metrics
- **Data Explorer:** Interactive charts organized into Outcomes, Passenger Patterns, Spending, and Relationships
- **Model Arena:** Comparison of the models tested during the project

## Running the website locally

From the repository root, navigate to the frontend folder:

```bash
cd Website
```

Install the required packages:

```bash
python3 -m pip install -r requirements.txt
```

Start the Streamlit app:

```bash
python3 -m streamlit run app.py
```

The website will open in a browser. Use the sidebar to upload the competition files:

- `train.csv`
- `test.csv`
- An optional model comparison CSV containing `Model` and `Validation Accuracy` columns
- An optional final submission CSV

The competition data is not included in this repository. It can be downloaded from the [Spaceship Titanic Kaggle competition](https://www.kaggle.com/competitions/spaceship-titanic).

## Machine learning workflow

The project followed these general steps:

1. Understand the competition and passenger-level dataset
2. Explore the target variable and input features
3. Investigate missing values and categorical variables
4. Engineer features such as cabin deck, cabin side, group size, age group, and total spending
5. Preprocess the data for machine learning
6. Train and compare classification models
7. Evaluate model performance using a validation split
8. Generate predictions and prepare a Kaggle submission

## Team

TensorFlowed was created by:

- Hasti Abbasi Kenarsari — Team Lead, Computer Science and Data Science
- Athalia Zhou — Computer Science
- Jaqueline Lopez — Applied Mathematics
- Thuy An Nguyen — Computer Science
- Mari Astillero — Computer Science

## Tools

- Python
- pandas
- NumPy
- scikit-learn
- XGBoost
- Plotly
- Streamlit
- Jupyter Notebook and Google Colab
- Kaggle

## What we learned

This project helped us apply the complete machine learning process, from exploring and preparing data to engineering features, training models, and evaluating predictions. We also gained experience collaborating on a data science project and communicating our findings through visualizations and an interactive showcase.
