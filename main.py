import requests
import base64

sources = [
    "https://home.frozensmile.online/NP5pxlh3O7/mwypm5y31myyn5en",
    "https://eternal.frozensmile.online/v6k9-Zp2m-Rx8t-qW5y-L7n1/14dozevwyiheyw5f"
]

def get_configs():
    all_configs = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/123.0.0.0 Safari/537.36'}
    
    for url in sources:
        try:
            resp = requests.get(url, timeout=30, verify=False, headers=headers) 
            if resp.status_code == 200 and resp.text.strip():
                all_configs.append(resp.text.strip())
        except:
            pass

    if all_configs:
        # Склеиваем все конфиги через перенос строки
        combined_text = "\n".join(all_configs)
        # Кодируем в Base64 (стандарт для v2box/Shadowrocket)
        encoded_configs = base64.b64encode(combined_text.encode('utf-8')).decode('utf-8')
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(encoded_configs)
    else:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write("No configs")

if __name__ == "__main__":
    get_configs()
