NYC Airbnb 2019 neighborhood summary for Topic 2: Tidy vs Untidy Data

What this file is
This file is a small summary table derived from a 600 row sample of NYC Airbnb 2019 listings.
Each row corresponds to one neighborhood within a borough.

Why it is useful for Topic 2
This dataset is intentionally untidy because multiple variables are encoded in the column names.
Each column name follows the pattern:

metric__room_type

For example:
mean_price__Private_room

The goal of Topic 2 is to reshape this dataset into one or more tidy data sets and justify your choices.

Row and column counts
Rows: 15
Columns: 17

Key columns
neighbourhood_group
neighbourhood

Metrics included in the column names
mean_price
median_minimum_nights
mean_availability_365
mean_reviews_per_month
n_listings

Room type keys included in the column names
Entire_home_apt
Private_room
Shared_room

Missing values
Some borough and neighborhood combinations do not have all room types in the sample.
Those combinations appear as missing values in the wide table.

Suggested tidy targets
Tidy version A for modeling and tabular summaries
One row per neighbourhood_group, neighbourhood, room_type
Columns: mean_price, median_minimum_nights, mean_availability_365, mean_reviews_per_month, n_listings

Tidy version B for visualization across metrics
One row per neighbourhood_group, neighbourhood, room_type, metric
Columns: value
