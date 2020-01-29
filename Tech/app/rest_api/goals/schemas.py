from flask_restful import fields

goal_schema = dict(
    title=fields.String,
    progress=fields.Float,
    aligned_to=fields.String
)
