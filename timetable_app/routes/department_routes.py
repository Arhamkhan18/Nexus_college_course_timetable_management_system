from flask import Blueprint
from timetable_app.controllers.department_controller import DepartmentController

department_bp = Blueprint('department_bp', __name__)

@department_bp.route('/api/departments', methods=['GET'])
def get_all_departments():
    return DepartmentController.get_all_departments()

@department_bp.route('/api/departments/<int:department_id>', methods=['GET'])
def get_department(department_id):
    return DepartmentController.get_department(department_id)

@department_bp.route('/api/departments', methods=['POST'])
def create_department():
    return DepartmentController.create_department()

@department_bp.route('/api/departments/<int:department_id>', methods=['PUT'])
def update_department(department_id):
    return DepartmentController.update_department(department_id)

@department_bp.route('/api/departments/<int:department_id>', methods=['DELETE'])
def delete_department(department_id):
    return DepartmentController.delete_department(department_id)
