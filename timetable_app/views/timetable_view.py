class TimetableView:
    @staticmethod
    def render_timetable(timetable):
        return {
            "timetable_id": timetable.timetable_id,
            "course_id": timetable.course_id,
            "classroom_id": timetable.classroom_id,
            "day_of_week": timetable.day_of_week,
            "start_time": timetable.start_time,  
            "end_time": timetable.end_time,
            "created_at": timetable.created_at,
            "updated_at": timetable.updated_at
        }

    @staticmethod
    def render_timetables(timetables):
        return [TimetableView.render_timetable(timetable) for timetable in timetables]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, timetable_id=None):
        response = {"message": message}
        if timetable_id:
            response["timetable_id"] = timetable_id
        return response
