+++++++++++++++++++++++++++++++++++++++++++++++
+ NYC Airbnb Open Data (2019) for Topic 1     +
+++++++++++++++++++++++++++++++++++++++++++++++

===============================================
Files included
===============================================
1) insideairbnb_nyc_2019_listings_messy_600.csv
   The same 600 rows, but modified for teaching. It intentionally includes common data importing pitfalls.


===============================================
Data source and attribution
===============================================
The underlying dataset is the NYC Airbnb Open Data 2019 listings dataset (commonly distributed as AB_NYC_2019.csv).
It is derived from Inside Airbnb open data.


===============================================
What was modified in the messy file
===============================================
The messy file is designed to create reasonable, meaningful auditing work during data import.
Examples of issues included:
- price: sometimes formatted as currency text (such as $1,200, USD 149, or '149 dollars')
- last_review: mixed date formats (such as 2019-06-22, 6/22/19, Jun 22, 2019) and multiple missing value tokens (NA, N/A, blank, '.', 'unknown')
- reviews_per_month: decimal comma (0,21), textual values (~0.21, '0.21 per mo'), and multiple missing tokens
- minimum_nights and availability_365: numeric values mixed with units (such as '2 nights' or '96 days')
- room_type and neighbourhood_group: inconsistent capitalization and extra whitespace
- latitude and longitude: numeric values mixed with trailing spaces
- host_name: occasional extra whitespace and a few non visible characters


===============================================
Recommended use in your Topic 1 activity
===============================================
1) Import the data and record the parsing messages and inferred column types
2) Identify hidden assumptions (for example, currency, dates, missing values, and units)
3) Propose and justify a cleaning plan, then implement it
4) Validate the result using checks that are appropriate for the context (ranges, missingness, type checks, and summary comparisons)

