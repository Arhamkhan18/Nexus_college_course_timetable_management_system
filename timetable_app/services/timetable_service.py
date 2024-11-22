from timetable_app.models.timetable_model import Timetable
from shared.utils.db_utils import db
from datetime import datetime,time

class TimetableService:
    @staticmethod
    def create_timetable(course_id, classroom_id, day_of_week, start_time, end_time):
        timetable = Timetable(
            course_id=course_id,
            classroom_id=classroom_id,
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time
        )
        db.session.add(timetable)
        db.session.commit()
        return timetable

    @staticmethod
    def get_timetable_by_id(timetable_id):
        return Timetable.query.get(timetable_id)

    @staticmethod
    def get_all_timetables():
        return Timetable.query.all()

    @staticmethod
    def get_timetables_by_course(course_id):
        return Timetable.query.filter_by(course_id=course_id).all()

    @staticmethod
    def get_timetables_by_classroom(classroom_id):
        return Timetable.query.filter_by(classroom_id=classroom_id).all()

    @staticmethod
    def update_timetable(timetable_id, course_id, classroom_id, day_of_week, start_time, end_time):
        timetable = Timetable.query.get(timetable_id)
        if timetable:
            timetable.course_id = course_id
            timetable.classroom_id = classroom_id
            timetable.day_of_week = day_of_week
            timetable.start_time = start_time
            timetable.end_time = end_time
            timetable.updated_at = datetime.utcnow()
            db.session.commit()
        return timetable

    @staticmethod
    def delete_timetable(timetable_id):
        timetable = Timetable.query.get(timetable_id)
        if timetable:
            db.session.delete(timetable)
            db.session.commit()
        return timetable
