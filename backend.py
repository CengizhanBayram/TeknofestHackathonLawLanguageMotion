import json
import os
import requests
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # Ortam değişkeninden API anahtarını alıyoruz
# Embedding modeli ve FAISS veritabanını başlatıyoruz
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", api_key=api_key)

# FAISS veritabanını yüklüyoruz
faiss_db_path = r"C:\Users\cengh\Desktop\PlanC\faiss_index_openai"
faiss_db = FAISS.load_local(faiss_db_path, embedding_model, allow_dangerous_deserialization=True)

# FAISS sorgulama fonksiyonu
def retrieve_from_faiss(query):
    docs = faiss_db.similarity_search(query, k=3)  # En yakın 3 belgeyi getiriyoruz
    return docs

# JSON verisini özel formata dönüştürme fonksiyonu
def convert_to_special_format(json_data):
    output = "<|begin_of_text|>"
    for entry in json_data:
        if entry["role"] == "system":
            output += f'<|start_header_id|>system<|end_header_id|>\n\n{entry["content"]}<|eot_id|>'
        elif entry["role"] == "user":
            output += f'\n<|start_header_id|>{entry["role"]}<|end_header_id|>\n\n{entry["content"]}<|eot_id|>'
        elif entry["role"] == "assistant":
            output += f'\n<|start_header_id|>{entry["role"]}<|end_header_id|>\n\n{entry["content"]}<|eot_id|>'
    output += "\n<|start_header_id|>assistant<|end_header_id|>"
    return output
    

# API isteği ve FAISS entegrasyonu
def make_api_request_with_faiss(query):
    # FAISS'ten belgeleri al
    retrieved_docs = retrieve_from_faiss(query)
    
    # Belgeleri API'ye göndermek için hazırlıyoruz
    retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])
    
    json_data = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query},
        {"role": "assistant", "content": retrieved_text}
    ]

    special_format_output = convert_to_special_format(json_data)
    print("Special Format Output:", special_format_output)
    # API isteği
    url = "https://inference2.t3ai.org/v1/completions"
    payload = json.dumps({
        "model": "/home/ubuntu/hackathon_model_2/",
        "prompt": special_format_output,
        "temperature": 0.3,
        "top_p": 0.9,
        "max_tokens": 1024,
        "repetition_penalty": 1.1,
        "stop_token_ids": [128001, 128009],
        "skip_special_tokens": True
    })

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        pretty_response = json.loads(response.text)
        assistant_reply = pretty_response['choices'][0]['text']
        return assistant_reply
    else:
        return f"Error: {response.status_code} - {response.text}"

# Kullanıcı sorgusu ile API'den yanıt alıyoruz
query = "Ticaret hukuku nedir?"
response = make_api_request_with_faiss(query)
print("Assistant Reply:", response)
