from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user

from . import db
from .models import World
from .schema import WorldSchema

bp = Blueprint("world", __name__, url_prefix="/world")

one_world_schema = WorldSchema()
multi_world_schema = WorldSchema(many=True)


# GET endpoints
@bp.route("/get", methods=["GET"])
@jwt_required()
def get_worlds_for_profile():
    worlds = World.query.filter_by(profile_id=current_user.get_active_profile().id).all()
    return jsonify(multi_world_schema.dump(worlds))


# POST endpoints
@bp.route("/add", methods=["POST"])
@jwt_required()
def add_world():
    new_world = World(name="", profile_id=current_user.get_active_profile().id)
    db.session.add(new_world)
    db.session.commit()
    return jsonify(one_world_schema.dump(new_world))


# PUT endpoints
@bp.route("/update", methods=["PUT"])
@jwt_required()
def update_world():
    data = request.get_json()
    id = data.get("id")
    new_name = data.get("name")
    world = World.query.get(id)
    world.name = new_name
    db.session.commit()
    return jsonify(one_world_schema.dump(world))
