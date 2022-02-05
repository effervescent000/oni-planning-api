from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user

from . import db
from .models import Dupe
from .schema import DupeSchema

bp = Blueprint("Dupe", __name__, url_prefix="/dupe")
one_dupe_schema = DupeSchema()
multi_dupe_schema = DupeSchema(many=True)

# GET endpoints


# POST endpoints


@bp.route("/add", methods=["POST"])
@jwt_required()
def add_dupe():
    data = request.get_json()
    print(data)
    name = data.get("name")
    agriculture_skill = data.get("agriculture")
    athletics_skill = data.get("athletics")
    construction_skill = data.get("construction")
    creativity_skill = data.get("creativity")
    cuisine_skill = data.get("cuisine")
    excavation_skill = data.get("excavation")
    husbandry_skill = data.get("husbandry")
    machinery_skill = data.get("machinery")
    medicine_skill = data.get("medicine")
    piloting_skill = data.get("piloting")
    rocketry_skill = data.get("rocketry")
    science_skill = data.get("science")
    strength_skill = data.get("strength")

    available_skill_points = data.get("skillPoints")

    crop_tending = data.get("cropTending")
    critter_ranching = data.get("critterRanching")
    grilling = data.get("grilling")
    advanced_research = data.get("advancedResearch")
    field_research = data.get("fieldResearch")
    applied_sciences = data.get("appliedSciences")
    data_analysis = data.get("dataAanalysis")

    if name == "":
        return jsonify("Dupe must have a name")

    dupe = Dupe(name=name)
    dupe.profile_id = current_user.get_active_profile().id
    dupe.agriculture_skill = agriculture_skill if agriculture_skill != None else 0
    dupe.athletics_skill = athletics_skill if athletics_skill != None else 0
    dupe.construction_skill = construction_skill if construction_skill != None else 0
    dupe.creativity_skill = creativity_skill if creativity_skill != None else 0
    dupe.cuisine_skill = cuisine_skill if cuisine_skill != None else 0
    dupe.excavation_skill = excavation_skill if excavation_skill != None else 0
    dupe.husbandry_skill = husbandry_skill if husbandry_skill != None else 0
    dupe.machinery_skill = machinery_skill if machinery_skill != None else 0
    dupe.medicine_skill = medicine_skill if medicine_skill != None else 0
    dupe.piloting_skill = piloting_skill if piloting_skill != None else 0
    dupe.rocketry_skill = rocketry_skill if rocketry_skill != None else 0
    dupe.science_skill = science_skill if science_skill != None else 0
    dupe.strength_skill = strength_skill if strength_skill != None else 0
    dupe.available_skill_points = available_skill_points if available_skill_points != None else 0

    dupe.crop_tending = crop_tending if crop_tending != None else False
    dupe.critter_ranching = critter_ranching if critter_ranching != None else False
    dupe.grilling = grilling if grilling != None else False
    dupe.advanced_research = advanced_research if advanced_research != None else False
    dupe.field_research = field_research if field_research != None else False
    dupe.applied_sciences = applied_sciences if applied_sciences != None else False
    dupe.data_analysis = data_analysis if data_analysis != None else False

    db.session.add(dupe)
    db.session.commit()

    return jsonify(one_dupe_schema.dump(dupe))


# PUT endpoints

# DELETE endpoints


# utils
