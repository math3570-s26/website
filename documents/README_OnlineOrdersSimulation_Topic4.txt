topic4-population.csv
Synthetic online orders delivery population for AI Activity 4

Purpose
This file is a complete finite population for a simulation activity about probabilistic and statistical simulation.
Students should treat the file as the full population, not as a sample.

Why this file is useful for simulation
Because the full population is known, students can:
1. compute population truths directly
2. design a simulation that matches the data generating process
3. compare simulated results to known benchmarks
4. catch common AI mistakes such as simulating the wrong event, using the wrong sampling rule, or confusing data variability with Monte Carlo variability

Suggested focus variables
- late_delivery: Yes or No
- delay_days: actual_days minus promised_days
- rush_order, fragile, carrier, warehouse: context variables that may tempt AI to overcomplicate the task
- order_value_usd: optional context variable

Recommended required simulation tasks
1. Probability simulation
Estimate the probability that a simple random sample of 20 orders, drawn WITHOUT replacement from this population, contains at least 9 late deliveries.

2. Statistical simulation
Study the sampling distribution of p-hat for late deliveries under repeated simple random samples WITHOUT replacement from this population.
Recommended sample sizes: n = 20 and n = 60.

Important teaching point
A very common AI mistake is to answer a nearby but different question, such as:
- simulating with replacement instead of without replacement
- using a binomial model automatically without checking whether it matches the sampling process
- simulating a single sample instead of many repeated samples
- reporting a simulated proportion without comparing it to the known population truth
- ignoring Monte Carlo error or replication stability

Variables
- order_id: unique order identifier
- warehouse: fulfillment warehouse
- region: customer region
- carrier: shipping carrier
- rush_order: Yes or No
- fragile: Yes or No
- promised_days: promised delivery time in days
- actual_days: actual delivery time in days
- late_delivery: Yes if actual_days > promised_days, otherwise No
- order_value_usd: order value in US dollars
- delay_days: actual_days - promised_days
- high_value: Yes if order_value_usd >= 120, otherwise No

Basic file facts
- rows: 300
- columns: 12

Instructor note
This is a synthetic dataset created for teaching. The values are realistic enough for simulation practice, but they do not represent a real company.
