from flask import Flask, render_template, request, jsonify
from backend import make_api_request_with_faiss
from feedback_handler import save_feedback
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Anasayfa için index.html (Mesajlaşma Botu)

@app.route('/about')
def about():
    return render_template('about.html')  # Hakkımızda sayfası için about.html

@app.route('/project')
def project():
    return render_template('project.html')  # Projemiz sayfası için project.html

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.form.get('msg', '')
    user_id = str(uuid.uuid4())  # Anonim kullanıcı kimliği

    if not user_query:
        return jsonify({"error": "No message provided"}), 400
    
    # API'den yanıtı al
    response = make_api_request_with_faiss(user_query)

    # JSON yanıtı döndür
    return jsonify({
        "answer": response,
        "user_id": user_id
    })

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    user_id = data.get('user_id')
    input_prompt = data.get('input_prompt')
    response = data.get('response')
    rating = data.get('rating')  # 'like' veya 'dislike'
    feedback_text = data.get('feedback_text', None)  # Yorum opsiyonel
    preferred_response = data.get('preferred_response', None)  # Alternatif yanıt opsiyonel
    
    # Geri bildirim kaydet
    save_feedback(user_id, input_prompt, response, rating, feedback_text, preferred_response)
    
    return jsonify({"status": "feedback saved"})

if __name__ == '__main__':
    app.run(debug=True)