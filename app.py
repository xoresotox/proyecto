# app.py
from flask import Flask, request, render_template_string, redirect
import subprocess

app = Flask(__name__)

# Aqui inicia la busqueda normal


@app.route('/')
def index():
    with open('simple_search.html', 'r') as file:
        html_content = file.read()
    return render_template_string(html_content)


@app.route('/search')
def search():
    query = request.args.get('q')
    result = subprocess.run(['perl', 'simple_search.pl', query],
                            capture_output=True, text=True)
    return result.stdout


# Aqui inicia la busqueda de imagenes con su recibidor
@app.route('/image_search', methods=['GET', 'POST'])
def busqueda_imagenes():
    with open('image_search.html', 'r') as file:
        html_content = file.read()
    return render_template_string(html_content)


@app.route('/img_search', methods=['GET'])
def img_search():
    query = request.args.get('q')
    google_image_search_url = f"https://www.google.com/search?tbm=isch&q={
        query}"
    return redirect(google_image_search_url)


# Aqui inicia la busqueda avanzada con su recibidor
@app.route('/advanced_search', methods=['GET', 'POST'])
def busqueda_avanzada():
    if request.method == 'POST':
        all_words = request.form.get('all_words')
        exact_phrase = request.form.get('exact_phrase')
        none_words = request.form.get('none_words')

        google_advanced_search_url = f"https://www.google.com/search?as_q={
            all_words}&as_epq={exact_phrase}&as_eq={none_words}"
        return redirect(google_advanced_search_url)

    with open('advanced_search.html', 'r') as file:
        html_content = file.read()
    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(debug=True)
