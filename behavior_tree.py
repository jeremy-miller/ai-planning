class BehariorTree:
    def __init__(self):
        self.root = Selector(
            children=[
                Sequence(
                    children=[
                        Condition(condition=self._is_enemy_visible),
                        Action(action=self._attack),
                    ]
                ),
            ]
        )

    def run(self):
        return self.root.run()

    @staticmethod
    def _is_enemy_visible():
        # check if the enemy is visible
        return True

    @staticmethod
    def _attack():
        # perform the attack action
        return True


class Node:
    def run(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Selector(Node):
    def __init__(self, children):
        self.children = children

    def run(self):
        for child in self.children:
            if child.run():
                return True
        return False


class Sequence(Node):
    def __init__(self, children):
        self.children = children

    def run(self):
        for child in self.children:
            if not child.run():
                return False
        return True


class Action(Node):
    def __init__(self, action):
        self.action = action

    def run(self):
        return self.action()


class Condition(Node):
    def __init__(self, condition):
        self.condition = condition

    def run(self):
        return self.condition()


if __name__ == "__main__":
    result = BehariorTree().run()
    print(result)
