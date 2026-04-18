import requests
import sys

# Твои ссылки. Проверь их внимательно!
sources = [
    "https://home.frozensmile.online/NP5pxlh3O7/",
    "https://eternal.frozensmile.online//v6k9-Zp2m-Rx8t-qW5y-L7n1/"
]

def get_configs():
    all_configs = []
    print(f"Python version: {sys.version}")
    
    for url in sources:
        if "ВАШ_ПУТЬ" in url:
            print(f"Пропустил ссылку: {url} (нужно заменить на реальную)")
            continue
            
        try:
            print(f"Запрашиваю: {url}")
            # Добавили verify=False на случай проблем с SSL сертификатами
            resp = requests.get(url, timeout=15, verify=False) 
            
            if resp.status_code == 200:
                content = resp.text.strip()
                if content:
                    all_configs.append(content)
                    print(f"Успех! Получено символов: {len(content)}")
                else:
                    print(f"Ошибка: Сервер {url} вернул пустой ответ")
            else:
                print(f"Ошибка: Сервер {url} вернул статус {resp.status_code}")
                
        except Exception as e:
            print(f"Критическая ошибка при запросе {url}: {str(e)}")

    # Сохраняем результат в любом случае, чтобы скрипт не падал с ошибкой
    output_content = "\n".join(all_configs) if all_configs else "No configs found"
    
    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(output_content)
        print("Файл index.html успешно обновлен.")
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")

if __name__ == "__main__":
    get_configs()
