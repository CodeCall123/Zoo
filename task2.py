import pandas as pd

# Load the dataset
df = pd.read_csv('zoo_animals.csv')

# Find the animal with the highest feeding cost
most_expensive_animal = df.loc[df['Cost_to_Feed'].idxmax()]

# Output the result
print(f"The most expensive animal to feed is: {most_expensive_animal['Species']} ({most_expensive_animal['Gender']}) with a daily cost of ${most_expensive_animal['Cost_to_Feed']:.2f}.")
