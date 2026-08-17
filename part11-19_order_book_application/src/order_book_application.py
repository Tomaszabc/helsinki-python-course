# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task:
    id = 0
    @classmethod
    def new_id(cls):
        Task.id += 1
        return Task.id

    def __init__(self, description, programmer, workload):
        self.programmer = programmer
        self.description = description
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False

    def is_finished(self):
        return self.finished
 
    def mark_finished(self):
        self.finished = True
 
    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self.__tasks = []

    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.__tasks

    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))

    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError("Wrong ID")

    def unfinished_orders(self):
        return [t for t in self.__tasks if not t.is_finished()]

    def finished_orders(self):
        return [t for t in self.__tasks if t.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exist")
        
        finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished()]
        not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished()]

        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)

        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)


class OrderBookApplication:
    def __init__(self):
        self.__order_book = OrderBook()

    def help(self):
        instructions_str = """
commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer"""
        print(instructions_str)

    def add_order(self):
        description = input("description: ")
        programmer_workload = input("programmer and workload estimate: ")

        try:
            parts = programmer_workload.rsplit(" ", 1)
            if len(parts) != 2:
                raise ValueError
            programmer = parts[0]
            workload = int(parts[1])
            self.__order_book.add_order(description, programmer, workload)
            print("added!")
        except ValueError:
            print("erroneous input")

    def list_finished(self):
        finished = self.__order_book.finished_orders()
        if not finished:
            print("no finished tasks")
        else: 
            for task in finished:
                print(task)

    def list_unfinished(self):
        unfinished = self.__order_book.unfinished_orders()
        for task in unfinished:
            print(task)

    def mark_finished(self):
        task_id = input("id: ")
        try:
            task_id = int(task_id)
            self.__order_book.mark_finished(task_id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def list_programmers(self):
        for programmer in self.__order_book.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            finished, unfinished, finished_hours, unfinished_hours = self.__order_book.status_of_programmer(programmer)
            print(f"tasks: finished {finished} not finished {unfinished}, hours: done {finished_hours} scheduled {unfinished_hours}")
        except ValueError:
             print("erroneous input")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished()
            elif command == "3":
                self.list_unfinished()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                print("Unknown command")

app = OrderBookApplication()
app.execute()