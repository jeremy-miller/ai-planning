class HierarchicalTaskNetwork:
    def __init__(self):
        self.primitive_tasks = ["Attack", "Patrol", "Guard"]
        self.methods = [
            Method("Secure by attacking", "Secure Area", ["Attack", "Patrol"]),
            Method("Secure by guarding", "Secure Area", ["Guard", "Patrol"]),
        ]

    def get_plan(self, task):
        if task.primitive:
            return [task.name]  # base case

        for method in self.methods:
            if method.task == task.name:
                plan = []
                for subtask_name in method.subtasks:
                    subtask = Task(subtask_name, subtask_name in self.primitive_tasks)
                    subplan = self.get_plan(subtask)
                    if not subplan:
                        break  # no plan for subtask
                    plan.extend(subplan)
                else:
                    return plan  # found plan for all subtasks

        return None  # no plan found


class Task:
    def __init__(self, name, primitive=False):
        self.name = name
        self.primitive = primitive


class Method:
    def __init__(self, name, task, subtasks):
        self.name = name
        self.task = task  # task this method decomposes
        self.subtasks = subtasks  # list of subtasks (can be compound or primitive)


if __name__ == "__main__":
    task = Task("Secure Area", primitive=False)
    plan = HierarchicalTaskNetwork().get_plan(task)
    print(plan)
