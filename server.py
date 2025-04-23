from flask import Flask, jsonify, request

# Creación de la aplicación Flask
app = Flask(__name__)

# Datos simulados de ejemplo (base de datos simulada)
data_store = [
    {'id': 1, 'name': 'Primer elemento', 'description': 'Este es el primer elemento'},
    {'id': 2, 'name': 'Segundo elemento', 'description': 'Este es el segundo elemento'}
]

# Ruta principal: Mensaje de bienvenida
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': '¡Bienvenido a mi API JSON!',
        'status': 'success'
    })

# GET: Obtener los metadatos de la música
@app.route('/metadata', methods=['GET'])
def get_metadata():
    return jsonify({
        'artista': 'Ejemplo',
        'titulo': 'Canción',
        'caratula': 'https://example.com/caratula.jpg'
    })

# GET: Obtener la URL del streaming
@app.route('/stream', methods=['GET'])
def get_stream_url():
    return jsonify({
        'streaming_url': "https://mox.moxapps.shop/stream"
    })

# GET: Obtener todos los elementos
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({
        'message': 'Elementos obtenidos correctamente',
        'data': data_store
    })

# GET: Obtener un elemento por ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Buscar elemento por ID
    item = next((item for item in data_store if item['id'] == item_id), None)
    if item:
        return jsonify({
            'message': 'Elemento obtenido correctamente',
            'data': item
        })
    else:
        return jsonify({
            'message': 'Elemento no encontrado',
            'error': True
        }), 404

# POST: Agregar un nuevo elemento
@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.json  # Leer datos enviados en formato JSON
    if 'id' not in new_item or 'name' not in new_item or 'description' not in new_item:
        return jsonify({
            'message': 'Faltan datos necesarios (id, name, description)',
            'error': True
        }), 400
    
    # Agregar el nuevo elemento
    data_store.append(new_item)
    return jsonify({
        'message': 'Elemento agregado correctamente',
        'data': new_item
    }), 201

# PUT: Actualizar un elemento existente
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.json  # Leer datos enviados en formato JSON
    item = next((item for item in data_store if item['id'] == item_id), None)
    if item:
        item.update(updated_item)  # Actualizar los campos del elemento
        return jsonify({
            'message': 'Elemento actualizado correctamente',
            'data': item
        })
    else:
        return jsonify({
            'message': 'Elemento no encontrado',
            'error': True
        }), 404

# DELETE: Eliminar un elemento por ID
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data_store
    item = next((item for item in data_store if item['id'] == item_id), None)
    if item:
        data_store = [i for i in data_store if i['id'] != item_id]  # Filtrar la lista
        return jsonify({
            'message': 'Elemento eliminado correctamente'
        })
    else:
        return jsonify({
            'message': 'Elemento no encontrado',
            'error': True
        }), 404

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
