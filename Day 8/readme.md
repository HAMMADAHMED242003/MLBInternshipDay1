# Breast Cancer Prediction System

## Project Overview

In this project, I built a breast cancer prediction system using the Breast Cancer Wisconsin Diagnostic Dataset available in Scikit-learn. I trained a Logistic Regression model, evaluated its performance, and then used GridSearchCV to find the best hyperparameters and compare the results with the baseline model.


## What I Learned About Model Evaluation

Through this project, I learned that training a model is not enough. It is important to evaluate how well it performs on unseen data. I learned how to use different evaluation metrics such as Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix. I also understood the importance of Cross Validation and how it gives a more reliable estimate of model performance.



## Hyperparameter Tuning

I learned that hyperparameters are settings that we choose before training a model. I used GridSearchCV to try different values of C and different solvers for Logistic Regression. This helped me find the best combination of parameters automatically instead of choosing them manually.


## Best Parameters

After running GridSearchCV, the best parameters were:

* C: 10
* Solver: liblinear



## Baseline vs Tuned Model

| Metric    | Baseline Model | Tuned Model |
| --------- | -------------: | ----------: |
| Accuracy  |         95.61% |      95.61% |
| Precision |         94.59% |      94.59% |
| Recall    |         96.55% |      96.55% |
| F1-Score  |         96.55% |      96.55% |


## Key Observations

* The Logistic Regression model performed very well on this dataset.
* GridSearchCV selected C = 10** and liblinear as the best hyperparameters.
* The tuned model achieved the same accuracy as the baseline model.
* This shows that the default model was already performing well, so hyperparameter tuning did not improve the final test accuracy.
* Even though the accuracy stayed the same, GridSearchCV helped confirm the best model settings using cross-validation.


## Conclusion

This project helped me understand the complete workflow of a machine learning classification project, from loading and exploring the data to training, evaluating, and improving a model using hyperparameter tuning. It also gave me hands-on experience with Scikit-learn and different model evaluation techniques.
