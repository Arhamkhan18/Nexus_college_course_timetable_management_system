from timetable_app.models.department_model import Department
from shared.utils.db_utils import db
from datetime import datetime

class DepartmentService:
    @staticmethod
    def create_department(department_name):
        department = Department(department_name=department_name)
        db.session.add(department)
        db.session.commit()
        return department

    @staticmethod
    def get_department_by_id(department_id):
        return Department.query.get(department_id)

    @staticmethod
    def get_all_departments():
        return Department.query.all()

    @staticmethod
    def update_department(department_id, department_name):
        department = Department.query.get(department_id)
        if department:
            department.department_name = department_name
            department.updated_at = datetime.utcnow()
            db.session.commit()
        return department

    @staticmethod
    def delete_department(department_id):
        department = Department.query.get(department_id)
        if department:
            db.session.delete(department)
            db.session.commit()
        return department
