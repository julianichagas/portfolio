# Rossmann Store Sales Prediction
## Overview
This [notebook](https://github.com/julianichagas/portfolio/blob/main/Rossmann%20Store%20Sales/Rossmann%20Store%20Sales.ipynb) project focuses on predicting the sales for each Rossmann store for the next six weeks. The purpose of this prediction is to define a budget for store renovations. To achieve this, a machine learning model was created using XGBoost Regressor. The project involves data preprocessing, exploratory data analysis (EDA), feature selection, model comparison, and hyperparameter tuning.

## Data
The data for this project was obtained from a CSV file. The dataset was cleaned and transformed to ensure its suitability for analysis.

## Exploratory Data Analysis (EDA)
EDA was conducted to gain insights into the dataset and understand the relationships between variables. This process involved various statistical and visual techniques to identify patterns, trends, and anomalies in the data.

## Feature Selection
To determine the most relevant features for the machine learning model, the Boruta algorithm was used as a feature selector. This technique helps to identify important features by comparing their importance with that of randomized shadow features.

## Model Comparison
Five regression models were evaluated and compared based on three evaluation metrics: Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), and Root Mean Squared Error (RMSE). The purpose of this comparison was to select the best-performing model for the sales prediction task. Ultimately, the XGBoost Regressor was chosen as the most suitable model.
<table class="dataframe" border="1">
  <thead>
    <tr style="text-align: right;">
      <th>Model Name</th>
      <th>MAE CV</th>
      <th>MAPE CV</th>
      <th>RMSE CV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Linear Regression</td>
      <td>2082.28 +/- 295.23</td>
      <td>0.3 +/- 0.02</td>
      <td>2956.58 +/- 467.36</td>
    </tr>
    <tr>
      <td>Linear Regression - Lasso</td>
      <td>2116.98 +/- 341.18</td>
      <td>0.29 +/- 0.01</td>
      <td>3060.24 +/- 503.67</td>
    </tr>
    <tr>
      <td>Random Forest Regressor</td>
      <td>836.15 +/- 215.92</td>
      <td>0.12 +/- 0.02</td>
      <td>1254.86 +/- 316.56</td>
    </tr>
    <tr>
      <td>XGBoost Regressor</td>
      <td>7049.17 +/- 588.63</td>
      <td>0.95 +/- 0.0</td>
      <td>7715.17 +/- 689.51</td>
    </tr>
  </tbody>
</table>

## Hyperparameter Tuning
To optimize the performance of the XGBoost Regressor, hyperparameter fine-tuning was performed using the random search technique. This involved randomly sampling a set of hyperparameters from a specified distribution and evaluating the model's performance with each combination. The goal was to find the hyperparameter configuration that resulted in the best predictive performance.

### Model Results:
<table class="dataframe" border="1">
  <thead>
    <tr style="text-align: right;">
      <th>Model Name</th>
      <th>MAE CV</th>
      <th>MAPE CV</th>
      <th>RMSE CV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>XGBoost Regressor</td>
      <td>819.93 +/- 129.04</td>
      <td>0.12 +/- 0.01</td>
      <td>1179.92 +/- 185.01</td>
    </tr>
  </tbody>
</table>

## Conclusion
The Rossmann Store Sales Prediction project utilizes machine learning techniques to forecast sales for each store. By leveraging the XGBoost Regressor and conducting comprehensive data analysis, feature selection, and model comparison, it was possible to identify the most suitable model for the task. The insights gained from this project can aid in budget allocation for store renovations and contribute to more informed business decisions.
