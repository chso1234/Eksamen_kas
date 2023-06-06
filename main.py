import tkinter as tk
import mysql.connector

# Koble til databasen
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="KAS"
)
cursor = db.cursor()

# Min valgte font
font = ("Georgia", 27)

# Lager funksjoner
def legg_til():
    dato = dato_entry.get()
    fornavn = fornavn_entry.get()
    etternavn = etternavn_entry.get()
    epost = epost_entry.get()
    beskrivelse = beskrivelse_entry.get()
    status = status_entry.get()
    arbeidslogg = arbeidslogg_entry.get()
    løsning = løsning_entry.get()

    sql = "INSERT INTO Henvendelser (Dato, Fornavn, Etternavn, Epost, Beskrivelse, Status, Arbeidslogg, Løsning) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (dato, fornavn, etternavn, epost, beskrivelse, status, arbeidslogg, løsning)
    cursor.execute(sql, val)
    db.commit()

def slett():
    saksID = saksID_entry.get()

    sql = f"DELETE FROM Henvendelser WHERE SaksID = '{saksID}'"
    cursor.execute(sql)
    db.commit()

def oppdater():
    saksID = saksID_entry.get()
    dato = dato_entry.get()
    fornavn = fornavn_entry.get()
    etternavn = etternavn_entry.get()
    epost = epost_entry.get()
    beskrivelse = beskrivelse_entry.get()
    status = status_entry.get()
    arbeidslogg = arbeidslogg_entry.get()
    løsning = løsning_entry.get()

    sql = "UPDATE Henvendelser SET Dato = %s, Fornavn = %s, Etternavn = %s, Epost = %s, Beskrivelse = %s, Status = %s, Arbeidslogg = %s, Løsning = %s WHERE SaksID = %s"
    val = (dato, fornavn, etternavn, epost, beskrivelse, status, arbeidslogg, løsning, saksID)
    cursor.execute(sql, val)
    db.commit()

def søk():
    saksID = saksID_entry.get()

    sql = "SELECT * FROM Henvendelser WHERE SaksID = %s"
    val = (saksID,)
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if result:
        # Håndterer resultatet av søket
        for row in result:
            print(row)  # Her kan du tilpasse hvordan du ønsker å håndtere resultatet
    else:
        print("Ingen resultater funnet for angitt SaksID.")


# Lager vinduet
root = tk.Tk()

# Lager labels
saksID_label = tk.Label(root, font=font, text="SaksID")
dato_label = tk.Label(root, font=font, text="Dato")
fornavn_label = tk.Label(root, font=font, text="Fornavn")
etternavn_label = tk.Label(root, font=font, text="Etternavn")
epost_label = tk.Label(root, font=font, text="Epost")
beskrivelse_label = tk.Label(root, font=font, text="Beskrivelse")
status_label = tk.Label(root, font=font, text="Status")
arbeidslogg_label = tk.Label(root, font=font, text="Arbeidslogg")
løsning_label = tk.Label(root, font=font, text="Løsning")

# Plassering av labels
saksID_label.grid(row=1, column=0)
dato_label.grid(row=2, column=0)
fornavn_label.grid(row=3, column=0)
etternavn_label.grid(row=4, column=0)
epost_label.grid(row=5, column=0)
beskrivelse_label.grid(row=6, column=0)
status_label.grid(row=7, column=0)
arbeidslogg_label.grid(row=8, column=0)
løsning_label.grid(row=9, column=0)

# Lager entrys
saksID_entry = tk.Entry(root, font=font)
dato_entry = tk.Entry(root, font=font)
fornavn_entry = tk.Entry(root, font=font)
etternavn_entry = tk.Entry(root, font=font)
epost_entry = tk.Entry(root, font=font)
beskrivelse_entry = tk.Entry(root, font=font)
status_entry = tk.Entry(root, font=font)
arbeidslogg_entry = tk.Entry(root, font=font)
løsning_entry = tk.Entry(root, font=font)

# Plassering av entrys
saksID_entry.grid(row=1, column=1)
dato_entry.grid(row=2, column=1)
fornavn_entry.grid(row=3, column=1)
etternavn_entry.grid(row=4, column=1)
epost_entry.grid(row=5, column=1)
beskrivelse_entry.grid(row=6, column=1)
status_entry.grid(row=7, column=1)
arbeidslogg_entry.grid(row=8, column=1)
løsning_entry.grid(row=9, column=1)

# Lager knapper
legg_til_button = tk.Button(root, text="Legg til henvendelse", font=font, command=legg_til)
legg_til_button.grid(row=11, column=1, sticky="we")

søk_button = tk.Button(root, text="Søk", font=font, command=søk)
søk_button.grid(row=12, column=1, sticky="we")

oppdater_button = tk.Button(root, text="Oppdater", font=font, command=oppdater)
oppdater_button.grid(row=14, column=1, sticky="we")

slett_button = tk.Button(root, text="Slett", font=font, command=slett)
slett_button.grid(row=15, column=1, sticky="we")

root.mainloop()
