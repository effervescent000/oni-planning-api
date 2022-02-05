from . import db
from passlib.hash import pbkdf2_sha256 as hash


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50))
    profiles = db.relationship("Profile", backref="user", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"User <{self.username}>"

    @staticmethod
    def hash_password(password):
        return hash.hash(password)

    def check_password(self, input):
        return hash.verify(input, self.password)

    def get_active_profile(self):
        for profile in self.profiles:
            if profile.is_active:
                return profile


class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    dupes = db.relationship("Dupe", backref="profile", lazy=True, cascade="all, delete-orphan")
    worlds = db.relationship("World", backref="profile", lazy=True, cascade="all, delete-orphan")


class Dupe(db.Model):
    __tablename__ = "dupes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), nullable=False)
    world_id = db.Column(db.Integer, db.ForeignKey("worlds.id"))

    agriculture_skill = db.Column(db.Integer, nullable=False)
    athletics_skill = db.Column(db.Integer, nullable=False)
    construction_skill = db.Column(db.Integer, nullable=False)
    creativity_skill = db.Column(db.Integer, nullable=False)
    cuisine_skill = db.Column(db.Integer, nullable=False)
    excavation_skill = db.Column(db.Integer, nullable=False)
    husbandry_skill = db.Column(db.Integer, nullable=False)
    machinery_skill = db.Column(db.Integer, nullable=False)
    medicine_skill = db.Column(db.Integer, nullable=False)
    piloting_skill = db.Column(db.Integer, nullable=False)
    rocketry_skill = db.Column(db.Integer, nullable=False)
    science_skill = db.Column(db.Integer, nullable=False)
    strength_skill = db.Column(db.Integer, nullable=False)

    advanced_research = db.Column(db.Boolean, nullable=False, default=False)
    field_research = db.Column(db.Boolean, nullable=False, default=False)
    applied_sciences = db.Column(db.Boolean, nullable=False, default=False)
    astronomy = db.Column(db.Boolean, nullable=False, default=False)
    data_analysis = db.Column(db.Boolean, nullable=False, default=False)

    crop_tending = db.Column(db.Boolean, nullable=False, default=False)
    critter_ranching = db.Column(db.Boolean, nullable=False, default=False)

    grilling = db.Column(db.Boolean, nullable=False, default=False)

    available_skill_points = db.Column(db.Integer, nullable=False)


class World(db.Model):
    __tablename__ = "worlds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), nullable=False)
    dupes = db.relationship("Dupe", backref="world", lazy=True, cascade="all, delete-orphan")
