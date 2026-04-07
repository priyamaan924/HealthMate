def recommend_diet(goal, calories):
    
    if goal == "Weight Loss":

        return {
            "Breakfast": "Oats + fruits (350 kcal)",
            "Lunch": "Brown rice + vegetables + dal (600 kcal)",
            "Dinner": "Salad + grilled chicken/tofu (450 kcal)",
            "Snack": "Nuts + green tea (200 kcal)"
        }

    elif goal == "Weight Gain":

        return {
            "Breakfast": "Peanut butter toast + banana shake (600 kcal)",
            "Lunch": "Rice + chicken/paneer + vegetables (800 kcal)",
            "Dinner": "Eggs + whole wheat bread (600 kcal)",
            "Snack": "Protein smoothie (300 kcal)"
        }

    else:

        return {
            "Breakfast": "Oats + milk + fruits (400 kcal)",
            "Lunch": "Rice + dal + vegetables (650 kcal)",
            "Dinner": "Soup + salad + paneer/chicken (500 kcal)",
            "Snack": "Yogurt + nuts (200 kcal)"
        }