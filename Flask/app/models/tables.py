from app import db


class User(db.models):
    __tablename__ = "users"

    id = db.Collumn(db.Integer, primary_key=True, auto_increment=True)
    username = db.Collumn(db.String, unique=True)
    pasword = db.Collumn(db.String)
    name = sb.Collumn(db.String)
    email = db.Collumn(db.String, unique=True)

    def __init__(self, username, pasword, name, email):
        self.username = username
        self.pasword = pasword
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.model):
    __tablename__ = "posts"

    id = db.Collumn(db.Integer, primary_key=True)
    content = db.Collumn(db.Text)
    id_user = db.Collumn(db.Integer, db.ForeignKey('user.id'))

    owner = db.relationship('User', foreign_key=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.models):
    """docstring for Follow."""
    __tablename__ = "follow"

    id = db.Collumn(db.Integer, prymary_key=True)
    user_id = db.Collumn(db.Integer, db.ForeignKey('user.id'))
    follower_id = db.Collumn(db.Integer, db.ForeignKey('user.id'))

    owner = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)

    def __init__(self, user_id, follower_id):
        self.user_id = user_id
        self.follower_id = follower_id

    def __repr__(self):
        return "<Follow %r>" % self.id
