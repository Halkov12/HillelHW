from flask import Flask
import pandas as pd

import string
import random



app = Flask(__name__)

@app.route("/generate_password")
def generate_password():
    """
    from 10 to 20 chars
    upper and lower case
    """
    length_password = random.randint(10, 20)
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    all_chars = string.ascii_letters + string.digits + string.punctuation
    for i in range(length_password - 4):
        password_chars.append(random.choice(all_chars))
    random.shuffle(password_chars)
    return ''.join(password_chars)

@app.route("/calculate_average")
def calculate_average():
    """
    csv file with students
    1.calculate average high
    2.calculate average weight
    csv - use lib
    *pandas - use pandas for calculating
    """
    df = pd.read_csv("hw.csv")
    height_value = df[" Height(Inches)"].mean()  # post
    weight_value = df[" Weight(Pounds)"].mean()
    return f"Average height: {height_value} \nAverage weight: {weight_value} "


if __name__ == "__main__":
    app.run(
        debug=True,
        host="localhost",
    )
