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
## Task 3: Which Animals Should Be Removed to Save Costs?

**Description**:  
The zoo is facing budget cuts and needs to reduce feeding costs while ensuring that at least 20 animals remain in the zoo. Your task is to identify which animals should be removed to save the most money, keeping the total number of animals at or above 20.

**Instructions**:

- You will be provided with a list of animals and their daily feeding costs.
- Write a function that selects the animals that should be removed to minimize feeding costs while maintaining a population of at least 20 animals.
- Your function should return a list of species that should be removed.
```
# Example dataset
animals_to_remove = [
    {"species": "Lion", "cost_to_feed": 50},
    {"species": "Elephant", "cost_to_feed": 70},
    {"species": "Giraffe", "cost_to_feed": 40},
    {"species": "Zebra", "cost_to_feed": 30},
    {"species": "Panda", "cost_to_feed": 60}
]

# Task: Select animals to remove to minimize costs while keeping 20 animals
def animals_to_remove_for_savings(animals, total_animals=20):
    animals.sort(key=lambda x: x['cost_to_feed'], reverse=True)
    # Logic to select animals while ensuring at least 20 animals remain
    # This is a simplified example, actual implementation will depend on the total number of animals
    return [animal['species'] for animal in animals if total_animals > 20]

# Example call (adjust based on actual total animal count)
print(animals_to_remove_for_savings(animals_to_remove))  # Output: ["Elephant", "Panda"]

```

## Task 4: Which Animal Would Finish a Quarter Mile the Fastest?

**Description**:  
Imagine a scenario where all the animals in the zoo start sprinting at the same time. The zoo management wants to know which animal would finish a quarter-mile distance the fastest. This information is not only fun but could also be used for educational programs and visitor engagement.

**Instructions**:

- You will receive a dataset that includes the sprint speeds of various animals.
- Write a function to determine which animal would complete a quarter-mile race the fastest.
- Your function should return the name of the species that would win the race.
Code Snippet:
```

