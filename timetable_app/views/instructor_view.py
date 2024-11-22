class InstructorView:
    @staticmethod
    def render_instructor(instructor):
        return {
            "instructor_id": instructor.instructor_id,
            "first_name": instructor.first_name,
            "last_name": instructor.last_name,
            "email": instructor.email,
            "department_id": instructor.department_id,
            "created_at": instructor.created_at,
            "updated_at": instructor.updated_at,
            "courses": [course.course_id for course in instructor.courses]
        }

    @staticmethod
    def render_instructors(instructors):
        return [InstructorView.render_instructor(instructor) for instructor in instructors]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, instructor_id=None):
        response = {"message": message}
        if instructor_id:
            response["instructor_id"] = instructor_id
        return response
