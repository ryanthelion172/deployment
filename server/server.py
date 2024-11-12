from flask import Flask, request
from pokemon import PokemonDB
import json

app = Flask(__name__)

# CORS header to handle cross-origin requests
header = {"Access-Control-Allow-Origin": "*"}

@app.route("/pokemon/<int:pokedex_id>", methods=["OPTIONS"])
def handle_cors_options(pokedex_id):
    return "", 204, {
            "Access-Control-Allow-Origin": "*", 
            "Access-Control-Allow-Methods": "PUT, DELETE", 
            "Access-Control-Allow-Headers": "Content-Type"
            }

@app.route("/pokemon", methods=["GET"])
def retrieve_pokemon():
    db = PokemonDB("pokemon.db")
    pokemon_list = db.getPokemon()

	#convert each record to a dictionary if it's not already
    pokemon_data = [
        {
            "pokedex_id": p[0],
            "name": p[1],
            "type1": p[2],
            "type2": p[3],
            "bst": p[4],
            "hit_points": p[5],
            "attack": p[6],
            "defense": p[7],
            "special_attack": p[8],
            "special_defense": p[9],
            "speed": p[10]
        } for p in pokemon_list
    ]
    return pokemon_data, 200, header

@app.route("/pokemon/<int:pokedex_id>", methods=["GET"])
def retrieve_one_pokemon(pokedex_id):
    db = PokemonDB("pokemon.db")
    pokemon_list = db.getOnePokemon(pokedex_id)
    if pokemon_list:
        pokemon_data = [
                {
                    "pokedex_id": p[0],
                    "name": p[1],
                    "type1": p[2],
                    "type2": p[3],
                    "bst": p[4],
                    "hit_points": p[5],
                    "attack": p[6],
                    "defense": p[7],
                    "special_attack": p[8],
                    "special_defense": p[9],
                    "speed": p[10]
                    } for p in pokemon_list
                ] 
        return pokemon_data, 200, header 
    else:
        return "Pokemon not found", 404, header

@app.route("/pokemon/<int:pokedex_id>", methods=["DELETE"])
def delete_pokemon(pokedex_id):
    db = PokemonDB("pokemon.db")
    pokemon = db.getOnePokemon(pokedex_id)

    if pokemon:
        db.deletePokemon(pokedex_id)
        return "", 200, header 
    else:
        return "Pokemon not found", 404, header

@app.route("/pokemon", methods=["POST"])
def create_pokemon():
    print("The Request data is: ", request.form)
    dexid = request.form["pokedex_id"]
    name = request.form["name"]
    type1 = request.form["type1"]
    type2 = request.form["type2"]
    bst = request.form["base_stat_total"]
    hp = request.form["hp"]
    atk = request.form["attack"]
    defen = request.form["defense"]
    spatk = request.form["special_attack"]
    spdef = request.form["special_defense"]
    spe = request.form["speed"]
    
    db = PokemonDB("pokemon.db")
    db.saveRecord(dexid, name, type1, type2, bst, hp, atk, defen, spatk, spdef, spe)

    return "Created", 201, header

@app.route("/pokemon/<int:pokedex_id>", methods=["PUT"])
def update_pokemon(pokedex_id):
    print("Update pokemon with ID ", pokedex_id)

    db = PokemonDB("pokemon.db")
    pokemon = db.getOnePokemon(pokedex_id)

    if pokemon:
        dexid = request.form["pokedex_id"]
        name = request.form["name"]
        type1 = request.form["type 1"]
        type2 = request.form["type 2"]
        bst = request.form["base_stat_total"]
        hp = request.form["hp"]
        atk = request.form["attack"]
        defen = request.form["defense"]
        spatk = request.form["special_attack"]
        spdef = request.form["special_defense"]
        spe = request.form["speed"]

        #db = pokemonDB("pokemon.db")
        db.updatePokemon(pokemon_id, name, type1, type2, bst, hit_points, attack, defense, special_attack, special_defense)
        return f"Updated {pokedex_id}", 201, header
    else:
        return f"Pokemon with {pokedex_id} not found", 404, header

def run():
    app.run(port=8080, host='0.0.0.0')

if __name__ == "__main__":
    run()

