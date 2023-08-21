from flask import Flask, render_template,request,redirect
import random

app = Flask(__name__)

ingredients_list = [
    {"name": "pommes de terre", "image": "static/images/poivre.jpg"},
    {"name": "oignons", "image": "static/images/oignons.jpg"},
    {"name": "ail", "image": "static/images/ail.jpg"},
    {"name": "huile d'olive", "image": "static/images/huile_dolive.jpg"},
    {"name": "sel", "image": "static/images/sel.jpg"},
    {"name": "riz", "image": "static/images/riz.jpg"},
    {"name": "poivre", "image": "static/images/poivre.jpg"},
    {"name": "poulet", "image": "static/images/poulet.jpg"},
    {"name": "beurre", "image": "static/images/beurre.jpg"},
    {"name": "lait", "image": "static/images/lait.jpg"},
    {"name": "oeufs", "image": "static/images/oeufs.jpg"},
    {"name": "sauce soja", "image": "static/images/sauce soja.jpg"},
    {"name": "sucre", "image": "static/images/sucre.jpg"},
    {"name": "cannelle", "image": "static/images/cannelle.jpg"},
    {"name": "légumes variés", "image": "static/images/légumes variés.jpg"},
    {"name": "basilic", "image": "static/images/basilic.jpg"},
    {"name": "tomates", "image": "static/images/tomates.jpg"},
    {"name": "pommes", "image": "static/images/pommes.jpg"},
    {"name": "vinaigre balsamique", "image": "static/images/vinaigre balsamique.jpg"},
    # Ajoutez plus d'ingrédients avec leurs images ici
]

recipes = [
    {
        "name": "Purée de pommes de terre",
        "ingredients": ["pommes de terre", "beurre", "lait", "sel", "poivre"],
        "steps": [
            "Épluchez les pommes de terre et coupez-les en morceaux.",
            "Faites cuire les pommes de terre dans une casserole d'eau bouillante salée jusqu'à ce qu'elles soient tendres.",
            "Égouttez les pommes de terre et écrasez-les avec un presse-purée.",
            "Ajoutez le beurre et le lait, puis mélangez jusqu'à obtenir une consistance lisse.",
            "Assaisonnez avec du sel et du poivre selon votre goût.",
            "Servez chaud."
        ]
    },
    {
        "name": "Omelette aux oignons",
        "ingredients": ["oeufs", "oignons", "huile d'olive", "sel", "poivre"],
        "steps": [
            "Émincez les oignons.",
            "Faites chauffer l'huile d'olive dans une poêle.",
            "Ajoutez les oignons et faites-les revenir jusqu'à ce qu'ils soient dorés.",
            "Dans un bol, battez les œufs avec du sel et du poivre.",
            "Versez les œufs battus dans la poêle avec les oignons.",
            "Laissez cuire l'omelette jusqu'à ce qu'elle soit prise.",
            "Retournez l'omelette et laissez cuire l'autre côté pendant quelques minutes.",
            "Servez chaud."
        ]
    },
    {
        "name": "Poulet rôti",
        "ingredients": ["poulet", "ail", "huile d'olive", "sel", "poivre"],
        "steps": [
            "Préchauffez le four à 200°C.",
            "Assaisonnez le poulet avec du sel, du poivre et de l'ail.",
            "Badigeonnez le poulet d'huile d'olive.",
            "Placez le poulet dans un plat allant au four et enfournez pendant environ 1 heure.",
            "Vérifiez la cuisson en insérant un thermomètre à viande dans la partie la plus épaisse du poulet. La température interne doit atteindre 75°C.",
            "Laissez reposer le poulet pendant quelques minutes avant de le découper.",
            "Servez chaud."
        ]
    },
    {
        "name": "Riz sauté aux légumes",
        "ingredients": ["riz", "légumes variés", "huile d'olive", "sauce soja"],
        "steps": [
            "Faites cuire le riz selon les instructions sur l'emballage.",
            "Dans une poêle, faites chauffer l'huile d'olive.",
            "Ajoutez les légumes coupés en dés et faites-les sauter jusqu'à ce qu'ils soient tendres.",
            "Ajoutez le riz cuit dans la poêle avec les légumes.",
            "Versez la sauce soja sur le riz et mélangez bien.",
            "Laissez cuire pendant quelques minutes jusqu'à ce que le riz soit chaud.",
            "Servez chaud."
        ]
    },
    {
        "name": "Salade de tomates et mozzarella",
        "ingredients": ["tomates", "mozzarella", "basilic", "huile d'olive", "vinaigre balsamique"],
        "steps": [
            "Coupez les tomates et la mozzarella en tranches.",
            "Disposez les tranches de tomates et de mozzarella sur une assiette.",
            "Parsemez de feuilles de basilic frais.",
            "Arrosez d'huile d'olive et de vinaigre balsamique.",
            "Salez et poivrez selon votre goût.",
            "Servez frais."
        ]
    },
    {
        "name": "Tarte aux pommes",
        "ingredients": ["pâte brisée", "pommes", "sucre", "cannelle"],
        "steps": [
            "Préchauffez le four à 180°C.",
            "Étalez la pâte brisée dans un moule à tarte.",
            "Épluchez et coupez les pommes en tranches.",
            "Disposez les tranches de pommes sur la pâte brisée.",
            "Saupoudrez de sucre et de cannelle.",
            "Enfournez la tarte pendant environ 30 minutes, jusqu'à ce qu'elle soit dorée.",
            "Laissez refroidir avant de servir."
        ]
    },
    # Ajoutez plus de recettes ici
]
@app.route('/')
def index():
    return render_template('index.html', ingredients=ingredients_list, recipes=recipes)

@app.route('/generate_recipe')
def generate_recipe():
    random_recipe = random.choice(recipes)
    random_ingredients = random.sample(ingredients_list, 4)
    return render_template('recipe.html', recipe=random_recipe, ingredients=random_ingredients)

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    recipe_name = request.form['recipe_name']
    recipe_ingredients = request.form.getlist('recipe_ingredients')
    recipe_steps = request.form.getlist('recipe_steps')
    new_recipe = {
        "name": recipe_name,
        "ingredients": recipe_ingredients,
        "steps": recipe_steps
    }
    recipes.append(new_recipe)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)