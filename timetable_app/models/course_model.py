from datetime import datetime
from shared.utils.db_utils import db



class Course(db.Model):
    __tablename__ = 'courses'
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.instructor_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    timetables = db.relationship('Timetable', backref='course', lazy=True)
