tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Задача '{task}' добавлена.")

def show_tasks():
    print("Список задач:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Задача '{removed}' удалена.")

def clear_tasks():
    tasks.clear()
    print("Список очищен.")
if __name__ == "__main__":
    add_task("Настроить Git")
    show_tasks()