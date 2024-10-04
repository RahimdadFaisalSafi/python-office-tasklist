from datetime import datetime, timedelta
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

# Funktion zum Anzeigen der Aufgabenliste
def show_tasklist():
    if not tasks:
        print("Deine Aufgabenliste ist leer.")
    else:
        print("Deine Aufgabenliste:")
        today = datetime.today()

        for task in tasks:
            task_str = f"- {task['Aufgabe']}"
            if "Fälligkeitsdatum" in task:
                due_date = datetime.strptime(task["Fälligkeitsdatum"], "%Y-%m-%d")
                task_str += f" (Fällig bis: {due_date.strftime('%Y-%m-%d')})"
                
                # Markiere Aufgaben in Rot, die innerhalb von 2 Tagen fällig sind
                if due_date <= today + timedelta(days=2):
                    task_str = f"\033[91m{task_str}\033[0m"  # ANSI Escape für rote Schrift
            print(task_str)


show_tasklist()
