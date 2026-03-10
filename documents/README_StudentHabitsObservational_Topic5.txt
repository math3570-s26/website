README for topic5-data.csv
AI Activity 5: Correlation, Regression, and Overinterpretation

Dataset title
Synthetic student habits and exam outcomes dataset

Purpose of this dataset
This dataset is designed for an activity about correlation, regression, interpretation, and overclaiming.
It is intentionally built so that:
- some overall associations look stronger than the within-group story
- at least one influential observation can affect the regression line
- not every relationship is well summarized by a simple straight line
- causal language would be inappropriate without stronger evidence

Important context
This is an observational dataset, not an experiment.
Students were not randomly assigned to different values of study time, sleep, caffeine, stress, or attendance.
Because of that, associations in this file should not be automatically interpreted as causal effects.

Rows and columns
- 210 rows
- 10 columns

Variables
- student_id: synthetic student ID
- section: course section label
- prior_gpa: prior GPA before the course
- study_hours_week: self reported weekly study hours for this course
- attendance_pct: percent of class meetings attended
- sleep_hours: average sleep hours per night during the exam period
- caffeine_mg_day: average daily caffeine intake in milligrams during the exam period
- stress_score: self reported stress score on a 1 to 10 scale
- practice_quiz_avg: average practice quiz score
- final_exam_score: final exam score out of 100

Recommended main variables for the required activity
- Response variable: final_exam_score
- Predictor variable: study_hours_week
- Context variable for grouped checking: section
- Optional secondary variable for checking a different pattern: sleep_hours or caffeine_mg_day

Why this dataset is useful for this activity
A simple correlation or regression output can sound convincing, especially if AI describes it confidently.
But careful human checking is still needed for questions such as:
- Is the language causal when the data are observational?
- Does one overall relationship hide section differences?
- Is the interpretation too strong for the evidence?
- Is the line influenced by unusual observations?
- Is a linear summary reasonable for the chosen variables?

Suggested software ideas
You may use R or Python.
Useful tasks include:
- scatterplots
- grouped scatterplots colored by section
- correlation calculation
- simple linear regression
- residual plots
- influence checks such as leverage, standardized residuals, or Cook's distance

Reminder
Do not treat a strong correlation as proof of cause.
Do not treat a fitted line as the whole story without checking the data visually.
