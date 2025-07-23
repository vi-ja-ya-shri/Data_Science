import random

# Step 1: Create initial dictionary
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Step 2: Display original dictionary
print("Initial Facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

# Step 3: Modify a fact
people_facts["Jeff"] = "Is afraid of heights."

# Step 4: Add a new person
people_facts["Jill"] = "Can hula dance."

# Step 5: Shuffle and display updated dictionary
print("\nUpdated Facts:\n")
# Convert to list, shuffle, then print to observe if order changes
items = list(people_facts.items())
random.shuffle(items)

for person, fact in items:
    print(f"{person}: {fact}")
