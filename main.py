from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'sk-proj-eW6PKt8h7ZLaEMwmBoFZT3BlbkFJ3AoyigKzcuN4ND6LAC15'

@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    data = request.json
    user_message = data.get('message')
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    
    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(debug=True)
