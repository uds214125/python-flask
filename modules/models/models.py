# from flask_sqlalchemy import SQLAlchemy
# from flask_security import UserMixin, RoleMixin

# db = SQLAlchemy()

# class User(db.Model, UserMixin):
    # email = db.Column(db.String(255), unique=True)
    # password = db.Column(db.String(255))
    # active = db.Column(db.Boolean())
    # roles = db.relationship('Role', secondary=roles_users,
    #                         backref=db.backref('users', lazy='dynamic'))

    # def __init__(self, email, password, active, roles):
    #     self.email = email
    #     self.password = password
    #     self.active = active
    #     self.roles = roles