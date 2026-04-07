def recommend_workout(goal):
    
    if goal == "Weight Loss":

        return [
            "Day 1: Running – 30 minutes",
            "Day 2: HIIT workout – 20 minutes",
            "Day 3: Cycling – 30 minutes",
            "Day 4: Strength training",
            "Day 5: Jogging + core workout",
            "Day 6: Yoga / Stretching",
            "Day 7: Rest"
        ]

    elif goal == "Weight Gain":

        return [
            "Day 1: Chest + Triceps workout",
            "Day 2: Back + Biceps workout",
            "Day 3: Leg day",
            "Day 4: Shoulder workout",
            "Day 5: Full body strength training",
            "Day 6: Light cardio",
            "Day 7: Rest"
        ]

    else:

        return [
            "Day 1: Walking – 30 minutes",
            "Day 2: Yoga – 20 minutes",
            "Day 3: Light cardio",
            "Day 4: Strength training",
            "Day 5: Cycling",
            "Day 6: Stretching",
            "Day 7: Rest"
        ]