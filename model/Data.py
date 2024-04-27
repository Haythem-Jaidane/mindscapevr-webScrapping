from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    Id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    image_link = db.Column(db.String(200),nullable=False)
    link = db.Column(db.String(200), unique=True,nullable=False)
    description = db.Column(db.String(600), nullable=False)
    last_modification = db.Column(db.Date, nullable=False)

    def serialize(self):
        return {
            'title': self.title,
            'image_link': self.image_link,
            'link': self.link,
            'description': self.description,
        }

