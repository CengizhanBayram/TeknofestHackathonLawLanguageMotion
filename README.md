# TeknofestHackathonLawLanguageMotion

# Law Language Motion - Hukuk Öğrencileri İçin Öğretici Chatbot

**Law Language Motion**, hukuk öğrencilerine yönelik geliştirilmiş bir öğretici chatbot’tur. Proje, öğrencilerin hukuki bilgilere hızlı ve bağlamsal bir şekilde erişmelerine yardımcı olurken, kişiselleştirilmiş bir öğrenme deneyimi sunar. Faiss veritabanı ve Langchain framework’ü ile desteklenen chatbot, hukuki belgeleri tarar ve T3AI BDM API kullanarak en uygun yanıtları üretir.

## Özellikler
- **Kişiselleştirilmiş Öğrenme Deneyimi**: Hukuk öğrencilerinin öğrenme süreçlerine özel yanıtlar.
- **Bağlamsal Yanıtlar**: T3AI BDM API ve RAG modeli kullanarak doğru ve anlamlı sonuçlar sunar.
- **Hızlı Veri Arama**: Faiss veritabanı ile hukuki belgeler arasında hızlı ve etkili arama yapılır.
- **Öğrenci Geri Bildirimi**: Öğrenciler, aldıkları yanıtlar üzerinde geri bildirimde bulunarak öğrenme sürecini iyileştirir.

## Kullanılan Teknolojiler
- **Faiss Veritabanı**: Büyük veri setlerinde hızlı arama ve eşleştirme.
- **Langchain Framework**: Doğal dil işleme ve bağlam anlama.
- **T3AI BDM API**: Bağlamsal veri işleme ve generative yapıda yanıtlar oluşturma.
- **RAG (Retrieval-Augmented Generation) Modeli**: Öğrenci sorularına uygun yanıtlar üretir.

## Kurulum

1. **Depoyu klonlayın:**
    ```bash
    git clone https://github.com/kullanici_adi/law-language-motion.git
    ```

2. **Gerekli paketleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3. **API Anahtarlarını Tanımlayın:**
    - T3AI BDM API anahtarınızı `.env` dosyasına ekleyin.

4. **Veritabanı Ayarları:**
    Faiss veritabanınızı oluşturarak veri setinizi yükleyin:
    ```bash
    python create_faiss_db.py
    ```

## Kullanım

1. **Chatbot'u Başlatın:**
    ```bash
    python main.py
    ```

2. **Soru Sorun:**
   Chatbot'u başlattıktan sonra, hukuki bir soruyu girin ve bağlamsal yanıt alın.

## Katkı

Katkıda bulunmak istiyorsanız, lütfen önce bir issue açın. Değişiklikler için lütfen bir pull request gönderin.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına bakın.
