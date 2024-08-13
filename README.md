# Zoo Management Challenge

## Task 1: Which Animal Lives the Longest?

**Description**:  
The zoo management team needs to identify which animal species has the longest lifespan. This information is crucial for planning long-term care and resources for the animals. Your task is to analyze the provided dataset and determine which animal species lives the longest.

**Instructions**:

- You will be given a dataset that includes various animal species and their lifespans.
- Write a function to find the animal species with the maximum lifespan.
- Your function should output the name of the species that lives the longest.

**Code Snippet**:
```
# Example dataset
animals = [
    {"species": "Lion", "lifespan": 20},
    {"species": "Elephant", "lifespan": 70},
    {"species": "Giraffe", "lifespan": 25}
]

# Task: Find the animal with the longest lifespan
def longest_living_animal(animals):
    max_lifespan_animal = max(animals, key=lambda x: x['lifespan'])
    return max_lifespan_animal['species']

print(longest_living_animal(animals))  # Output: "Elephant"
```
## Task 2: Which Animal Costs the Most to Feed?

**Description**:  
Feeding costs are a significant part of the zoo's budget. The zoo wants to know which animal species is the most expensive to feed. This task will help in budgeting and cost management. Your task is to determine which species costs the most to feed, taking into account the gender differences in feeding costs.

**Instructions**:

- You will receive a dataset containing the daily feeding costs for different animal species, broken down by gender.
- Write a function that calculates which species has the highest daily feeding cost.
- Your function should return the species that costs the most to fee

```
# Example dataset
feeding_costs = [
    {"species": "Lion", "gender": "Male", "cost_to_feed": 50},
    {"species": "Elephant", "gender": "Female", "cost_to_feed": 30},
    {"species": "Giraffe", "gender": "Male", "cost_to_feed": 40}
]

# Task: Find the species that costs the most to feed
def most_expensive_to_feed(feeding_costs):
    max_cost_species = max(feeding_costs, key=lambda x: x['cost_to_feed'])
    return max_cost_species['species']

print(most_expensive_to_feed(feeding_costs))  # Output: "Lion"

```
