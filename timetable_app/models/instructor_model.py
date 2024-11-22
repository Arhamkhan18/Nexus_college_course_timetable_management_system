from datetime import datetime
from shared.utils.db_utils import db



class Instructor(db.Model):
    __tablename__ = 'instructors'
    instructor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    courses = db.relationship('Course', backref='instructor', lazy=True)
