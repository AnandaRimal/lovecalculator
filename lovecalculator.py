"""
LOVE CALCULATOR CONCEPT:

The Love Calculator is a fun program that evaluates the compatibility between two people based on their names.
It works by counting the occurrences of specific letters in both names to create two scores:
- "TRUE" score: Based on the letters 'T', 'R', 'U', and 'E'
- "LOVE" score: Based on the letters 'L', 'O', 'V', and 'E'

These scores are combined to form a "love percentage." For example:
- If the 'TRUE' score is 3 and the 'LOVE' score is 4, the love score becomes "34."

The resulting score is interpreted as follows:
- Less than 20: "Your love score is like coke and mentos!"
- Between 20 and 50: "You have an average love score."
- Between 50 and 80: "You have a good love score!"
- Over 80: "You two are an outstanding couple!"

This version of the program also includes:
1. A heart graphic to make the output visually appealing.
2. A "processing" animation to simulate calculation.
3. Fun and personalized messages based on the love score.

NOTE:
This program is purely for entertainment and does not reflect actual compatibility!
"""

import time

def print_heart_art():
    """Prints a decorative heart graphic."""
    heart = """
       ******       ******
     **      **   **      **
   **         ** **         **
  **           **           **
 **             **             **
**               **               **
 **             **             **
  **           **           **
   **         ** **         **
     **      **   **      **
       ******       ******
    """
    print(heart)

def love_calculator():
    """Main Love Calculator logic."""
    print("Welcome to the Love Calculator! 💖")
    time.sleep(1)

    # Print heart art
    print_heart_art()
    time.sleep(1)

    # Get names from the user
    name1 = input("Enter the first person's name: ")
    name2 = input("Enter the second person's name: ")

    # Combine names and calculate scores
    combined = name1 + name2
    lowercase = combined.lower()

    # Count letters for "TRUE"
    t = lowercase.count("t")
    r = lowercase.count("r")
    u = lowercase.count("u")
    e = lowercase.count("e")
    true_score = t + r + u + e

    # Count letters for "LOVE"
    l = lowercase.count("l")
    o = lowercase.count("o")
    v = lowercase.count("v")
    e = lowercase.count("e")
    love_score = l + o + v + e

    # Combine scores
    total_score = str(true_score) + str(love_score)
    love_percentage = int(total_score)

    # Simulate processing effect
    print("\nCalculating your love score... 💘")
    for _ in range(3):
        print("❤️", end="", flush=True)
        time.sleep(1)
    print("\n")

    # Display the love score
    print_heart_art()
    print(f"💖 The love score of {name1} and {name2} is: {total_score}% 💖")

    # Interpret the score
    if love_percentage < 20:
        print("\nYour love score is like coke and mentos! ⚡️")
    elif love_percentage < 50:
        print("\nYou have an average love score. 💕 Keep working on it!")
    elif love_percentage < 80:
        print("\nYou have a good love score! 💘 A lovely bond!")
    else:
        print("\nYou two are an outstanding couple! 💖🌟 Made for each other!")

# Run the Love Calculator
love_calculator()
