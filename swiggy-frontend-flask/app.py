from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Replace with your MySQL database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "YourPassword",
    "database": "shopping1",
}


@app.route("/", methods=["GET", "POST"])
def form_page():
    if request.method == "POST":
        # Get form data
        username = request.form["username"]
        phone = request.form["phone"]
        email = request.form["email"]
        location = request.form["location"]
        pin = request.form["pin"]
        password = request.form["password"]

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "INSERT INTO register (username, phone , email, location , pin , password) VALUES (%s, %s, %s, %s, %s , %s)"
        data = (username, phone, email, location, pin, password,)

        try:
            cursor.execute(query, data)
            connection.commit()
            message = "Data inserted successfully!"
        except mysql.connector.Error as err:
            connection.rollback()
            message = f"Error: {err}"
        finally:
            cursor.close()
            connection.close()

        return render_template("main.html", message=message)

    return render_template("signup.html")


@app.route("/main", methods=["GET", "POST"])
def main_page():

    return render_template('main.html')


@app.route("/location", methods=["GET", "POST"])
def location_page():

    return render_template('location.html')


@app.route("/india", methods=["GET", "POST"])
def india_page():

    return render_template('india.html')


@app.route("/italin", methods=["GET", "POST"])
def italin_page():

    return render_template('italin.html')


@app.route("/chaines", methods=["GET", "POST"])
def chaines_page():

    return render_template('chaines.html')


@app.route("/frenchfries", methods=["GET", "POST"])
def frenchfries_page():

    return render_template('frenchfries.html')


@app.route("/burger", methods=["GET", "POST"])
def burger_page():

    return render_template('burger.html')


@app.route("/friedrice", methods=["GET", "POST"])
def friedrice_page():

    return render_template('friedrice.html')


@app.route("/menu1", methods=["GET", "POST"])
def menu1_page():

    return render_template('menu1.html')


@app.route("/menu2", methods=["GET", "POST"])
def menu2_page():

    return render_template('menu2.html')


@app.route("/menu3", methods=["GET", "POST"])
def menu3_page():

    return render_template('menu3.html')


@app.route("/momos", methods=["GET", "POST"])
def momos_page():

    return render_template('momos.html')


@app.route("/noodles", methods=["GET", "POST"])
def noodles_page():

    return render_template('noodles.html')


@app.route("/pizza", methods=["GET", "POST"])
def pizza_page():

    return render_template('pizza.html')


if __name__ == "__main__":
    app.run(debug=True)
