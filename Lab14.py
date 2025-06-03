import os
import json
from datetime import datetime

DIARY_FILE = "travel_diary.json"

# Завантажити записи
def load_diary():
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Зберегти записи
def save_diary(entries):
    with open(DIARY_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=4)

# Додати новий запис
def add_entry():
    date_str = input("Введіть дату (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("❌ Невірний формат дати. Спробуйте ще раз.")
        return
    location = input("Введіть локацію: ").strip()
    text = input("Введіть текст запису:\n").strip()
    if not (date_str and location and text):
        print("❌ Усі поля обов’язкові.")
        return
    entries = load_diary()
    entries.append({"date": date_str, "location": location, "text": text})
    save_diary(entries)
    print("✅ Запис додано.")

# Пошук за датою або ключовим словом
def search_entries():
    entries = load_diary()
    query = input("Введіть дату (YYYY-MM-DD) або ключове слово для пошуку: ").strip().lower()
    if not query:
        print("❌ Пошуковий запит порожній.")
        return
    results = []
    for e in entries:
        if query == e["date"].lower() or query in e["text"].lower() or query in e["location"].lower():
            results.append(e)
    if not results:
        print("🔍 Записи за запитом не знайдено.")
    else:
        print(f"\nЗнайдено {len(results)} запис(ів):")
        for r in results:
            print(f"Дата: {r['date']}\nЛокація: {r['location']}\nТекст: {r['text']}\n{'-'*40}")

# Аналітика подорожей
def analyze_diary():
    entries = load_diary()
    if not entries:
        print("Щоденник порожній.")
        return
    unique_locations = set(e["location"].lower() for e in entries)
    total_words = sum(len(e["text"].split()) for e in entries)
    print("\n📊 Аналітика подорожей:")
    print(f"Кількість унікальних локацій: {len(unique_locations)}")
    print(f"Загальна кількість записів: {len(entries)}")
    print(f"Загальна кількість слів у записах: {total_words}")

# Меню
def menu():
    while True:
        print("\nМеню:")
        print("1. Додати запис")
        print("2. Пошук у щоденнику")
        print("3. Аналітика подорожей")
        print("0. Вийти")
        choice = input("Оберіть дію: ").strip()
        if choice == "1":
            add_entry()
        elif choice == "2":
            search_entries()
        elif choice == "3":
            analyze_diary()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    menu()
