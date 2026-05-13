from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Lista em memória para armazenar usuários
usuarios = []

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'mensagem': 'bem vindo ao site'
    }), 200


# GET - listar todos os usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)


# POST - adicionar usuário
@app.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    dados = request.get_json()

    if not dados or 'nome' not in dados:
        return jsonify({
            'erro': 'O campo "nome" é obrigatório'
        }), 400

    usuario = {
        'id': len(usuarios) + 1,
        'nome': dados['nome']
    }

    usuarios.append(usuario)

    return jsonify({
        'mensagem': 'Usuário adicionado com sucesso',
        'usuario': usuario
    }), 201


# PUT - atualizar usuário por ID
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados = request.get_json()

    if not dados or 'nome' not in dados:
        return jsonify({
            'erro': 'O campo "nome" é obrigatório'
        }), 400

    for usuario in usuarios:
        if usuario['id'] == id:
            usuario['nome'] = dados['nome']

            return jsonify({
                'mensagem': 'Usuário atualizado com sucesso',
                'usuario': usuario
            }), 200

    return jsonify({
        'erro': 'Usuário não encontrado'
    }), 404


# DELETE - remover usuário por ID
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):

    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)

            return jsonify({
                'mensagem': 'Usuário removido com sucesso'
            }), 200

    return jsonify({
        'erro': 'Usuário não encontrado'
    }), 404


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)