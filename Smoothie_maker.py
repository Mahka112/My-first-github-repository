import pandas as pd
import openai

def available_ingredients():
    """
    Displays the available smoothie ingredients, including frozen fruits, bases, and special additions.
    """
    smoothie_ingredients = {
        "Frozen Fruits": ["Banana", "Date", "Passionfruit", "Pineapple", "Berries", "Strawberries", "Mango", "Melon"],
        "base": [
            "Oat Milk", "Rice Milk", "Almond Milk", "3% Milk", "2% Milk", "1% Milk",
            "Soy Milk", "Light Soy Milk", "Sugar-Free Soy Mil", "water", "orange juice"
        ],
        "Special Additions": [
            "Pecan", "Chia Seeds", "Spirulina", "Acai", "Tahini", "Silan", "Banana Protein Powder",
            "Berry Protein Powder", "Cocoa", "Matcha", "ice"
        ]
    }

    df = pd.DataFrame.from_dict(smoothie_ingredients, orient='index').transpose()
    print('here are the available ingredients:')
    print(df)
    return smoothie_ingredients


def smoothie_maker():
    smoothie_ingredients = available_ingredients()
    while True:
        # קבלת רכיבים מהמשתמש
        fruits = []
        for i in range(3):
            fruit = input(f"Please choose fruit {i+1}: ").capitalize()
            if fruit in smoothie_ingredients['Frozen Fruits']:
                fruits.append(fruit)
            else:
                print(f"{fruit} is not available. Please choose from the available fruits.")
                continue

        base = input("Please choose the base: ").capitalize()
        if base not in smoothie_ingredients['base']:
            print(f"{base} is not available. Please choose from the available bases.")
            continue

        special_addition = []
        for i in range(2):
            addition = input(f"please choose special addition {i+1}: ").capitalize()
            if addition in smoothie_ingredients['Special Additions']:
                special_addition.append(addition)
            else:
                print(f"{addition} is not available. Please choose from the available special additions.")
                continue

        # חיבור הרכיבים ליצירת השייק
        smoothie = f"{fruits}, {base}, {special_addition}"

        takeaway = input("Would you like your smoothie as takeaway? (yes/no): ")
        if takeaway.lower() == 'yes':
            smoothie += ', takeaway'
        elif takeaway.lower() != 'no':
            print("Invalid input, assuming 'no'.")

        while True:
            # אישור מהמשתמש
            question = input("Is your smoothie complete? If you're ready, type 'yes'; if you want to make changes, type 'no' ")
            # בדיקה אם המשתמש סיים
            if question.lower() == "yes":
                return smoothie
            elif question.lower() == "no":
                break
            else:
                print("Please choose Yes or No.\n")

def premade_smoothies():
    smoothie_menu = {
        "Queen banana": ["Banana", "Date", "Pecan"],
        "Tropicana": ["Pineapple", "Mango", "Melon"],
        "Honey milk": ["Strawberries", "Berries", "Honey"],
        "Green master": ["Banana", "Pineapple", "passionfruit", "Spirulina"],
        "Super shake": ["Acai", "Strawberries", "Date", "Chia", "Protein Powder"]
    }
    dataframe = pd.DataFrame.from_dict(smoothie_menu, orient='index')
    dataframe.columns = ["Ingredient 1", "Ingredient 2", "Ingredient 3", "Ingredient 4", "Ingredient 5"]
    print("Available Smoothies Menu:")
    print(dataframe)
    order = input("please choose a smoothie from the menu: ")
    if order.lower().capitalize() in smoothie_menu:
        takeaway = input("Would you like your smoothie as takeaway? (yes/no): ")
        if takeaway.lower() == 'yes':
            order += ', takeaway'
        elif takeaway.lower() != 'no':
            print("Invalid input, assuming 'no'.")

        print(f"your smoothie is: {order}")
    else:
        print("Please Write the full name from the menu")

openai.api_key = ""

def check_smoothie_with_ai(smoothie):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Is this smoothie a good combination? {smoothie}",
        max_tokens=50
    )

    gpt_response = response.choices[0].text.strip().lower()

    # בדיקת התשובה והצגת תוצאה
    if "yes" in gpt_response or "good" in gpt_response:
        print(f"\nYour smoothie is ready! 🍹 Here is your delicious smoothie: {smoothie}")
    else:
        print("\nIt seems that this combination might not be the best. Consider adding or changing an ingredient.")

def main_menu():
    while True:
        print("welcome to the smoothie maker")
        print("1. order premade smoothie")
        print("2. build your own smoothie")
        print("3. available ingridents")
        print("4. exit")
        choice = input("please choose an option: ")
        if choice == "1":
            premade_smoothies()
            break
        elif choice == "2":
            final_smoothie = smoothie_maker()
             check_smoothie_with_ai(final_smoothie):
            print("Your smoothie is:", final_smoothie)
            break
        elif choice == "3":
            available_ingredients()
            break
        elif choice == "4":
            print("thank you for using the smoothie maker")
            break
        else:
            print("Invalid choice, please choose again.")


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
main_menu()
