from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemple de fonction pour simuler une réponse du chatbot
def chatbot_response(user_input):
    return f"Vous avez dit : {user_input}"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)