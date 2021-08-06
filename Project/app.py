from flask import Flask, render_template, json, request, redirect
import os
import database.db_connector as db

# Configuration
app = Flask(__name__)

# Routes 
'''A large portion of code based on provided starter code and following along with flask lecture videos.'''
@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/characters', methods=['GET', 'POST'] )
def characters():
    ''' Intercepts POST requests and adds new character tied to a specific user based on form inputs and a userEmail to userId lookup.
        Intercepts GET requests and displays table with all current characters.
    '''
    db_connection = db.connect_to_database()
    if request.method == 'POST':
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
        '''https://pythonbasics.org/flask-redirect-and-errors/'''
        return redirect('/characters')

    else:
        charName = request.args.get('charName')
        if charName:
            query = "SELECT GameUsers.userEmail AS userEmail, GameCharacters.charName AS charName, GameCharacters.userId, GameCharacters.level FROM GameUsers, GameCharacters WHERE charName Like %s GROUP BY charName HAVING COUNT(charName) > 1;"
            data = ('%'+charName+'%',)
            cursor = db.execute_query(db_connection, query, data)
            results = cursor.fetchall()
            print(results)
            return render_template("characters.j2", rows=results)

        else:
            # How to pass multiple values to same render_template: https://flask.palletsprojects.com/en/2.0.x/api/
            query = "SELECT GameUsers.userEmail AS userEmail, GameUsers.userId as userId, GameCharacters.charName AS charName, GameCharacters.level FROM GameUsers, GameCharacters GROUP BY charName HAVING COUNT(charName) > 1;"
            cursor = db.execute_query(db_connection, query=query)
            results = cursor.fetchall()
            print(results)
            query2 = "SELECT userEmail, userId FROM GameUsers GROUP BY userId;"
            cursor2 = db.execute_query(db_connection, query2)
            results2 = cursor2.fetchall()
            print(results2)
            return render_template("characters.j2", rows=results, rows2=results2)

@app.route('/update_characters/<int:userId>', methods=['GET', 'POST'] )
def update_characters(userId):
    ''' Intercepts POST requests and updates details of an existing character based on form inputs.
        Intercepts GET requests and displays table row with the selected character's details pre-populated.
    '''
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
    '''removes character by specified charName'''
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
    ''' Intercepts POST requests and adds new guild based on form inputs.
        Intercepts GET requests and displays table with all current guilds.
    '''
    db_connection = db.connect_to_database()
    if request.method == 'POST':
        guildName = request.form['guildName']
        query = 'INSERT INTO GameGuilds (guildName) Values (%s)'
        data = (guildName,)
        db.execute_query(db_connection, query, data)
        return redirect('/guilds')

    else:
        guildName = request.args.get('guildName')
        if guildName:
            query = "SELECT guildName, guildId FROM GameGuilds WHERE guildName LIKE %s "
            data = (guildName+'%',)
            cursor = db.execute_query(db_connection, query, data)
            results = cursor.fetchall()
            print(results)
            return render_template("guilds.j2", rows=results)

        else:
            query = "SELECT guildName, guildId FROM GameGuilds;"
            cursor = db.execute_query(db_connection, query)
            results = cursor.fetchall()
            print(results)
            return render_template("guilds.j2", rows=results)

@app.route('/update_guilds/<int:id>',  methods=['GET', 'POST'] )
def update_guilds(id):
    ''' Intercepts POST requests and updates details of an existing guild based on form inputs.
        Intercepts GET requests and displays table row with the selected guild's details pre-populated.
    '''
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
        query = 'SELECT guildName, guildId FROM GameGuilds WHERE guildId = %s;' % (id)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchone()
        print(results)
        return render_template("update_guilds.j2", row=results)

@app.route('/delete_guilds/<int:id>',  methods=['GET', 'POST'] )
def delete_guilds(id):
    ''' 
        Intercepts GET requests and removes the selected row by guildId.
    '''
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
    ''' Intercepts POST requests and adds new user based on form inputs.
        Intercepts GET requests and displays table with all current users.
    '''
    db_connection = db.connect_to_database()
    if request.method == 'POST':
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
        firstName = request.args.get("firstName")
        if firstName:
            query = "SELECT userEmail, firstName, lastName, password, userId FROM GameUsers WHERE firstName LIKE %s "
            data = ('%'+firstName+'%',)
            cursor = db.execute_query(db_connection, query, data)
            results = cursor.fetchall()
            print(results)
            return render_template("users.j2", rows=results)

        else:
            query = "SELECT userEmail, firstName, lastName, password, userId FROM GameUsers;"
            cursor = db.execute_query(db_connection, query)
            results = cursor.fetchall()
            print(results)
            return render_template("users.j2", rows=results)

@app.route('/update_users/<int:userId>',  methods=['GET', 'POST'] )
def update_users(userId):
    ''' Intercepts POST requests and updates and existing user based on form inputs.
        Intercepts GET requests and displays table with all current users.
    '''
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
    '''removes a user by provided userEmail'''
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
    ''' 
        Intercepts GET requests and displays table with all current profession.
    '''
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
        professionName = request.args.get('professionName')
        if professionName:
            query = "SELECT professionName, professionId FROM GameProfessions WHERE professionName LIKE %s "
            data = (professionName+'%',)
            cursor = db.execute_query(db_connection, query, data)
            results = cursor.fetchall()
            return render_template("professions.j2", rows=results)

        else:
            query = "SELECT professionName, professionId FROM GameProfessions;"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            results = cursor.fetchall()
            print(results)
            return render_template("professions.j2", rows=results)


@app.route('/recipes',  methods=['GET', 'POST'] )
def recipes():
    ''' Intercepts POST requests and adds new recipe based on form inputs.
        Intercepts GET requests and displays table with all current recipes.
    '''
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
        recipeName = request.args.get('recipeName')
        levelRequirement = request.args.get('levelRequirement')
        if recipeName or levelRequirement:
            query = "SELECT recipeName, levelRequirement, professionId, recipeId FROM GameProfessionsRecipes WHERE recipeName LIKE %s "
            data = (recipeName+'%',)
            cursor = db.execute_query(db_connection, query, data)
            results = cursor.fetchall()
            return render_template("recipes.j2", rows=results)


        else:
            query = "SELECT recipeName, levelRequirement, professionId, recipeId FROM GameProfessionsRecipes;"
            cursor = db.execute_query(db_connection, query)
            results = cursor.fetchall()
            print(results)
            return render_template("recipes.j2", rows=results)

@app.route('/update_recipes/<int:recipeId>',  methods=['GET', 'POST'] )
def update_recipes(recipeId):
    ''' Intercepts POST requests and updates an existing recipe based on form inputs.
        Intercepts GET requests and displays table with all current recipes.
    '''
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
    '''removes a recipe by recipeId.'''
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
    app.run(host='0.0.0.0', port=port, debug=True) #flip/www
    # app.run(port=port, debug=True) #localhost

