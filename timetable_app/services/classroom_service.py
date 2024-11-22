from timetable_app.models.classroom_model import Classroom
from shared.utils.db_utils import db
from datetime import datetime

class ClassroomService:
    @staticmethod
    def create_classroom(room_number, capacity, building):
        classroom = Classroom(room_number=room_number, capacity=capacity, building=building)
        db.session.add(classroom)
        db.session.commit()
        return classroom

    @staticmethod
    def get_classroom_by_id(classroom_id):
        return Classroom.query.get(classroom_id)

    @staticmethod
    def get_all_classrooms():
        return Classroom.query.all()

    @staticmethod
    def update_classroom(classroom_id, room_number, capacity, building):
        classroom = Classroom.query.get(classroom_id)
        if classroom:
            classroom.room_number = room_number
            classroom.capacity = capacity
            classroom.building = building
            classroom.updated_at = datetime.utcnow()
            db.session.commit()
        return classroom

    @staticmethod
    def delete_classroom(classroom_id):
        classroom = Classroom.query.get(classroom_id)
        if classroom:
            db.session.delete(classroom)
            db.session.commit()
        return classroom
