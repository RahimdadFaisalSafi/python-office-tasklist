# Aufgabenliste anlegen
tasks = []

# Funktion zum Hinzufügen einer Aufgabe
def add_task():
    task = input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: ")
    due_date = input("Möchtest du ein Fälligkeitsdatum angeben? (optional, drücke Enter um zu überspringen): ")

    # Aufgabe mit oder ohne Fälligkeitsdatum zur Liste hinzufügen
    if due_date:
        tasks.append({"Aufgabe": task, "Fälligkeitsdatum": due_date})
        print(f"Die Aufgabe '{task}' mit Fälligkeitsdatum {due_date} wurde zur Liste hinzugefügt.")
    else:
        tasks.append({"Aufgabe": task})
        print(f"Die Aufgabe '{task}' wurde zur Liste hinzugefügt.")

add_task()
