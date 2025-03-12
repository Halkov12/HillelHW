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
    psw = []
    length_psw = random.randint(10, 20)
    counter = 0
    while counter < length_psw:
        psw.append(random.choice(string.ascii_lowercase))
        psw.append(random.choice(string.ascii_uppercase))
        psw.append(random.choice(string.digits))
        psw.append(random.choice(string.punctuation))
        counter += 1
    random.shuffle(psw)
    return ''.join(psw)

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
