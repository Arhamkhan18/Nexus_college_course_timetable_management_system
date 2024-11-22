from flask import Blueprint
from timetable_app.controllers.classroom_controller import ClassroomController

classroom_bp=Blueprint('classroom_bp',__name__)

@classroom_bp.route('/api/classrooms',methods=['GET'])
def get_all_classroom():
    return ClassroomController.get_all_classrooms()

@classroom_bp.route('/api/classrooms/<int:classroom_id>',methods=['GET'])
def get_classroom(classroom_id):
    return ClassroomController.get_classroom(classroom_id)

@classroom_bp.route('/api/classrooms/<int:classroom_id>',methods=['PUT'])
def update_classroom(classroom_id):
    return ClassroomController.update_classroom(classroom_id)

@classroom_bp.route('/api/classrooms',methods=['POST'])
def create_classroom():
    return ClassroomController.create_classroom()

@classroom_bp.route('/api/classrooms/<int:classroom_id>',methods=['DELETE'])
def delete_classroom(classroom_id):
    return ClassroomController.delete_classroom(classroom_id)

    