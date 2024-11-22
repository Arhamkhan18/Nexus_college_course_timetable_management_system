from timetable_app.models.instructor_model import Instructor
from shared.utils.db_utils import db
from datetime import datetime

class InstructorService:
    @staticmethod
    def create_instructor(first_name, last_name, email, department_id):
        instructor = Instructor(first_name=first_name, last_name=last_name, email=email, department_id=department_id)
        db.session.add(instructor)
        db.session.commit()
        return instructor

    @staticmethod
    def get_instructor_by_id(instructor_id):
        return Instructor.query.get(instructor_id)

    @staticmethod
    def get_all_instructors():
        return Instructor.query.all()

    @staticmethod
    def get_instructors_by_department(department_id):
        return Instructor.query.filter_by(department_id=department_id).all()

    @staticmethod
    def update_instructor(instructor_id, first_name, last_name, email, department_id):
        instructor = Instructor.query.get(instructor_id)
        if instructor:
            instructor.first_name = first_name
            instructor.last_name = last_name
            instructor.email = email
            instructor.department_id = department_id
            instructor.updated_at = datetime.utcnow()
            db.session.commit()
        return instructor

    @staticmethod
    def delete_instructor(instructor_id):
        instructor = Instructor.query.get(instructor_id)
        if instructor:
            db.session.delete(instructor)
            db.session.commit()
        return instructor
