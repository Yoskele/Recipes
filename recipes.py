import sqlite3

DB_FILE_PATH = 'data/data.db'

class Recipes:

    def __init__(self):
        '''Set up necessary database objects that will be reused by
        other functions of this class.'''

        self.conn = sqlite3.connect(DB_FILE_PATH)

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()



#-------- -- - - - -- - - - -- - - Jobbar Här -- -------------
    def get_recipes(self, user_id):
        '''Get a list of dictionaries(!) representing recipes that belong
        to the given user.'''
        query = 'SELECT * FROM  recipes WHERE user_id = {}'.format(user_id)
        self.cursor.execute(query)
        info = self.cursor.fetchall()

        return info



#---------------------------- INTE KLAR DENNA UNDER -------------------
    def get_recipe(self, recipe_id):
        '''Get a dictionary(!) of the data for the dictionary whose ID
        matches the given ID.'''
        query = "SELECT * FROM recipes WHERE recipe_id={}".format(recipe_id)
        self.cursor.execute(query)
        #fetchall() method, which fetches all rows from the table
        recipe = self.cursor.fetchone()
        #fetchone() method if you are interested in one row. from the table 
        self.conn.close()
        return recipe
        # Outcome from this code is id and Description and Object

#----------------------------------
    # WORKS WELL
    def add_recipe(self, description, ingredients, user_id):
        '''Add a recipe to the database. Use the given dictionary of data
        as well as the given user ID as data for the new row.'''
        query ="INSERT INTO recipes (user_id, description, ingredients) VALUES ({}, '{}', '{}')".format(user_id, description, ingredients)
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()

#--------------------------------------------------------------

yoss = Recipes()


#print(yoss.get_recipe(7))

#------------------------------------
# TEST KOD gav mig värden innne i column.
    # def get_recipe(self, id):
    #     '''Get a dictionary(!) of the data for the dictionary whose ID
    #     matches the given ID.'''
    #     query = "SELECT * FROM food WHERE id={}".format(id)
    #     self.cursor.execute(query)
    #     food = self.cursor.fetchall()
    #     test = {}
    #     #This gives the first Value inside the id. But cant give id 2.
    #     for x in food:
    #         test = x
    #         print(test[1])
    #     self.conn.close()
    #     return food