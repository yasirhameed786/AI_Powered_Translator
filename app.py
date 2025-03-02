from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# Define a custom dictionary with specific languages
SPECIFIC_LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'ta': 'Tamil',
    'ml': 'Malayalam',
    'kn': 'Kannada'
}

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    error_msg = None
    if request.method == "POST":
        original_text = request.form.get("text")
        target_language = request.form.get("language")
        try:
            translated_text = translate_text(original_text, target_language)
        except Exception as e:
            translated_text = ""
            error_msg = str(e)
    return render_template("index.html", translated_text=translated_text, error_msg=error_msg, languages=SPECIFIC_LANGUAGES)

def translate_text(text, lang):
    try:
        translation = translator.translate(text, dest=lang)
        if translation:  # Ensure translation is not None
            return translation.text
        else:
            return "Translation was unsuccessful."
    except Exception as e:
        raise Exception(f"Failed to translate due to: {e}")

if __name__ == "__main__":
    app.run(debug=True)
