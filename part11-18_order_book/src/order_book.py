# Write your solution here:
class Task:
    id_counter = 0

    def __init__(self, description: str, name: str, workload: int):
        self.__description = description
        self.__workload = workload
        self.__name = name 
        Task.id_counter += 1
        self.__id = Task.id_counter
        self.__is_finished = False

    @property
    def id(self):
        return self.__id

    @property
    def description(self):
        return self.__description

    @property 
    def programmer(self):
        return self.__name

    @property
    def workload(self):
        return self.__workload
    
    def is_finished(self):
        return self.__is_finished

    def mark_finished(self):
        self.__is_finished = True
        return self.__is_finished

    def __str__(self):
        status = "FINISHED" if self.__is_finished else "NOT FINISHED"
        return (f"{self.__id}: {self.__description} ({self.__workload} hours), programmer {self.__name} {status}")

class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self.tasks.append(order)

    def all_orders(self):
        return self.tasks

    def programmers(self):
        seen = set()
        result = []
        for task in self.tasks:
            if task.programmer not in seen:
                seen.add(task.programmer)
                result.append(task.programmer)
        return result


    def mark_finished(self, id: int):
        for task in self.tasks:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError("no id")

    def finished_orders(self):
        finished_list = []
        for task in self.tasks:
            if task.is_finished():
                finished_list.append(task)

        return finished_list

    def unfinished_orders(self):
        unfinished_list = []
        for task in self.tasks:
            if not task.is_finished():
                unfinished_list.append(task)

        return unfinished_list
  


if __name__ == "__main__":

    # t1 = Task("program hello world", "Eric", 3)
    # print(t1.id, t1.description, t1.programmer, t1.workload)
    # print(t1)
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task("program webstore", "Adele", 10)
    # t3 = Task("program mobile app for workload accounting", "Eric", 25)
    # print(t2)
    # print(t3)

    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # for order in orders.all_orders():
    #     print(order)

    # print()

    # for programmer in orders.programmers():
    #     print(programmer)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(1)
    orders.mark_finished(2)

    for order in orders.all_orders():
        print(order)