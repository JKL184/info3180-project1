from . import db



class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    desc = db.Column(db.String(1000))
    room = db.Column(db.String(300))
    bathroom = db.Column(db.String(300))
    price = db.Column(db.String(300))
    proptype= db.Column(db.String(300))
    location = db.Column(db.String(300))
    photo = db.Column(db.String(300))

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
