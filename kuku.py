import os
import datetime

DATA_FILE = "kuku_data.txt"

def save_entry(text):
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(f"[{timestamp}] {text}\n")
    print("✔ Zapisano wpis.")

def show_entries():
    if not os.path.exists(DATA_FILE):
        print("Brak wpisów.")
        return

    print("\n=== Wpisy Kuku ===")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        print(f.read())

def main():
    while True:
        print("\n--- Kuku CLI ---")
        print("1. Dodaj wpis")
        print("2. Pokaż wpisy")
        print("3. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            text = input("Wpis: ")
            save_entry(text)
        elif choice == "2":
            show_entries()
        elif choice == "3":
            print("Do zobaczenia!")
            break
        else:
            print("Niepoprawny wybór.")

if __name__ == "__main__":
    main()
