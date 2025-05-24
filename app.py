from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Predefined wordlists for band names
fantasy_words = ["Mystic", "Shadow", "Astral", "Dragon", "Lunar"]
music_words = ["Echo", "Harmony", "Pulse", "Reverb", "Chords"]
era_styles = ["Retro", "Future", "Neon", "Vintage", "Cyber"]

@app.route("/", methods=["GET", "POST"])
def band_name_generator():
    band_name = ""

    if request.method == "POST":
        city_name = request.form["city"]
        animal_name = request.form["animal"]
        genre = request.form["genre"]

        # Pick a random adjective based on genre
        genre_mapping = {
            "rock": "Thunderous",
            "pop": "Neon",
            "hip-hop": "Legendary",
            "electronic": "Cyber",
            "jazz": "Soulful"
        }
        adjective = genre_mapping.get(genre.lower(), "Epic")
        extra_word = random.choice(fantasy_words + music_words + era_styles)

        # Generate band name
        band_name = f"{adjective} {city_name} {animal_name} {extra_word}"

    return render_template("index.html", band_name=band_name)

if __name__ == "__main__":
    app.run(debug=True)