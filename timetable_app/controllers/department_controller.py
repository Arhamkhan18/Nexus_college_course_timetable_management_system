from flask import request
from timetable_app.services.department_service import DepartmentService
from timetable_app.views.department_view import DepartmentView

class DepartmentController:
    @staticmethod
    def get_all_departments():
        departments = DepartmentService.get_all_departments()
        return DepartmentView.render_departments(departments), 200

    @staticmethod
    def get_department(department_id):
        department = DepartmentService.get_department_by_id(department_id)
        if not department:
            return DepartmentView.render_error('Department not found'), 404
        return DepartmentView.render_department(department), 200

    @staticmethod
    def create_department():
        data = request.get_json()
        department_name = data.get('department_name')
        
        department = DepartmentService.create_department(department_name)
        return DepartmentView.render_success('Department created successfully', department.department_id), 201

    @staticmethod
    def update_department(department_id):
        data = request.get_json()
        department_name = data.get('department_name')

        department = DepartmentService.update_department(department_id, department_name)
        if department:
            return DepartmentView.render_success('Department updated successfully', department.department_id), 200
        return DepartmentView.render_error('Department not found'), 404

    @staticmethod
    def delete_department(department_id):
        department = DepartmentService.delete_department(department_id)
        if department:
            return DepartmentView.render_success('Department deleted successfully', department.department_id), 200
        return DepartmentView.render_error('Department not found'), 404
