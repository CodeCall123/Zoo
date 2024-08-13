import pandas as pd

# Load the dataset
df = pd.read_csv('zoo_animals.csv')

# Calculate the time to finish a quarter mile (0.25 miles or 0.4 km)
# Time = Distance / Speed
df['Time_to_Finish'] = 0.4 / (df['Speed'] / 60)  # Speed in km/h converted to km/min

# Find the fastest animal
fastest_animal = df.loc[df['Time_to_Finish'].idxmin()]

# Output the result
print(f"The fastest animal over a quarter mile is: {fastest_animal['Species']} with a time of {fastest_animal['Time_to_Finish']:.2f} minutes.")
