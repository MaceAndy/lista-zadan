class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if index >= 0 and index < len(self.tasks):
            del self.tasks[index]

    def complete_task(self, index):
        if index >= 0 and index < len(self.tasks):
            self.tasks[index].completed = True

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("Lista zadań jest pusta.")
        else:
            print("Lista zadań:")
            for index, task in enumerate(self.tasks):
                status = "✓" if task.completed else "◻"
                print(f"{index + 1}. [{status}] {task.description}")

def main():
    todo_list = TodoList()

    while True:
        print("\nCo chcesz zrobić?")
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Oznacz zadanie jako wykonane")
        print("4. Wyświetl listę zadań")
        print("5. Zakończ program")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            description = input("Podaj opis zadania: ")
            todo_list.add_task(description)
            print("Zadanie dodane.")

        elif choice == "2":
            index = int(input("Podaj numer zadania do usunięcia: ")) - 1
            todo_list.remove_task(index)
            print("Zadanie usunięte.")

        elif choice == "3":
            index = int(input("Podaj numer zadania do oznaczenia jako wykonane: ")) - 1
            todo_list.complete_task(index)
            print("Zadanie oznaczone jako wykonane.")

        elif choice == "4":
            todo_list.display_tasks()

        elif choice == "5":
            print("Program zakończony.")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()