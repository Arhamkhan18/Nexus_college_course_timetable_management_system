from flask import request
from timetable_app.services.timetable_service import TimetableService
from timetable_app.views.timetable_view import TimetableView

class TimetableController:
    @staticmethod
    def get_all_timetables():
        timetables = TimetableService.get_all_timetables()
        return TimetableView.render_timetables(timetables), 200

    @staticmethod
    def get_timetable(timetable_id):
        timetable = TimetableService.get_timetable_by_id(timetable_id)
        if not timetable:
            return TimetableView.render_error('Timetable not found'), 404
        return TimetableView.render_timetable(timetable), 200

    @staticmethod
    def create_timetable():
        data = request.get_json()
        course_id = data.get('course_id')
        classroom_id = data.get('classroom_id')
        day_of_week = data.get('day_of_week')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        timetable = TimetableService.create_timetable(course_id, classroom_id, day_of_week, start_time, end_time)
        return TimetableView.render_success('Timetable created successfully', timetable.timetable_id), 201

    @staticmethod
    def update_timetable(timetable_id):
        data = request.get_json()
        course_id = data.get('course_id')
        classroom_id = data.get('classroom_id')
        day_of_week = data.get('day_of_week')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        timetable = TimetableService.update_timetable(timetable_id, course_id, classroom_id, day_of_week, start_time, end_time)
        if timetable:
            return TimetableView.render_success('Timetable updated successfully', timetable.timetable_id), 200
        return TimetableView.render_error('Timetable not found'), 404

    @staticmethod
    def delete_timetable(timetable_id):
        timetable = TimetableService.delete_timetable(timetable_id)
        if timetable:
            return TimetableView.render_success('Timetable deleted successfully', timetable.timetable_id), 200
        return TimetableView.render_error('Timetable not found'), 404
