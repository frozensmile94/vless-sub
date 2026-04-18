import requests
import os

# Твои ссылки
sources = [
    "https://home.frozensmile.online/NP5pxlh3O7/mwypm5y31myyn5en",
    "https://eternal.frozensmile.online/v6k9-Zp2m-Rx8t-qW5y-L7n1/14dozevwyiheyw5f" # ЗАМЕНИ ЭТО, ЕСЛИ ЕСТЬ
]

def run():
    results = []
    print("--- Начало сбора конфигов ---")
    
    for url in sources:
        if "ВАШ_ПУТЬ" in url:
            print(f"Propustil shablonnuyu ssilku: {url}")
            continue
            
        try:
            print(f"Proveryayu: {url}")
            # Отключаем проверку SSL и ставим долгий таймаут
            r = requests.get(url, timeout=20, verify=False)
            if r.status_code == 200 and r.text.strip():
                results.append(r.text.strip())
                print(f"Uspeh! Polucheno: {len(r.text)} simvolov")
            else:
                print(f"Oshibka: Status {r.status_code} dlya {url}")
        except Exception as e:
            print(f"Ne udalos' podkluchit'sa k {url}: {e}")

    # Сохраняем результат
    content = "\n".join(results) if results else "No configs collected yet"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("--- Gotovo! Fail index.html sozdan ---")

if __name__ == "__main__":
    run()
