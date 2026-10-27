
# Danh sách lưu các công việc
tasks = []


# Thêm công việc
def add_task(task_name):
    task = {
        "name": task_name,
        "completed": False
    }
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")


# Liệt kê tất cả công việc
def list_tasks():
    print("\nDanh sách công việc:")

    if len(tasks) == 0:
        print("Chưa có công việc nào!")
        return

    for i, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "[x]"
        else:
            status = "[ ]"

        print(f"{i}. {status} {task['name']}")


# Đánh dấu công việc hoàn thành
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print("Chỉ số công việc không hợp lệ!")


# Xóa công việc
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Đã xóa công việc: {deleted_task['name']}")
    else:
        print("Chỉ số công việc không hợp lệ!")


# Điểm bắt đầu chương trình
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")

    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

    list_tasks()

    complete_task(0)
    list_tasks()

    delete_task(1)
    list_tasks()
