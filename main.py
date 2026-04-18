import requests

sources = [
    "https://home.frozensmile.online/NP5pxlh3O7/mwypm5y31myyn5en",
    "https://eternal.frozensmile.online/v6k9-Zp2m-Rx8t-qW5y-L7n1/14dozevwyiheyw5f"
]

def get_configs():
    all_configs = []
    # Максимально подробные заголовки браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*)',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    for url in sources:
        try:
            print(f"Попытка подключения к: {url}")
            # Увеличиваем таймаут и отключаем проверку SSL
            resp = requests.get(url, timeout=45, verify=False, headers=headers) 
            
            if resp.status_code == 200:
                content = resp.text.strip()
                if content:
                    all_configs.append(content)
                    print(f"Успех! Получено данных.")
            else:
                print(f"Сервер ответил кодом: {resp.status_code}")
        except Exception as e:
            print(f"Ошибка: {str(e)}")

    output = "\n".join(all_configs) if all_configs else "No configs found"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    get_configs()
