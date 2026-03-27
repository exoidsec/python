import pandas as pd

data = {
    'Region': [
        'North', 'South', 'East', 'West',
        'North', 'South', 'East', 'West',
        'North', 'South', 'East', 'West',
        'North', 'South'
    ],
    'Product': [
        'iPod', 'iPod', 'iPod', 'iPod',
        'VR', 'VR', 'VR', 'VR',
        'iPod', 'VR', 'iPod', 'VR',
        'Mini', 'Mini'
    ],
    'Sales': [
        2150, 1180, 3320, 2210,
        4400, 3150, 3290, 5330,
        3150, 3220, 5180, 4260,
        3500, 3470
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Sales DataFrame:")
print(df)

pivot_table = pd.pivot_table(
    data=df,
    index='Product', # Rows
    columns='Region', # Columns
    values='Sales', # Values
    aggfunc='sum', # Sum of sales
    fill_value=0 # Replace NaN with 0
)

print("\n------ Pivot Table: Product-wise Sales by Region ------")
print(pivot_table)

pivot_table1 = pd.pivot_table(
    data=df,
    index='Region',
    columns='Product',
    values='Sales',
    aggfunc='sum',
    fill_value=0
)

print("\n------ Pivot Table: Region-wise Sales by Product ------")
print(pivot_table1)

pivot_with_totals = pd.pivot_table(
    data=df,
    index='Product',
    columns='Region',
    values='Sales',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='Total'
)

print("\n------ Pivot Table with Grand Totals ------")
print(pivot_with_totals)

pivot_avg = pd.pivot_table(
    df,
    index='Product',
    columns='Region',
    values='Sales',
    aggfunc='mean',
    fill_value=0
).round(1)

print("\n------ Average Sales per Product by Region ------")
print(pivot_avg)

multi_pivot = pd.pivot_table(
    df,
    index='Product',
    columns='Region',
    values='Sales',
    aggfunc=['sum', 'count'],
    fill_value=0
)

print("\n------ Multiple Aggregations: Sum and Count ------")
print(multi_pivot)
