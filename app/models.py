from . import db



class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    desc = db.Column(db.String(300))
    room = db.Column(db.String(80))
    bathroom = db.Column(db.String(80))
    price = db.Column(db.String(80))
    proptype= db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(80))

    def __init__(self, title,desc,room,bathroom,price,proptype,location,photo):
        self.title=title
        self.desc=desc
        self.room=room
        self.bathroom=bathroom
        self.price=price
        self.proptype=proptype
        self.location=location
        self.photo=photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property_Title %r>' % (self.title)
