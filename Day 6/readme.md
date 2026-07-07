## What I Learned About Data Preprocessing
1. I learned how to encode categorical data using One-Hot Encoding and label encoding.
2. I created a new Average_Score column to use as the target variable.
3. I learned how to split the data into training and testing sets.
4. I learned how to apply feature scaling using StandardScaler and understood why it should be applied after the train-test split to avoid data leakage.

## Why Train-Test Splitting is Important

Train-test splitting helps evaluate the model on unseen data. It prevents the model from memorizing the training data and shows how well it can make predictions on new data.

## Evaluation Metrics Used

I used the following evaluation metrics:

1. Mean Absolute Error (MAE)
2. Mean Squared Error (MSE)
3. R² Score

## Model Performance and Observations

The model achieved:
1. MAE: 0.0
2. MSE: 0.0
3. R² Score: 1.0

Initially, I thought there was a mistake because the predicted values were exactly the same as the actual values. Later, I understood that this happened because the target column (Average_Score) was created directly from the same subject marks used as input features. Therefore, the Linear Regression model was able to learn the exact relationship and make perfect predictions.