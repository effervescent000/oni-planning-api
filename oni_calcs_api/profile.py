from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user

from . import db
from .models import Profile
from .schema import ProfileSchema

bp = Blueprint("profile", __name__, url_prefix="/profile")

one_profile_schema = ProfileSchema()
multi_profile_schema = ProfileSchema(many=True)

# GET endpoints


@bp.route("/get", methods=["GET"])
@jwt_required()
def get_profiles_for_current_user():
    if current_user != None:
        return jsonify(multi_profile_schema.dump(current_user.profiles))


# POST endpoints


@bp.route("/add", methods=["POST"])
@jwt_required()
def add_profile():
    new_profile = Profile(user_id=current_user.id)
    if current_user.get_active_profile() == None:
        new_profile.is_active = True
    db.session.add(new_profile)
    db.session.commit()
    return jsonify(one_profile_schema.dump(new_profile))


# PUT endpoints


@bp.route("/activate", methods=["PUT"])
@jwt_required()
def set_active_profile():
    id = request.get_json().get("id")
    target_profile = Profile.query.get(id)
    if target_profile.user_id != current_user.id:
        return jsonify("Error: Not authorized"), 401
    profile_list = Profile.query.filter_by(user_id=current_user.id).all()
    for profile in profile_list:
        profile.is_active = False
        db.session.commit()
    # finally, set the target profile to active
    target_profile.is_active = True
    db.session.commit()
    # return the active profile
    return jsonify(one_profile_schema.dump(target_profile))
