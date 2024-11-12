const apiWrapper = window.location.protocol === 'file:' ? 'https://localhost:8080' : ''


// Add Pokemon
document.getElementById("add-pokemon-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const dexid = document.getElementById("dexid").value;
    const name = document.getElementById("name").value;
    const type1 = document.getElementById("type1").value;
    const type2 = document.getElementById("type2").value;
    const bst = document.getElementById("bst").value;
    const hp = document.getElementById("hp").value;
    const atk = document.getElementById("atk").value;
    const defen = document.getElementById("defen").value;
    const spatk = document.getElementById("spatk").value;
    const spdef = document.getElementById("spdef").value;
    const spe = document.getElementById("spe").value;

    // Construct the data string
    let data = 
        "pokedex_id=" + encodeURIComponent(dexid) +
        "&name=" + encodeURIComponent(name) +
        "&type1=" + encodeURIComponent(type1) +
        "&type2=" + encodeURIComponent(type2) +
        "&base_stat_total=" + encodeURIComponent(bst) +
        "&hp=" + encodeURIComponent(hp) +
        "&attack=" + encodeURIComponent(atk) +
        "&defense=" + encodeURIComponent(defen) +
        "&special_attack=" + encodeURIComponent(spatk) +
        "&special_defense=" + encodeURIComponent(spdef) +
        "&speed=" + encodeURIComponent(spe);

    fetch("http://localhost:8080/pokemon", {
        method: "POST",
        body: data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }).then(response => {
        if (response.status === 201) {
            console.log("New Pokémon created!", response);
            loadPokemon();
        }
    });

    // Clear form fields after submission
    document.getElementById("add-pokemon-form").reset();
});

function resetForm() {
    document.getElementById("pokemon-form").reset();
    document.getElementById("form-title").innerText = "Add a new Pokémon";
    document.getElementById("form-submit").innerText = "Add Pokémon";
}


// Edit Pokémon
function editPokemon(pokedex_id) {
    // Prompt the user for new values for each attribute
    const newName = prompt("Enter new name for Pokémon:");
    const newType1 = prompt("Enter new primary type:");
    const newType2 = prompt("Enter new secondary type:");
    const newBst = prompt("Enter new Base Stat Total:");
    const newHp = prompt("Enter new HP:");
    const newAtk = prompt("Enter new Attack:");
    const newDefen = prompt("Enter new Defense:");
    const newSpatk = prompt("Enter new Special Attack:");
    const newSpdef = prompt("Enter new Special Defense:");
    const newSpe = prompt("Enter new Speed:");

    // Construct the data string for the PUT request
    let data =
        "name=" + encodeURIComponent(newName) +
        "&type1=" + encodeURIComponent(newType1) +
        "&type2=" + encodeURIComponent(newType2) +
        "&base_stat_total=" + encodeURIComponent(newBst) +
        "&hp=" + encodeURIComponent(newHp) +
        "&attack=" + encodeURIComponent(newAtk) +
        "&defense=" + encodeURIComponent(newDefen) +
        "&special_attack=" + encodeURIComponent(newSpatk) +
        "&special_defense=" + encodeURIComponent(newSpdef) +
        "&speed=" + encodeURIComponent(newSpe);

    // Send the PUT request to update the Pokémon
    fetch(`http://localhost:8080/pokemon/${pokedex_id}`, {
        method: "PUT",
        body: data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }).then(response => {
        if (response.status === 201) {
            console.log("Pokémon updated!", response);
            loadPokemon(); // Reload the list to show updated values
        } else {
            console.log("Failed to update Pokémon", response);
        }
    });
}



// Fetch and display all Pokémon
function loadPokemon() {
    fetch("http://localhost:8080/pokemon")
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector("#pokemon-table tbody");
            tableBody.innerHTML = "";
            data.forEach(pokemon => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${pokemon.pokedex_id}</td>
                    <td>${pokemon.name}</td>
                    <td>${pokemon.type1}</td>
                    <td>${pokemon.type2}</td>
                    <td>${pokemon.bst}</td>
                    <td>${pokemon.hit_points}</td>
                    <td>${pokemon.attack}</td>
                    <td>${pokemon.defense}</td>
                    <td>${pokemon.special_attack}</td>
                    <td>${pokemon.special_defense}</td>
                    <td>${pokemon.speed}</td>
                    <td>
                        <button onclick="editPokemon(${pokemon.pokedex_id})">Edit</button>
                        <button onclick="deletePokemon(${pokemon.pokedex_id})">Delete</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        });
}


// Delete Pokémon
function deletePokemon(pokedex_id) {

    const confirmation = confirm(`Are you sure you want to delete Pokémon with Pokedex ID ${pokedex_id}?`);
    if (confirmation == true) {
	    fetch(`http://localhost:8080/pokemon/${pokedex_id}`, {
		method: "DELETE"
	    }).then(() => loadPokemon());
    }
}

// Initial load
loadPokemon();

