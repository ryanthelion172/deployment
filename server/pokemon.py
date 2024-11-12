import sqlite3

def dict_factory(cursor, row):
    fields = []
    # Extract column names from cursor description
    for column in cursor.description:
        fields.append(column[0])

    # Create a dictionary where keys are column names and values are row values
    result_dict = {}
    for i in range(len(fields)):
        result_dict[fields[i]] = row[i]

    return result_dict

class PokemonDB:
    def __init__(self, filename):
        # connect
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        self.connection.row_factory = dict_factory


    def getPokemon(self):
        #only way to get fetch all or one, have to fetch afterwards
        self.cursor.execute("SELECT * FROM pokemon")
        pokemon = self.cursor.fetchall()
        return pokemon

    def getOnePokemon(self, dex_id):
        data = [dex_id]
        #only way to get fetch all or one, have to fetch afterwards
        self.cursor.execute("SELECT * FROM pokemon WHERE pokedex_id = ?",data)
        pokemon = self.cursor.fetchone()
        return pokemon

    def addPokemon(self,dex_id,name,type1,type2,bst,hp,atk,spatk,defen,spdef,spd):
        data = [dex_id,name,type1,type2,bst,hp,atk,spatk,defen,spdef,spd]
        self.cursor.execute("INSERT INTO pokemon(pokedex_id,name,type1,type2,bst,hit_points,attack,special_attack,defense,special_defense,speed)VALUES(?,?,?,?,?,?,?,?,?,?,?)",data)
        self.connection.commit()

    def deletePokemon(self, dex_id):
        data = [dex_id]
        self.cursor.execute("DELETE FROM pokemon WHERE pokedex_id = ?",data);
        self.connection.commit()

    def updatePokemon(self,dex_id,name,type1,type2,bst,hp,atk,spatk,defen,spdef,spd):
        data = [name,type1,type2,bst,hp,atk,spatk,defen,spdef,spd,dex_id]
        self.cursor.execute("UPDATE pokemon SET pokedex_id = ?,name = ?,type1 = ?,type2 = ?,bst = ?,hit_points = ?,attack = ?,special_attack = ?,defense = ?,special_defense = ?,speed = ? WHERE id = ?",data)
        self.connection.commit()


#cursor.execute("INSERT INTO pokemon(pokedex_id,name,type1,bst,hit_points,attack,special_attack,defense,special_defense,speed)VALUES('152','chickorita','Grass',318,45,49,65,49,65,45)")
#connection.commit()


#cursor.execute("DELETE FROM pokemon WHERE pokedex_id = 152");
#connection.commit()

#cursor.execute("SELECT * FROM pokemon")

#print(cursor.fetchall())

#connection.close()

