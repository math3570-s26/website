README_MessyRetailOrders_Topic3.txt

Dataset title
Messy Retail Orders and Returns Dataset

Purpose
This synthetic dataset was created for AI Activity 3 in MATH/COSC 3570.
It is designed to support practice with data cleaning, wrangling, and visualization.
The file is intentionally messy. Students should not assume that column types, missing values, categories, dates, or repeated IDs are already clean.

Context
The file is a raw export from a fictional retail business covering orders from January 2025 through July 2025.
Each row is intended to represent one extracted transaction line from the raw export.
Because this is a raw extract, some rows may be duplicated exactly, while some repeated order IDs may reflect multi-line orders rather than errors.
Students should inspect carefully before deciding what to remove, keep, or combine.

Learning goal
The main goal is not simply to make a plot.
The goal is to show that quick AI-generated code can produce a polished but misleading visualization when the underlying data are dirty.

File included
- topic3-data.csv

Dimensions
- 480 rows
- 15 columns

Column descriptions
1. order_id
   Order identifier. Repeated values may occur.
2. order_date
   Date the order was placed.
3. ship_date
   Date the order was shipped.
4. region
   Geographic region.
5. city
   City linked to the order.
6. category
   Main product category.
7. subcategory
   Product subcategory.
8. sales_channel
   How the order was placed.
9. customer_type
   Type of customer.
10. quantity
   Quantity ordered.
11. unit_price
   Unit price for the line item.
12. discount
   Discount applied to the line item.
13. revenue
   Revenue recorded for the line item.
14. returned
   Return flag or return status.
15. notes
   Free-text operational note. This column may be useful for inspection but is not required for analysis.

Important cautions
- Do not assume the date columns use one consistent format.
- Do not assume numeric columns are already numeric.
- Do not assume one missing-value code is used everywhere.
- Do not assume repeated order_id means the row is a duplicate.
- Do not assume labels such as region, category, sales_channel, and customer_type are standardized.
- Do not assume a quick plot from the raw file is trustworthy.

Suggested visualization directions
Students may choose one main question such as:
- How does monthly revenue vary by sales channel?
- How does total revenue vary across categories or regions?
- How do return rates differ by customer type or category?
- Which categories appear most important before and after cleaning?

A strong project will compare:
1. a naive or minimally cleaned plot, and
2. a corrected plot built from a documented cleaning and wrangling pipeline.

What not to do
- Do not trust AI suggestions without checking the raw values.
- Do not report a final plot without showing what cleaning decisions affected it.
- Do not drop rows automatically without explaining why.

Instructor note
This dataset is synthetic and was designed for pedagogy, not for real business inference.
