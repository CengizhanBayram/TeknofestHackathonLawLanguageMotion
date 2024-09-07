*Bu proje TEKNOFEST 2024 Antalya T3AI Hackathon Yarışması Uygulama Geliştirme Kategorisi için geliştirilmiştir.*

# Law Language Motion

## Projede neyin amaçlandığını bir cümle ile özetleme: 
Hukuk öğrencilerinin karmaşık hukuki bilgilere erişim ve anlamada yaşadığı zorlukları, yapay zeka destekli öğretici chatbot ile çözerek öğrenme süreçlerini daha etkili ve kişiselleştirilmiş hale getirmeyi amaçlıyoruz.

## Takım Adı: Law Language Motion
- 👤 Cengizhan Bayram
- 👤 Ferhat Kürkçüoğlu

## Uygulamadan Ekran Görüntüleri

![Uygulama Ekranı 1](image1.png)
![Uygulama Ekranı 2](image2.png)

## Uygulamayı Lokalde Çalıştırma

1. **Depoyu klonlayın:**
    ```bash
    git clone https://github.com/CengizhanBayram/TeknofestHackathonLawLanguageMotion.git
    ```

2. **Gerekli paketleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3. **API Anahtarlarını Tanımlayın:**
    - T3AI BDM API anahtarınızı `.env` dosyasına ekleyin.

4. **Veritabanı Ayarları:**
    Faiss veritabanınızı oluşturun:
    ```bash
    python create_faiss_db.py
    ```

5. **Uygulamayı Başlatın:**
    ```bash
    python main.py
    ```

6. **Kullanım:**
    - Chatbot'a hukuki sorularınızı sorun ve yanıtları alın.
