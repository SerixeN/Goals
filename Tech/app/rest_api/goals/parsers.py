from flask_restful.reqparse import RequestParser


create_goal_parser = RequestParser()
create_goal_parser.add_argument('title', type=str, required=True)
create_goal_parser.add_argument('progress', type=float, required=False)
create_goal_parser.add_argument('aligned_to', type=str, required=False)

update_goal_parser = RequestParser()
update_goal_parser.add_argument('progress', type=float, required=False)
