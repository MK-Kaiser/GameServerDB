from flask import Flask, render_template, json, request
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
#db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/characters', methods=['GET', 'POST'] )
def characters():
    if request.method == "POST":
        character = request.form['character_name']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        print(character)
        return render_template("characters.j2", result=character)

    else:
        return render_template("characters.j2")

@app.route('/update_characters/<int:id>', methods=['GET', 'POST'] )
def update_characters(id):
    if request.method == "POST":
        character = request.form['character_name']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        print('Updated character name to:', character)
        return render_template("update_characters.j2", result=character)

    else:
        return render_template("update_characters.j2")

@app.route('/delete_characters/<int:id>', methods=['GET', 'POST'] )
def delete_characters(id):
    if request.method == "POST":
        character = request.form['character_name']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        print(character)
        return render_template("characters.j2", result=character)

    else:
        return render_template("characters.j2")


@app.route('/guilds',  methods=['GET', 'POST'] )
def guilds():
    if request.method == "POST":
        result = request.form['character']
        result += ' '
        result += request.form['guild']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("guilds.j2", result=result)

    else:
        return render_template("guilds.j2")

@app.route('/update_guilds/<int:id>',  methods=['GET', 'POST'] )
def update_guilds(id):
    if request.method == "POST":
        result = request.form['character']
        result += ' '
        result += request.form['guild']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("update_guilds.j2", result=result)

    else:
        return render_template("update_guilds.j2")

@app.route('/delete_guilds/<int:id>',  methods=['GET', 'POST'] )
def delete_guilds(id):
    if request.method == "POST":
        result = request.form['character']
        result += ' '
        result += request.form['guild']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("guilds.j2", result=result)

    else:
        return render_template("guilds.j2")


@app.route('/users',  methods=['GET', 'POST'] )
def users():
    if request.method == "POST":
        result = request.form['email']
        result += ' '
        result += request.form['firstname']
        result += ' '
        result += request.form['lastname']
        result += ' '
        result += request.form['password']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("users.j2", result=result)

    else:
        return render_template("users.j2")

@app.route('/update_users/<int:id>',  methods=['GET', 'POST'] )
def update_users(id):
    if request.method == "POST":
        result = request.form['email']
        result += ' '
        result += request.form['firstname']
        result += ' '
        result += request.form['lastname']
        result += ' '
        result += request.form['password']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("update_users.j2", result=result)

    else:
        return render_template("update_users.j2")


@app.route('/delete_users/<int:id>',  methods=['GET', 'POST'] )
def delete_users(id):
    if request.method == "POST":
        result = request.form['email']
        result += ' '
        result += request.form['firstname']
        result += ' '
        result += request.form['lastname']
        result += ' '
        result += request.form['password']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("users.j2", result=result)

    else:
        return render_template("users.j2")


@app.route('/professions',  methods=['GET', 'POST'] )
def professions():
    if request.method == "POST":
        name = request.form['name']
        print(name)
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("professions.j2", result=name)

    else:
        return render_template("professions.j2")

@app.route('/update_professions/<int:id>',  methods=['GET', 'POST'] )
def update_professions(id):
    if request.method == "POST":
        name = request.form['name']
        print(name)
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("update_professions.j2", result=name)

    else:
        return render_template("update_professions.j2")

@app.route('/delete_professions/<int:id>',  methods=['GET', 'POST'] )
def delete_professions(id):
    if request.method == "POST":
        name = request.form['name']
        print(name)
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("professions.j2", result=name)

    else:
        return render_template("professions.j2")


@app.route('/recipes',  methods=['GET', 'POST'] )
def recipes():
    if request.method == "POST":
        ingredient = request.form['ingredient']
        print(ingredient)
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("recipes.j2", result=ingredient)

    else:
        return render_template("recipes.j2")

@app.route('/update_recipes/<int:id>',  methods=['GET', 'POST'] )
def update_recipes(id):
    if request.method == "POST":
        ingredient = request.form['ingredient']
        print(ingredient)
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("update_recipes.j2", result=ingredient)

    else:
        return render_template("update_recipes.j2")

@app.route('/delete_recipes/<int:id>',  methods=['GET', 'POST'] )
def delete_recipes(id):
    if request.method == "POST":
        ingredient = request.form['ingredient']
        print(ingredient)
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("recipes.j2", result=ingredient)

    else:
        return render_template("recipes.j2")



# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8333))
    app.run(port=port, debug=True)
