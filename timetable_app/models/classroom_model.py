from datetime import datetime
from shared.utils.db_utils import db



class Classroom(db.Model):
    __tablename__ = 'classrooms'
    classroom_id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(20), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    building = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    timetables = db.relationship('Timetable', backref='classroom', lazy=True)
