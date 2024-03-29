from admin_app_config import db


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(320), nullable=True)
    email = db.Column(db.String(320), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    user_group = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    last_login = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return 'Email: %s' % self.email

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return True

    def get_id(self):
        return self.id

    def BMI(self):
        if self.height is not None and self.weight is not None:
            return 703 * float(self.weight) / float(self.height ** 2)
        else:
            return None

    def is_anonymous(self):
        return False

    def has_role(self, role):
        return self.user_group == role


class UserLocation(db.Model):

    __tablename__ = 'user_location'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return 'User ID: {}\nDate: {}'.format(
            self.user_id, self.date)


class UserSteps(db.Model):

    __tablename__ = 'user_steps'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    step_count = db.Column(db.Integer)

    def __repr__(self):
        return 'User ID: {}\nDate: {}'.format(
            self.user_id, self.date)


class HazardSummary(db.Model):

    __tablename__ = 'hazard_summary'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hazard_category = db.Column(db.String(100), nullable=False, unique=True)
    summary= db.Column(db.Text, nullable=False)
    source = db.Column(db.Text, nullable=False)
    bad_distance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return 'Hazard Category: {}'.format(self.hazard_category)


class HazardLocation(db.Model):

    __tablename__ = 'hazard_location'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hazard_category = db.Column(
        db.String(100),
        db.ForeignKey('hazard_summary.hazard_category'),
        nullable=False
    )
    place_name = db.Column(db.String(100))
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    summary = db.relationship(
        HazardSummary,
        backref=db.backref('hazard_location', uselist=False),
        uselist=False,
        lazy='joined'
    )

    def __repr__(self):
        return 'Hazard Category: {}\nPlace Name: {}'.format(
            self.hazard_category, self.place_name)
