from flask import Flask, render_template, json, request, redirect
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
        userEmail = request.form['userEmail']
        charName = request.form['charName']
        level = request.form['level']
        '''insert new character tied to the specified user'''
        query = 'SELECT userEmail, userId FROM `GameUsers` WHERE userEmail = %s'
        data = (userEmail,)
        results = db.execute_query(db_connection, query, data).fetchone()
        userId = results['userId']
        '''Inserts new character'''
        query = 'INSERT INTO GameCharacters (charName, userId, level) Values (%s, %s, %s)'
        data = (charName, userId, level)
        db.execute_query(db_connection, query, data)
        return redirect('/characters')

    else:
        query = "SELECT charName, level, userId FROM GameCharacters;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("characters.j2", rows=results)

@app.route('/update_characters/<int:userId>', methods=['GET', 'POST'] )
def update_characters(userId):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        charName = request.form['charName']
        level = request.form['level']
        query = 'UPDATE GameCharacters SET charName = %s, level = %s WHERE userId = %s'
        data = (charName, level, userId)
        db.execute_query(db_connection, query, data)
        return redirect("/characters")

    else:
        '''Right now it is pulling first character in db owned by that user, need to get exact char match on charName and userId'''
        query = 'SELECT charName, level, userId FROM GameCharacters WHERE userId = %s;' % (userId)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_characters.j2", row=results)

@app.route('/delete_characters/<charName>', methods=['GET', 'POST'] )
def delete_characters(charName):
    '''removes character by specified name'''
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        print(charName)
        query = 'DELETE FROM GameCharacters WHERE charName = (%s)'
        data = (charName,)
        result = db.execute_query(db_connection, query, data)
        return redirect('/characters')

    else:
        return render_template("characters.j2")


@app.route('/guilds',  methods=['GET', 'POST'] )
def guilds():
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        guildName = request.form['guildName']
        '''Inserts new guild'''
        query = 'INSERT INTO GameGuilds (guildName) Values (%s)'
        data = (guildName,)
        db.execute_query(db_connection, query, data)
        return redirect('/guilds')


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
        guildName = request.form['guildName']
        guildId = request.form['guildId']
        print(guildName, guildId)
        query = 'UPDATE GameGuilds SET guildName = %s WHERE guildId = %s'
        data = (guildName, guildId)
        db.execute_query(db_connection, query, data)
        return redirect('/guilds')

    else:
        '''prepopulates the update page with the selected guild to update'''
        query = 'SELECT guildName, guildId FROM GameGuilds WHERE guildId = %s;' % (id)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_guilds.j2", row=results)

@app.route('/delete_guilds/<int:id>',  methods=['GET', 'POST'] )
def delete_guilds(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        query = 'DELETE FROM GameGuilds WHERE guildId = (%s)'
        data = (id,)
        result = db.execute_query(db_connection, query, data)
        return redirect('/guilds')

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
        return redirect("/users")

    else:
        query = "SELECT userEmail, firstName, lastName, password, userId FROM GameUsers;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("users.j2", rows=results)

@app.route('/update_users/<int:userId>',  methods=['GET', 'POST'] )
def update_users(userId):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        userEmail = request.form['userEmail']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        password = request.form['password']
        query = 'UPDATE GameUsers SET userEmail = %s, firstName = %s, lastName = %s, password = %s WHERE userId = %s'
        data = (userEmail, firstName, lastName, password, userId)
        db.execute_query(db_connection, query, data)
        return redirect("/users")

    else:
        query = 'SELECT userEmail, firstName, lastName, password, userId FROM GameUsers WHERE userId = %s;' % (userId)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_users.j2", row=results)


@app.route('/delete_users/<userEmail>',  methods=['GET', 'POST'] )
def delete_users(userEmail):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        query = 'DELETE FROM GameUsers WHERE userEmail = (%s)'
        data = (userEmail,)
        result = db.execute_query(db_connection, query, data)
        return redirect('/users')

    else:
        return render_template("users.j2")


@app.route('/professions',  methods=['GET', 'POST'] )
def professions():
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        '''Not working yet, complains with:
        CONSTRAINT `CONSTRAINT_1` failed for `cs340_kaisemar`.`GameProfessions`'''
        professionName = request.form['professionName']
        '''Inserts new profession'''
        query = 'INSERT INTO GameProfessions (professionName) Values (%s)'
        data = (professionName,)
        db.execute_query(db_connection, query, data)
        return redirect('/professions')

    else:
        query = "SELECT professionName, professionId FROM GameProfessions;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("professions.j2", rows=results)

@app.route('/update_professions/<int:professionId>',  methods=['GET', 'POST'] )
def update_professions(professionId):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        professionName = request.form['professionName']
        query = 'UPDATE GameProfessions SET professionName = %s WHERE professionId = %s'
        data = (professionName, professionId)
        db.execute_query(db_connection, query, data)
        return redirect("/professions")

    else:
        query = 'SELECT professionName, professionId FROM GameProfessions WHERE professionId = %s;' % (professionId)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_professions.j2", row=results)

@app.route('/delete_professions/<int:id>',  methods=['GET', 'POST'] )
def delete_professions(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        query = 'DELETE FROM GameProfessions WHERE professionId = (%s)'
        data = (id,)
        result = db.execute_query(db_connection, query, data)
        return redirect('/professions')

    else:
        return render_template("professions.j2")


@app.route('/recipes',  methods=['GET', 'POST'] )
def recipes():
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        recipeName = request.form['recipeName']
        levelRequirement = request.form['levelRequirement']
        professionId = request.form['professionId']
        query = 'INSERT INTO GameProfessionsRecipes (recipeName, levelRequirement, professionId) Values (%s, %s, %s)'
        data = (recipeName, levelRequirement, professionId)
        db.execute_query(db_connection, query, data)
        return redirect('/recipes')

    else:
        query = "SELECT recipeName, levelRequirement, professionId, recipeId FROM GameProfessionsRecipes;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        print(results)
        return render_template("recipes.j2", rows=results)

@app.route('/update_recipes/<int:recipeId>',  methods=['GET', 'POST'] )
def update_recipes(recipeId):
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        recipeName = request.form['recipeName']
        levelRequirement = request.form['levelRequirement']
        professionId = request.form['professionId']
        query = 'UPDATE GameProfessionsRecipes SET recipeName = %s, levelRequirement = %s, professionId = %s WHERE recipeId = %s'
        data = (recipeName, levelRequirement, professionId, recipeId)
        db.execute_query(db_connection, query, data)
        return redirect("/recipes")

    else:
        query = 'SELECT recipeName, levelRequirement, professionId, recipeId FROM GameProfessionsRecipes WHERE recipeId = %s;' % (recipeId)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_recipes.j2", row=results)

@app.route('/delete_recipes/<int:id>',  methods=['GET', 'POST'] )
def delete_recipes(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        query = 'DELETE FROM GameProfessionsRecipes WHERE recipeId = (%s)'
        data = (id,)
        result = db.execute_query(db_connection, query, data)
        return redirect('/recipes')

    else:
        return render_template("recipes.j2")



# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8333))
    app.run(port=port, debug=True)
