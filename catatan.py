import os

def load_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        return notes
    return []

def save_notes(notes):
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(note + "\n")

def add_note():
    note = input("Tulis catatan baru: ")
    notes.append(note)
    save_notes(notes)
    print("Catatan ditambahkan.")

def show_notes():
    if notes:
        print("\nCatatan:")
        for i, note in enumerate(notes):
            print(f"{i+1}. {note.strip()}")
    else:
        print("Tidak ada catatan.")

def main():
    global notes
    notes = load_notes()
    
    while True:
        print("\n1. Tambah Catatan\n2. Lihat Catatan\n3. Keluar")
        choice = input("Pilih opsi: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
