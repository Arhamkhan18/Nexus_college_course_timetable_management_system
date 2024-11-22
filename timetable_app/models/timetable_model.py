from datetime import datetime
from shared.utils.db_utils import db



class Timetable(db.Model):
    __tablename__ = 'timetables'
    timetable_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    classroom_id = db.Column(db.Integer, db.ForeignKey('classrooms.classroom_id'), nullable=False)
    day_of_week = db.Column(db.String(10), nullable=False)
    start_time = db.Column(db.String(8), nullable=False)
    end_time = db.Column(db.String(8), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
