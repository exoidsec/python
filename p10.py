# Load a dataset and perform time series analysis using pandas
# DateTime features: Extract year, month, day, weekday from
# date column, and group data by month and include monthly sales.

# Step 1: Import libraries and create sample dataset
import pandas as pd

# Sample sales data
data = {
    'date': [
        '2024-01-15', '2024-01-20', '2024-02-05',
        '2024-02-18', '2024-02-29', '2024-03-25',
        '2024-04-02', '2024-04-09', '2024-04-15',
        '2024-02-29', '2024-04-20', '2024-04-22'
    ],
    'sales': [330, 170, 420, 250, 310, 470, 390, 370, 290, 170, 560, 430]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Step 2: Convert to Datetime and Extract Components
df['date'] = pd.to_datetime(df['date'])

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.weekday # Monday = 0, Sunday = 6
df['weekday_name'] = df['date'].dt.day_name()

print("\nDataFrame with extracted datetime features:")
print(df)

# Step 3: Group by Month and Calculate Monthly Sales
monthly_sales = df.groupby('month')['sales'].sum().reset_index()
monthly_sales.columns = ['Month', 'Total Sales']

# Optional: Map month number to month name
month_names = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

monthly_sales['Month'] = monthly_sales['Month'].map(month_names)

print("\nMonthly Sales Summary:")
print(monthly_sales)

# Group by Year-Month (for multi-year data)
# If your data spans multiple years, group by both year and month
df['year_month'] = df['date'].dt.to_period('M') # e.g., 2024-01

monthly_summary = df.groupby('year_month')['sales'].agg(
    ['sum', 'mean', 'count']
).reset_index()

print("\nAdvanced: Year-Month Summary")
print(monthly_summary)
