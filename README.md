<a name="top"></a>

# Why Are Customers Churning

by Martin Reyes

<!-- <p>
  <a href="https://github.com/martin-reyes" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/128/3291/3291695.png" alt="GitHub" width="40" height="40">
  </a>

  <a href="https://www.linkedin.com/in/martin-reyes-ds/" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/128/3536/3536505.png" alt="LinkedIn" width="40" height="40">
    </a>
</p>
 -->

## Project Description

23% of current customers on record have churned. In this project, we will aim to find drivers in customer churn by  exploring data acquired on our MySQL database. We will explore features both individually and relative to customer churn status. We will take these insights, present them, and use them to create machine learning models to predict whether a customer churns. After evaluating the models with metrics that address our goals, we will use the models to come up with recommendations and predictions on churningn customers.

 
## Project Goal
 
* Discover drivers of customers churning and other key insights.
* Use main drivers to develop a machine learning model to predict churning customers.
* Use insights and model evaluation to identify features to address when a customer is predicted to churn.

 
## Initial Thoughts
 
My initial hypothesis is our demographic features, gender and senior citizen status, will not relate to churn while our numerical features (tenure, monthly charges, and total charges) will.
 
## The Plan
 
* **Acquire** data from MYSQL
 
* **Prepare** data. 
    1. Inspect raw data and note any desired transformations which may include any of the following:
        * Drop unnecessary columns (duplicate, redundant columns)
        * Numeric columns should be numeric data types
        * Handle missing values and impute appropriate values
            * check for explicit missing values (e.g. `np.nan`)
            * check for implicit missing values (e.g. whitespace, `'unknown'`, etc.)
        * Deal with any duplicate rows
        * Address and encode categorical columns
            * one-hot encode unordered categorical columns
            * label encode ordered categorical columns  
    1. Inspect clean data
        * Ensure data is tidy:
            * one value per cell
            * each observation is one and only one row
            * each feature is one and only one column
    1. Split the data
        * Determine if target column has class imbalance. If, so stratify.
        * We will do 70/15/15 train/validate/test split.
        * **RANDOM_STATE will be 125**
    1. Create data dictionary
    1. Summarize data transformations

* **Explore** data in search of features that drive churn
   1. General Inspect
       - `.info()` and `.describe()`
       - identify continuous and categorical columns
   1. Univariate Stats: 
       - Categorical
       - Nunerical
   1. Bivariate Stats:
       - Categorical features to target relationships
       - Continuous features to target relationship
   1. Use these quick insights to ask and answer specific questions:
       - Which features appear to relate to churn the most?
      
* Develop a **model** to predict if a customer will churn
   * Use drivers identified in explore to build predictive models of different types
   * Create and run a baseline model with `sklearn`'s `DummyClassifier` to compare our results to
   * Create and run KNN, Logistic Regression, and Decistion Tree classification models
   * Use the insights from the highest-performing model (with highest test accuracy) to confirm our initial hypotheses and insights on the features that are the biggest drivers of churn
   
* **Evaluate** models on train and validate data
   * Identify the metric to maximize
       * Do we simply want an accurate model?
       * If not is it more costly to incorrectly identify non-churning customers (FN) or churning customers (FP)?
   * Select the best model based on highest desired metric

* Evaluate the best model on validation data set. After we find the best model, test on the test set.
    * Save test predictions to a csv file
 
* Draw conclusions
 
 
<a name="data-dictionary"></a>
## Data Dictionary

| Feature              | Definition |
|:----------------------|:-------------------- |
| customer_id          | Unique identifier for each customer |
| gender_male          | Indicates whether the customer is male or not |
| senior_citizen       | Indicates whether the customer is a senior citizen or not |
| partner              | Indicates whether the customer has a partner or not |
| dependents           | Indicates whether the customer has dependents or not |
| tenure               | Number of months the customer has been with the company |
| phone_service        | Indicates whether the customer has phone service or not |
| multiple_lines       | Indicates whether the customer has multiple lines for phone |
| online_security      | Indicates whether the customer has online security service or not |
| online_backup        | Indicates whether the customer has online backup service or not |
| device_protection | Indicates whether the customer has device protection service or not|
| tech_support         | Indicates whether the customer has tech support service or not|
| streaming_tv         | Indicates whether the customer has streaming TV service or not|
| streaming_movies   | Indicates whether the customer has streaming movies service or not|
| paperless_billing  | Indicates whether the customer has opted for paperless billing or not|
| monthly_charges      | The amount charged to the customer on a monthly basis |
| total_charges        | The total amount charged to the customer over the entire tenure |
| churn (**target**)      | Indicates whether the customer has churned (cancelled the service) or not |
| contract_type   | The type of contract the customer has (e.g., month-to-month, one-year, two-year)|
| internet_service_type| The type of internet service the customer has (e.g., DSL, fiber optic, None) |
| payment_type      | The method of payment used by the customer (e.g., electronic check, credit card, bank transfer, mailed check) |
|Additional Features|Encoded and values for categorical data|

 
## Steps to Reproduce
1. Clone this repo.
2. To acquire data, ensure env.py file is in local repo with MySQL credentials, or [telco_churn_raw.csv](data/telco_churn_raw.csv) is in the data folder.
3. Run through notebooks to produce results.
 
## Summary
Key Insights:
- Strong Drivers of Churn:
    - Tenure
        - Churners have a shorter tenure
    - Internet Service Type
        - Churners largely have fiber optic internet
    - Contract Type
        - Churners are largely on month-to-month contracts
        - Churners are rarely on twy-year contracts
    - Payment by Electronic Check
        - Churners typically pay by electronic check
        
We were able to outperform our baseline accuracy of 73% by fitting a logistic regression classifier and getting an 80.5% accuracy.


## Recommendations
* With most churning customers leaving in the first few months, we should take action early to prevent churn.
    * We can take low-cost actions like reaching out and offering a survey of customer satisfaction.
    * We can consider higher-investment actions like offering promotions or early discounts
* Take similar action to encourage customers to go on a one or two year contract rather than month-to-month.
* We should see why those with fiber-optic cable churn more than others.
    * Is this cost related? (look into monthly charges) 
    * How does out fiber-optic cable perform?

## Next Steps
With more time, we can:
- Do Multivariate analysis and see how a combination or columns relate to churn 
- Develop a better-performing model by feature engineering, feature scaling, running other ML classifiers, etc.
- If we want to take action with any of the recommendations, we can change our performance metric to precision or recall, and predict and target customers this way.

[Back to top](#top)