class DepartmentView:
    @staticmethod
    def render_department(department):
        return {
            "department_id": department.department_id,
            "department_name": department.department_name,
            "created_at": department.created_at,
            "updated_at": department.updated_at,
            "courses": [course.course_id for course in department.courses],
            "instructors": [instructor.instructor_id for instructor in department.instructors]
        }

    @staticmethod
    def render_departments(departments):
        return [DepartmentView.render_department(department) for department in departments]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, department_id=None):
        response = {"message": message}
        if department_id:
            response["department_id"] = department_id
        return response
