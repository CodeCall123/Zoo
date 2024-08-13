import pandas as pd

# Load the dataset
df = pd.read_csv('zoo_animals.csv')

# Find the animal with the longest lifespan
longest_living_animal = df.loc[df['Lifespan'].idxmax()]

# Output the result
print(f"The animal that lives the longest is: {longest_living_animal['Species']} with a lifespan of {longest_living_animal['Lifespan']} years.")
