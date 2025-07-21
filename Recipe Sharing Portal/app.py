from flask import Flask, render_template, redirect,url_for,request

app = Flask(__name__)

recipe_data = [
    {
        "id": 1,
        "title": "Spaghetti Bolognese",
        "ingredients": [
            "200g spaghetti",
            "100g minced beef",
            "1 onion",
            "2 garlic cloves",
            "400g canned tomatoes",
            "Salt and pepper",
            "Olive oil"
        ],
        "instructions": [
            "Boil spaghetti until al dente.",
            "Heat oil, sauté onion and garlic.",
            "Add minced beef and cook until browned.",
            "Pour in canned tomatoes and simmer for 15 mins.",
            "Season with salt and pepper.",
            "Serve sauce over spaghetti."
        ],
        "image": "spaghetti.jpg"
    },
    {
        "id": 2,
        "title": "Vegetable Fried Rice",
        "ingredients": [
            "2 cups cooked rice",
            "1 carrot",
            "1/2 cup peas",
            "1 bell pepper",
            "2 tbsp soy sauce",
            "2 eggs",
            "Oil"
        ],
        "instructions": [
            "Scramble eggs and set aside.",
            "Stir-fry chopped veggies in oil.",
            "Add rice and soy sauce.",
            "Mix in scrambled eggs.",
            "Serve hot."
        ],
        "image": "fried_rice.jpg"
    }
]

@app.route("/")
def list_recipes():
    return render_template("list.html", recipe_data=recipe_data)

@app.route("/recipe/details")
def recipe_details():
    r_id = request.args.get("id")
    if r_id is None:
        return "Recipe ID is missing", 400

    try:
        r_id = int(r_id)
    except ValueError:
        return "Invalid Recipe ID", 400

    recipe = next((r for r in recipe_data if r["id"] == r_id), None)

    if recipe is None:
        return "Recipe not found", 404

    return render_template("details.html", recipe=recipe)


@app.route("/recipe/add", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        # Get form data
        title = request.form.get("title")
        image = request.form.get("image")
        ingredients = request.form.get("ingredients")  # multiline string
        instructions = request.form.get("instructions")  # multiline string

        # Convert ingredients/instructions into list
        ingredients_list = [line.strip() for line in ingredients.splitlines() if line.strip()]
        instructions_list = [line.strip() for line in instructions.splitlines() if line.strip()]

        # Auto-generate next ID
        new_id = max(r["id"] for r in recipe_data) + 1 if recipe_data else 1

        # Add to recipe_data
        recipe_data.append({
            "id": new_id,
            "title": title,
            "image": image,
            "ingredients": ingredients_list,
            "instructions": instructions_list
        })

        return redirect(url_for('list_recipes'))

    return render_template("add_recipe.html")


if __name__ == "__main__":
    app.run(debug=True)
