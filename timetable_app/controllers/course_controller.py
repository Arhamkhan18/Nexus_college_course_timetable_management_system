from flask import request
from timetable_app.services.course_service import CourseService
from timetable_app.views.course_view import CourseView

class CourseController:
    @staticmethod
    def get_all_courses():
        courses = CourseService.get_all_courses()
        return CourseView.render_courses(courses), 200

    @staticmethod
    def get_course(course_id):
        course = CourseService.get_course_by_id(course_id)
        if not course:
            return CourseView.render_error('Course not found'), 404
        return CourseView.render_course(course), 200

    @staticmethod
    def create_course():
        data = request.get_json()
        course_name = data.get('course_name')
        credits = data.get('credits')
        department_id = data.get('department_id')
        instructor_id = data.get('instructor_id')

        course = CourseService.create_course(course_name, credits, department_id, instructor_id)
        return CourseView.render_success('Course created successfully', course.course_id), 201

    @staticmethod
    def update_course(course_id):
        data = request.get_json()
        course_name = data.get('course_name')
        credits = data.get('credits')
        department_id = data.get('department_id')
        instructor_id = data.get('instructor_id')

        course = CourseService.update_course(course_id, course_name, credits, department_id, instructor_id)
        if course:
            return CourseView.render_success('Course updated successfully', course.course_id), 200
        return CourseView.render_error('Course not found'), 404

    @staticmethod
    def delete_course(course_id):
        course = CourseService.delete_course(course_id)
        if course:
            return CourseView.render_success('Course deleted successfully', course.course_id), 200
        return CourseView.render_error('Course not found'), 404
