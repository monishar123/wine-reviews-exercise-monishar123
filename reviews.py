import pandas as pd

# Read the dataset
data_file = 'data/winemag-data-130k-v2.csv.zip'
df = pd.read_csv(data_file)

# Group the data by country, count reviews, and calculate average points
summary_df = df.groupby('country').agg(
    count=('country', 'size'),
    points=('points', 'mean')
).reset_index()

# Round the average points to 1 decimal place
summary_df['points'] = summary_df['points'].round(1)

# Write the summary to a new CSV file
output_file = 'data/reviews-per-country.csv'
summary_df.to_csv(output_file, index=False)

print(f"Summary saved to {output_file}")

