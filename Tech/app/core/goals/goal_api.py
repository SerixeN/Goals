from bson import ObjectId

from app.database import goals_collection
from app.decorators import error_handler
from app.utils import MongoIdConverter


@error_handler('Failed to create goal')
def create_goal(args):
    result = goals_collection.insert_one(args)
    return MongoIdConverter.id_to_string(result.inserted_id)


@error_handler('Failed to update goal')
def update_goal(goal_id, args):
    query = {'_id': ObjectId(goal_id)}
    params = {'$set': {'progress': args['progress']}}
    updated_goal = goals_collection.update_one(query, params)
    return updated_goal


@error_handler('Failed to find goals')
def get_aligned_goals(goal_id):
    query = {'aligned_to': goal_id}
    result = list(goals_collection.find(query))
    return MongoIdConverter.id_to_string(result)
