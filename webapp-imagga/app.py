from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Credenciales de la API de Imagga
IMAGGA_API_KEY = 'acc_01b94e1ed3934f6'
IMAGGA_API_SECRET = '1342ddff8b7afea131b11d2641735136'
TAGS_ENDPOINT = 'https://api.imagga.com/v2/tags'

# Lista de imágenes
images = [
    'https://images.unsplash.com/photo-1525253086316-d0c936c814f8',
    'https://images.unsplash.com/photo-1517423440428-a5a00ad493e8',
    'https://images.unsplash.com/photo-1574158622682-e40e69881006'
]

@app.route('/')
def home():
    return render_template('index.html', images=images)

@app.route('/analyze', methods=['POST'])
def analyze():
    image_url = request.form.get('image_url')
    if not image_url:
        return redirect(url_for('home'))
    
    try:
        response = requests.get(
            TAGS_ENDPOINT,
            auth=(IMAGGA_API_KEY, IMAGGA_API_SECRET),
            params={'image_url': image_url}
        )
        response.raise_for_status()
        
        data = response.json()
        tags = data.get('result', {}).get('tags', [])[:2]  # Tomar solo las dos primeras etiquetas
        return render_template('result.html', image_url=image_url, tags=tags)
    except requests.exceptions.RequestException as e:
        return f"Error al conectar con Imagga: {e}", 500
    except ValueError:
        return f"Error al procesar JSON: {response.text}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)