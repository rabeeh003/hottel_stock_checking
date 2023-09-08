class Kichen:
    pantry = {
        "chicken": 500,
        "lemon": 2,
        "cumin": 24,
        "paprika": 18,
        "chilli powder": 7,
        "yogurt": 300,
        "oil": 450,
        "onion": 5,
        "garlic": 9,
        "ginger": 2,
        "tomato puree": 125,
        "almonds": 75,
        "rice": 500,
        "coriander": 20,
        "lime": 3,
        "pepper": 8,
        "egg": 6,
        "pizza": 2,
        "spam": 1,
    }

    recipes = {
        "Butter chicken": [
            "chicken",
            "lemon",
            "cumin",
            "paprika",
            "chilli powder",
            "yogurt",
            "oil",
            "onion",
            "garlic",
            "ginger",
            "tomato puree",
            "almonds",
            "rice",
            "coriander",
            "lime",
        ],
        "Chicken and chips": [
            "chicken",
            "potatoes",
            "salt",
            "malt vinegar",
        ],
        "Pizza": [
            "pizza",
        ],
        "Egg sandwich": [
            "egg",
            "bread",
            "butter",
        ],
        "Beans on toast": [
            "beans",
            "bread",
        ],
        "Spam a la tin": [
            "spam",
            "tin opener",
            "spoon",
        ],
    }

class Cooking(Kichen):
    def __init__(self):
        print("""
            Select a recipe number:
                1 = Butter chicken
                2 = Chicken and chips
                3 = Pizza
                4 = Egg sandwich
                5 = Beans on toast
                6 = Spam a la tin
        """)
        self.tools = Kichen.pantry.copy()
        self.resi = Kichen.recipes
        self.item = int(input("Enter a number: "))

    def processing(self):
        selected = self.resi[self.selected]
        for x in selected:
            if x in self.tools:
                self.tools[x] -= 1
        print(f"After take items for {self.selected}. balance stoke:")
        for x, y in self.tools.items():
            print(x, y)

    def checking(self):
        if self.item == 1:
            self.selected = "Butter chicken"
            print("Selected recipe: ",self.selected, self.resi[self.selected])
            self.processing()
        elif self.item == 2:
            self.selected = "Chicken and chips"
            print("Selected recipe: ", self.selected, self.resi[self.selected])
            self.processing()
        elif self.item == 3:
            self.selected = "Pizza"
            print("Selected recipe: ", self.selected, self.resi[self.selected])
            self.processing()
        elif self.item == 4:
            self.selected = "Egg sandwich"
            print("Selected recipe: ", self.selected, self.resi[self.selected])
            self.processing()
        elif self.item == 5:
            self.selected = "Beans on toast"
            print("Selected recipe: ", self.selected, self.resi[self.selected])
            self.processing()
        elif self.item == 6:
            self.selected = "Spam a la tin"
            print("Selected recipe: ", self.selected, self.resi[self.selected])
            self.processing()
        else:
            print("Selected recipe: ", self.item, "not available this time.\nplease chose another")


ok = Cooking()
ok.checking()