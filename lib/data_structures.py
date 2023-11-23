spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} - Cuisine: {food['cuisine']}, Heat Level: {food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

# Example usage:
names = get_names(spicy_foods)
print("Names of Spicy Foods:", names)

spiciest_foods = get_spiciest_foods(spicy_foods)
print("Spiciest Foods:")
print_spicy_foods(spiciest_foods)

average_heat = get_average_heat_level(spicy_foods)
print("Average Heat Level:", average_heat)

# Adding a new spicy food
new_spicy_food = {
    "name": "Jerk Chicken",
    "cuisine": "Jamaican",
    "heat_level": 8,
}
create_spicy_food(spicy_foods, new_spicy_food)

# Checking spicy food by cuisine
cuisine = "Thai"
spicy_food_by_cuisine = get_spicy_food_by_cuisine(spicy_foods, cuisine)
if spicy_food_by_cuisine:
    print(f"Spicy Food from {cuisine}: {spicy_food_by_cuisine['name']}")
else:
    print(f"No spicy food found from {cuisine}.")
