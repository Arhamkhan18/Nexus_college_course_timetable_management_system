from datetime import datetime
from shared.utils.db_utils import db



class Department(db.Model):
    __tablename__ = 'departments'
    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    courses = db.relationship('Course', backref='department', lazy=True)
    instructors = db.relationship('Instructor', backref='department', lazy=True)
