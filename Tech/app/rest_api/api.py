from flask_restful import Api

from app import app
from app.rest_api.goals.resource import GoalResource, GoalCollectionResource

api = Api(app)

api.add_resource(GoalResource, '/goals')
api.add_resource(GoalCollectionResource, '/goals/<goal_id>')
