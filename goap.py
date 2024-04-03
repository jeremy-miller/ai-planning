class GoalOrientedActionPlanning:
    def __init__(self):
        self.world_state = {"is_safe": False, "has_treasure": False, "has_sword": False}
        self.available_actions = [
            Action("Get Sword", {"has_sword": False}, {"has_sword": True}),
            Action("Fight Monsters", {"has_sword": True, "is_safe": False}, {"is_safe": True}),
            Action("Find Treasure", {"is_safe": True}, {"has_treasure": True}),
        ]

    def get_plan(self, goal, world_state=None):
        if not world_state:
            world_state = self.world_state

        if all(world_state.get(k, False) == v for k, v in goal.items()):  # goal achieved
            return []

        for action in self.available_actions:
            if action.check_preconditions(world_state):
                new_world_state = world_state.copy()
                action.apply_effects(new_world_state)
                sub_plan = self.get_plan(goal, new_world_state)
                if sub_plan is not None:
                    return [action.name] + sub_plan

        return None  # no plan found


class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def check_preconditions(self, world_state):
        return all(world_state.get(k, False) == v for k, v in self.preconditions.items())

    def apply_effects(self, world_state):
        for key, value in self.effects.items():
            world_state[key] = value


if __name__ == "__main__":
    goal = {"is_safe": True, "has_treasure": True}
    plan = GoalOrientedActionPlanning().get_plan(goal)
    print(plan)
