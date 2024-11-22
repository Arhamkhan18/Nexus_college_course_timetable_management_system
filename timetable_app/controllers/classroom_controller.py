from flask import request
from timetable_app.services.classroom_service import ClassroomService
from timetable_app.views.classroom_view import ClassroomView

class ClassroomController:
    @staticmethod
    def get_all_classrooms():
        classrooms = ClassroomService.get_all_classrooms()
        return ClassroomView.render_classrooms(classrooms), 200

    @staticmethod
    def get_classroom(classroom_id):
        classroom = ClassroomService.get_classroom_by_id(classroom_id)
        if not classroom:
            return ClassroomView.render_error('Classroom not found'), 404
        return ClassroomView.render_classroom(classroom), 200

    @staticmethod
    def create_classroom():
        data = request.get_json()
        room_number = data.get('room_number')
        capacity = data.get('capacity')
        building = data.get('building')

        classroom = ClassroomService.create_classroom(room_number, capacity, building)
        return ClassroomView.render_success('Classroom created successfully', classroom.classroom_id), 201

    @staticmethod
    def update_classroom(classroom_id):
        data = request.get_json()
        room_number = data.get('room_number')
        capacity = data.get('capacity')
        building = data.get('building')

        classroom = ClassroomService.update_classroom(classroom_id, room_number, capacity, building)
        if classroom:
            return ClassroomView.render_success('Classroom updated successfully', classroom.classroom_id), 200
        return ClassroomView.render_error('Classroom not found'), 404

    @staticmethod
    def delete_classroom(classroom_id):
        classroom = ClassroomService.delete_classroom(classroom_id)
        if classroom:
            return ClassroomView.render_success('Classroom deleted successfully', classroom.classroom_id), 200
        return ClassroomView.render_error('Classroom not found'), 404
