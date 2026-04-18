import requests
import base64

# Твои ссылки
sources = [
    "https://home.frozensmile.online/NP5pxlh3O7/mwypm5y31myyn5en",
    "https://eternal.frozensmile.online/v6k9-Zp2m-Rx8t-qW5y-L7n1/14dozevwyiheyw5f"
]

def get_configs():
    all_configs = []
    # Минималистичные заголовки, чтобы сервер не тратил время на анализ
    headers = {
        'User-Agent': 'v2rayN/6.33', # Притворяемся популярным клиентом
        'Accept': '*/*'
    }
    
    for url in sources:
        try:
            print(f"Connecting to: {url}")
            # verify=False обязателен, если есть проблемы с сертификатами
            resp = requests.get(url, timeout=30, verify=False, headers=headers) 
            
            if resp.status_code == 200:
                raw_data = resp.text.strip()
                if raw_data:
                    # Если данные уже в base64 (что часто бывает в 3x-ui), декодируем их сначала
                    try:
                        decoded = base64.b64decode(raw_data).decode('utf-8')
                        all_configs.append(decoded)
                    except:
                        all_configs.append(raw_data)
                    print(f"Success for {url}")
        except Exception as e:
            print(f"Skip {url} due to error: {e}")

    if all_configs:
        # Склеиваем всё в одну кучу
        combined = "\n".join(all_configs)
        # Кодируем финальный результат в Base64 для v2box
        final_base64 = base64.b64encode(combined.encode('utf-8')).decode('utf-8')
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(final_base64)
        print("File index.html updated and encoded in Base64.")
    else:
        print("No data collected.")

if __name__ == "__main__":
    get_configs()
