class CourseView:
    @staticmethod
    def render_course(course):
        return {
            "course_id": course.course_id,
            "course_name": course.course_name,
            "credits": course.credits,
            "department_id": course.department_id,
            "instructor_id": course.instructor_id,
            "created_at": course.created_at,
            "updated_at": course.updated_at,
            "timetables": [timetable.timetable_id for timetable in course.timetables]
        }

    @staticmethod
    def render_courses(courses):
        return [CourseView.render_course(course) for course in courses]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, course_id=None):
        response = {"message": message}
        if course_id:
            response["course_id"] = course_id
        return response
