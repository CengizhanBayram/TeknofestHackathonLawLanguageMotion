import json
import uuid
from datetime import datetime
import platform

def guess_device_type() -> str :
    os_name = platform.system().lower()
    device_type = "Unknown Device"
    
    if os_name == 'windows':
        device_type = "Desktop or Laptop"
    elif os_name == 'darwin':
        device_type = "Mac Desktop or Laptop"
    elif os_name == 'linux':
        # Linux dağıtımlarında cihaz tahmin etmek zor olabilir.
        # Burada mobil cihazları ayırt etmek için daha fazla kontrol ekleyebilirsin.
        device_type = "Desktop or Laptop"
        
        # Örnek olarak Android kontrolü:
        if 'android' in platform.platform().lower():
            device_type = "Android Mobile or Tablet"
    elif os_name == 'java':
        device_type = "Mobile Device"
    elif os_name == 'android':
        device_type = "Android Mobile or Tablet"
    elif 'ios' in platform.platform().lower():
        device_type = "iOS Mobile or Tablet"

    return device_type

# Kullanım örneği:
device = guess_device_type()
print(f"Device type: {device}")

# Geri bildirim kaydetme fonksiyonu
def save_feedback(user_id, input_prompt, response, rating, feedback_text=None, preferred_response=None, device="desktop"):
    """
    Geri bildirimi kaydeder. Bu fonksiyon, JSON formatında bir log oluşturur ve bir dosyaya yazar.
    Dosya yoksa otomatik olarak oluşturur.
    """
    interaction_data = {
        "interaction_id": str(uuid.uuid4()),  # Benzersiz bir kimlik numarası oluştur
        "user_id": user_id,  # Anonim kullanıcı kimliği
        "timestamp": datetime.utcnow().isoformat() + "Z",  # Zaman damgası ISO 8601 formatında
        "content_generated": {
            "input_prompt": input_prompt,
            "response": response
        },
        "user_feedback": {
            "rating": rating,  # Kullanıcının beğenme/beğenmeme durumu ("like" veya "dislike")
            "feedback_text": feedback_text,  # Kullanıcının yorumu
            "preferred_response": preferred_response  # Kullanıcının beklediği alternatif yanıt
        },
        "feedback_metadata": {
            "device": guess_device_type(),  # Geri bildirimin alındığı cihaz (varsayılan: desktop)
            "location": "Unknown",  # İsteğe bağlı olarak coğrafi konum eklenebilir
            "session_duration": 0  # Oturum süresi burada sabit, dinamik hale getirilebilir
        }
    }

    # JSON dosyasını açma ve yazma, dosya yoksa oluşturulur
    with open("feedback_log.json", "a+") as f:
        # Dosyaya JSON formatında yazma
        json.dump(interaction_data, f, ensure_ascii=False, indent=4)  # JSON formatında kaydet
        f.write("\n")  # Her etkileşim yeni satıra yazılsın

# Örnek kullanım (isteğe bağlı, test için)
if __name__ == "__main__":
    save_feedback(
        user_id="user_001",
        input_prompt="Verimliliğimi nasıl artırabilirim?",
        response="İşte verimliliğinizi artırmak için bazı ipuçları...",
        rating="dislike",
        feedback_text="İpuçları çok genel kalmış.",
        preferred_response="Zaman yönetimi üzerine daha spesifik örnekler verin."
    )
