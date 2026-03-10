Messy? No. Trustworthy? Not automatically.

README_SubscriptionChurnClassification_Topic6.txt

File
- topic6-data.csv

Context
This dataset is a synthetic customer subscription dataset for a binary classification task.
The goal is to predict whether a customer will churn in the next 30 days.

Important idea for this activity
A classification model can look strong and still be untrustworthy.
AI can help generate code and explanations, but AI is not good at understanding your real decision context unless you tell it that context clearly.
Humans must decide:
- what the prediction target really is
- which variables are appropriate at prediction time
- which metric matters most
- whether a model is trustworthy enough to use

Rows and columns
- 650 rows
- 18 columns

Outcome variable
- churn_next_30d: Yes or No

Variable descriptions
- customer_id: customer identifier
- tenure_months: number of months the customer has been with the company
- monthly_charges: monthly bill in dollars
- contract_type: Month-to-month, One-year, or Two-year
- autopay: whether the customer uses autopay
- internet_service: Fiber, DSL, or None
- support_tickets_90d: number of support tickets in the last 90 days
- late_payments_6m: number of late payments in the last 6 months
- streaming_tv: whether the customer has streaming TV
- online_security: whether the customer has online security service
- senior: whether the customer is in a senior customer category
- region: customer region
- avg_data_gb: average monthly data use in GB
- satisfaction_score: customer satisfaction score from 1 to 10
- retention_offer_last30d: whether a retention offer was made recently
- cancellation_request_flag: whether the customer submitted a cancellation request
- exit_survey_completed: whether an exit survey was completed
- churn_next_30d: target for classification

Caution
Not every available column should automatically be used as a predictor.
Some columns may be suspicious because they may only be known after a customer has effectively decided to churn or after the churn process has already started.
Part of your job is to decide what should or should not be used in a trustworthy predictive model.

Recommended analysis habits
- Set a random seed before splitting data
- Separate training and test data
- Report more than one evaluation metric
- Compare your model to a simple baseline
- Explain your choices in plain language
- Do not assume that high accuracy means a useful model

Reminder
This activity is not about proving AI wrong.
It is about evaluating whether AI generated work is aligned, trustworthy, reproducible, and useful.
