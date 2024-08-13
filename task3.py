import pandas as pd

# Load the dataset
df = pd.read_csv('zoo_animals.csv')

# Sort animals by cost to feed in descending order
df_sorted = df.sort_values(by='Cost_to_Feed', ascending=False)

# Select the top animals to remove to save costs while keeping 20 animals
animals_to_remove = df_sorted.iloc[20:]

# Output the species that should be removed
print("To minimize feeding costs, consider removing the following animals:")
print(animals_to_remove[['Species', 'Cost_to_Feed']])
