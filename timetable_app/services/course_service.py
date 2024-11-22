from timetable_app.models.course_model import Course
from shared.utils.db_utils import db
from datetime import datetime

class CourseService:
    @staticmethod
    def create_course(course_name, credits, department_id, instructor_id):
        course = Course(course_name=course_name, credits=credits, department_id=department_id, instructor_id=instructor_id)
        db.session.add(course)
        db.session.commit()
        return course

    @staticmethod
    def get_course_by_id(course_id):
        return Course.query.get(course_id)

    @staticmethod
    def get_all_courses():
        return Course.query.all()

    @staticmethod
    def get_courses_by_department(department_id):
        return Course.query.filter_by(department_id=department_id).all()

    @staticmethod
    def update_course(course_id, course_name, credits, department_id, instructor_id):
        course = Course.query.get(course_id)
        if course:
            course.course_name = course_name
            course.credits = credits
            course.department_id = department_id
            course.instructor_id = instructor_id
            course.updated_at = datetime.utcnow()
            db.session.commit()
        return course

    @staticmethod
    def delete_course(course_id):
        course = Course.query.get(course_id)
        if course:
            db.session.delete(course)
            db.session.commit()
        return course
