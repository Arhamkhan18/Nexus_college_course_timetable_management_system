from flask import request
from timetable_app.services.instructor_service import InstructorService
from timetable_app.views.instructor_view import InstructorView

class InstructorController:
    @staticmethod
    def get_all_instructors():
        instructors = InstructorService.get_all_instructors()
        return InstructorView.render_instructors(instructors), 200

    @staticmethod
    def get_instructor(instructor_id):
        instructor = InstructorService.get_instructor_by_id(instructor_id)
        if not instructor:
            return InstructorView.render_error('Instructor not found'), 404
        return InstructorView.render_instructor(instructor), 200

    @staticmethod
    def create_instructor():
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        department_id = data.get('department_id')

        instructor = InstructorService.create_instructor(first_name, last_name, email, department_id)
        return InstructorView.render_success('Instructor created successfully', instructor.instructor_id), 201

    @staticmethod
    def update_instructor(instructor_id):
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        department_id = data.get('department_id')

        instructor = InstructorService.update_instructor(instructor_id, first_name, last_name, email, department_id)
        if instructor:
            return InstructorView.render_success('Instructor updated successfully', instructor.instructor_id), 200
        return InstructorView.render_error('Instructor not found'), 404

    @staticmethod
    def delete_instructor(instructor_id):
        instructor = InstructorService.delete_instructor(instructor_id)
        if instructor:
            return InstructorView.render_success('Instructor deleted successfully', instructor.instructor_id), 200
        return InstructorView.render_error('Instructor not found'), 404
