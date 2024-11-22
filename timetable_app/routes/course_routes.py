from flask import Blueprint
from timetable_app.controllers.course_controller import CourseController

course_bp=Blueprint('course_bp',__name__)

@course_bp.route('/api/courses',methods=['GET'])
def get_all_courses():
    return CourseController.get_all_courses()

@course_bp.route('/api/courses/<int:course_id>',methods=['GET'])
def get_course(course_id):
    return CourseController.get_course(course_id)

@course_bp.route('/api/courses/<int:course_id>',methods=['PUT'])
def update_course(course_id):
    return CourseController.update_course(course_id)

@course_bp.route('/api/courses',methods=['POST'])
def create_course():
    return CourseController.create_course()

@course_bp.route('/api/courses/<int:course_id>',methods=['DELETE'])
def delete_course(course_id):
    return CourseController.delete_course(course_id)
