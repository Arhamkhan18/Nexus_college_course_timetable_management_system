from flask import Blueprint
from timetable_app.controllers.timetable_controller import TimetableController

timetable_bp = Blueprint('timetable_bp', __name__)

@timetable_bp.route('/api/timetables', methods=['GET'])
def get_all_timetables():
    return TimetableController.get_all_timetables()

@timetable_bp.route('/api/timetables/<int:timetable_id>', methods=['GET'])
def get_timetable(timetable_id):
    return TimetableController.get_timetable(timetable_id)

@timetable_bp.route('/api/timetables', methods=['POST'])
def create_timetable():
    return TimetableController.create_timetable()

@timetable_bp.route('/api/timetables/<int:timetable_id>', methods=['PUT'])
def update_timetable(timetable_id):
    return TimetableController.update_timetable(timetable_id)

@timetable_bp.route('/api/timetables/<int:timetable_id>', methods=['DELETE'])
def delete_timetable(timetable_id):
    return TimetableController.delete_timetable(timetable_id)
