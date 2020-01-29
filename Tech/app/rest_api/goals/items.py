from app.core.goals.goal_api import create_goal, update_goal, get_aligned_goals


class BaseGoal:

    def __init__(self, document):
        self.title = document['title']
        self.progress = document['progress']
        self.aligned_to = document['aligned_to']


class Goal(BaseGoal):

    def __init__(self, document):
        super().__init__(document)

    @staticmethod
    def create_goal(args):
        goal = create_goal(args)
        return goal

    @staticmethod
    def update_goal(goal_id, args):
        updated_goal = update_goal(goal_id, args)
        return updated_goal

    @staticmethod
    def get_goals(goal_id):
        goals = get_aligned_goals(goal_id)
        return [Goal(goal) for goal in goals]
