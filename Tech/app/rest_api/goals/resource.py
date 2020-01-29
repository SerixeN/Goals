from http import HTTPStatus

from flask_restful import Resource, marshal_with, abort

from app.rest_api.goals.items import Goal
from app.rest_api.goals.parsers import create_goal_parser, update_goal_parser
from app.rest_api.goals.schemas import goal_schema


class GoalResource(Resource):

    def post(self):
        args = create_goal_parser.parse_args()
        goal = Goal.create_goal(args)
        return goal, HTTPStatus.CREATED


class GoalCollectionResource(Resource):

    @marshal_with(goal_schema)
    def put(self, goal_id):
        args = update_goal_parser.parse_args()
        if not args.get('progress'):
            abort(HTTPStatus.BAD_REQUEST, message='Missing progress value')
        update_goal = Goal.update_goal(goal_id, args)
        return update_goal, HTTPStatus.OK

    @marshal_with(goal_schema)
    def get(self, goal_id):
        goals = Goal.get_goals(goal_id)
        return goals, HTTPStatus.OK
