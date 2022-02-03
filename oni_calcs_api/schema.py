from . import ma


class ProfileSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "is_active")


multi_profiles_schema = ProfileSchema(many=True)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "role", "profiles")

    profiles = ma.Nested(multi_profiles_schema)


class DupeSchema(ma.Schema):
    class Meta:
        fields = ("id", "profile_id", "world_id", "agriculture_skill", "athletics_skill")


class WorldSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
