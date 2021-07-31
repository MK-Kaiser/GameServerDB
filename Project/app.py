from flask import Flask, render_template, json, request
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/characters', methods=['GET', 'POST'] )
def characters():
    ''' Intercepts POST requests and adds new character based on form inputs.
        Intercepts GET requests and displays table with all current characters.
    '''
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        '''good code for enumerating current highest id and incrementing.'''

        # query = 'SELECT max( userId ) FROM GameCharacters;'
        # cursor = db.execute_query(db_connection=db_connection, query=query)
        # highestId = cursor.fetchone()
        # userId = int(highestId['max( userId )'])
        # print(type(userId), userId)
        # userId = str(userId + 1)
        # print('highestId is naturally a: ', type(highestId['max( userId )']))

        '''Lookup userId from provided email'''
        user = request.form['userEmail']
        charName = request.form['charName']
        level = request.form['level']
        '''insert new character tied to the specified user'''
        #query = 'SELECT userEmail, userId FROM `GameUsers` WHERE userEmail = %s;' % (user)
        #results = db.execute_query(db_connection, query).fetchone()
        #userId = results['userId']

        #data = (charName, userId, level)
        #query = 'INSERT INTO GameCharacters (charName, userId, level) Values (%s, %s, %s);'

        #db.execute_query(db_connection, query, data)

        query = "SELECT charName, level, userId FROM GameCharacters;"
        cursor = db.execute_query(db_connection, query)
        results = cursor.fetchall()
        print(results)
        return render_template("characters.j2", rows=results)

    else:
        query = "SELECT charName, level, userId FROM GameCharacters;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("characters.j2", rows=results)

@app.route('/update_characters/<int:id>', methods=['GET', 'POST'] )
def update_characters(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        charName= request.form['charName']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        print('Updated character name to:', charName)
        return render_template("update_characters.j2", result=charName)

    else:
        query = 'SELECT charName, level, userId FROM GameCharacters WHERE userId = %s;' % (id)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_characters.j2", row=results)

@app.route('/delete_characters/<int:id>', methods=['GET', 'POST'] )
def delete_characters(id):
    db_connection = db.connect_to_database()
    if request.method == "POST":
        character = request.form['character_name']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        print(character)
        query = "SELECT charName, level, userId FROM GameCharacters;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("characters.j2", rows=results)

    else:
        return render_template("characters.j2")


@app.route('/guilds',  methods=['GET', 'POST'] )
def guilds():
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        result = request.form['character']
        result += ' '
        result += request.form['guild']
        return render_template("guilds.j2", result=result)

    else:
        query = "SELECT guildName, guildId FROM GameGuilds;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("guilds.j2", rows=results)

@app.route('/update_guilds/<int:id>',  methods=['GET', 'POST'] )
def update_guilds(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        result = request.form['character']
        result += ' '
        result += request.form['guild']
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("update_guilds.j2", result=result)

    else:
        query = 'SELECT guildName, guildId FROM GameGuilds WHERE guildId = %s;' % (id)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_guilds.j2", row=results)

@app.route('/delete_guilds/<int:id>',  methods=['GET', 'POST'] )
def delete_guilds(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
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
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        '''Inserts new user'''
        userEmail = request.form['userEmail']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        password = request.form['password']
        data = (userEmail, firstName, lastName, password)
        print(data)
        query = 'INSERT INTO GameUsers (userEmail, firstName, lastName, password) Values (%s, %s, %s, %s);'
        print(query)
        db.execute_query(db_connection, query, data)
        '''Load updated table'''
        query = "SELECT userEmail, firstName, lastName, password, userId FROM GameUsers;"
        cursor = db.execute_query(db_connection, query)
        results = cursor.fetchall()
        return render_template("users.j2", rows=results)



    else:
        query = "SELECT userEmail, firstName, lastName, password, userId FROM GameUsers;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("users.j2", rows=results)

@app.route('/update_users/<int:id>',  methods=['GET', 'POST'] )
def update_users(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
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
        query = 'SELECT userEmail, firstName, lastName, password, userId FROM GameUsers WHERE userId = %s;' % (id)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_users.j2", row=results)


@app.route('/delete_users/<int:id>',  methods=['GET', 'POST'] )
def delete_users(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
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
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        name = request.form['professionName']
        '''Error inserting profession'''
        #query = 'INSERT INTO GameProfessions (professionName) Values (%s);' % (name)
        #db.execute_query(db_connection, query)

        #return render_template("professions.j2")

        query = "SELECT professionName, professionId FROM GameProfessions;"
        cursor = db.execute_query(db_connection, query)
        results = cursor.fetchall()
        return render_template("professions.j2", rows=results)


    else:
        query = "SELECT professionName, professionId FROM GameProfessions;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("professions.j2", rows=results)

@app.route('/update_professions/<int:id>',  methods=['GET', 'POST'] )
def update_professions(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        name = request.form['name']
        print(name)
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("update_professions.j2", result=name)

    else:
        query = 'SELECT professionName, professionId FROM GameProfessions WHERE professionId = %s;' % (id)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_professions.j2", row=results)

@app.route('/delete_professions/<int:id>',  methods=['GET', 'POST'] )
def delete_professions(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
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
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        print(ingredient)
        return render_template("recipes.j2", result=ingredient)

    else:
        query = "SELECT recipeName, levelRequirement, professionId, recipeId FROM GameProfessionsRecipes;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("recipes.j2", rows=results)

@app.route('/update_recipes/<int:id>',  methods=['GET', 'POST'] )
def update_recipes(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        print(ingredient)
#    query = "SELECT * FROM bsg_people;"
#    cursor = db.execute_query(db_connection=db_connection, query=query)
#    results = cursor.fetchall()
        return render_template("update_recipes.j2", result=ingredient)

    else:
        query = 'SELECT recipeName, levelRequirement, professionId, recipeId FROM GameProfessionsRecipes WHERE recipeId = %s;' % (id)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_recipes.j2", row=results)

@app.route('/delete_recipes/<int:id>',  methods=['GET', 'POST'] )
def delete_recipes(id):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
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
