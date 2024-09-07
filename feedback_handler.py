import json
import uuid
from datetime import datetime

def save_feedback(user_id, input_prompt, response, rating, feedback_text=None, preferred_response=None):
    feedback_log = 'feedback_log.json'  # JSON dosyasının yolu

    # Yeni geri bildirim verisi oluşturma
    interaction_data = {
        "interaction_id": str(uuid.uuid4()),  # Benzersiz kimlik
        "user_id": user_id,  # Anonim kullanıcı kimliği
        "timestamp": datetime.utcnow().isoformat() + "Z",  # ISO 8601 zaman damgası
        "content_generated": {
            "input_prompt": input_prompt,
            "response": response
        },
        "user_feedback": {
            "rating": rating,  # Kullanıcının verdiği puan ("like" veya "dislike")
            "feedback_text": feedback_text if feedback_text else "",  # Opsiyonel yorum
            "preferred_response": preferred_response if preferred_response else ""  # Opsiyonel alternatif yanıt
        },
        "feedback_metadata": {
            "device": "desktop",  # Varsayılan olarak 'desktop'
            "location": "Unknown",  # Coğrafi konum boş bırakıldı
            "session_duration": 0  # Bu dinamik hale getirilebilir
        }
    }

    # Mevcut JSON dosyasını kontrol et
    try:
        with open(feedback_log, 'r', encoding='utf-8') as file:
            feedback_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        feedback_data = []  # Dosya bulunamazsa veya bozuksa yeni liste oluştur

    # Yeni veriyi ekle
    feedback_data.append(interaction_data)

    # JSON dosyasını kaydet
    with open(feedback_log, 'w', encoding='utf-8') as file:
        json.dump(feedback_data, file, ensure_ascii=False, indent=4)  # JSON dosyasına düzgün formatta yaz