import requests
import base64

sources = [
    "https://home.frozensmile.online/NP5pxlh3O7/",
    "https://eternal.frozensmile.online/v6k9-Zp2m-Rx8t-qW5y-L7n1/"
]

def get_configs():
    all_configs = []
    for url in sources:
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                # Декодируем base64 если нужно, или берем как есть
                content = resp.text
                all_configs.append(content)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    
    with open("index.html", "w") as f:
        # Объединяем все ссылки через перенос строки
        f.write("\n".join(all_configs))

if __name__ == "__main__":
    get_configs()
