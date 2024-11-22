class ClassroomView:
    @staticmethod
    def render_classroom(classroom):
        return {
            "classroom_id": classroom.classroom_id,
            "room_number": classroom.room_number,
            "capacity": classroom.capacity,
            "building": classroom.building,
            "created_at": classroom.created_at,
            "updated_at": classroom.updated_at,
            "timetables": [timetable.timetable_id for timetable in classroom.timetables]
        }

    @staticmethod
    def render_classrooms(classrooms):
        return [ClassroomView.render_classroom(classroom) for classroom in classrooms]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, classroom_id=None):
        response = {"message": message}
        if classroom_id:
            response["classroom_id"] = classroom_id
        return response
