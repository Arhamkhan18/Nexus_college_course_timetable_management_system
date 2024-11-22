from flask import Blueprint
from timetable_app.controllers.instructor_controller import InstructorController

instructor_bp = Blueprint('instructor_bp', __name__)

@instructor_bp.route('/api/instructors', methods=['GET'])
def get_all_instructors():
    return InstructorController.get_all_instructors()

@instructor_bp.route('/api/instructors/<int:instructor_id>', methods=['GET'])
def get_instructor(instructor_id):
    return InstructorController.get_instructor(instructor_id)

@instructor_bp.route('/api/instructors', methods=['POST'])
def create_instructor():
    return InstructorController.create_instructor()

@instructor_bp.route('/api/instructors/<int:instructor_id>', methods=['PUT'])
def update_instructor(instructor_id):
    return InstructorController.update_instructor(instructor_id)

@instructor_bp.route('/api/instructors/<int:instructor_id>', methods=['DELETE'])
def delete_instructor(instructor_id):
    return InstructorController.delete_instructor(instructor_id)
