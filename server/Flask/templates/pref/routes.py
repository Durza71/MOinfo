from flask import Blueprint, render_template, request, redirect, url_for

pref_bp = Blueprint("pref", __name__, template_folder="templates/pref")

categories = [
    "Technology", "Science", "Health", "Finance", "Sports", 
    "Education", "Entertainment", "Politics", "Travel", "Food"
    # This list can be much longer
]

@pref_bp.route("/pref", methods=["GET", "POST"])
def preferences():
    if request.method == "POST":
        # Grab selected categories and interest levels
        selected_categories = request.form.getlist("category")
        interests = {cat: request.form.get(f"interest_{cat}") for cat in selected_categories}
        with Session as session:
            for interest in interests:

        return redirect(url_for("preferences"))

    return render_template("pref/pref.html", categories=categories)
