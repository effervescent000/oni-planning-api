from . import ma


class ProfileSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "is_active")


multi_profiles_schema = ProfileSchema(many=True)
one_profile_schema = ProfileSchema()


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "role", "profiles")

    profiles = ma.Nested(multi_profiles_schema)


class DupeSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "profile_id",
            "world_id",
            "agriculture_skill",
            "athletics_skill",
            "construction_skill",
            "creativity_skill",
            "cuisine_skill",
            "excavation_skill",
            "husbandry_skill",
            "machinery_skill",
            "medicine_skill",
            "piloting_skill",
            "rocketry_skill",
            "science_skill",
            "strength_skill",
            "advanced_research",
            "field_research",
            "applied_sciences",
            "astronomy",
            "data_analysis",
            "crop_tending",
            "critter_ranching",
            "grilling",
            "available_skill_points",
        )


class WorldSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
