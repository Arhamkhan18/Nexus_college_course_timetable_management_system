import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from flask_cors import CORS
from timetable_app.routes.classroom_routes import classroom_bp
from timetable_app.routes.course_routes import course_bp
from timetable_app.routes.department_routes import department_bp
from timetable_app.routes.instructor_routes import instructor_bp
from timetable_app.routes.timetable_routes import timetable_bp
from shared.utils.db_utils import db



app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ar123@localhost/college_timetable'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True







db.init_app(app)

app.register_blueprint(classroom_bp)
app.register_blueprint(course_bp)
app.register_blueprint(department_bp)
app.register_blueprint(instructor_bp)
app.register_blueprint(timetable_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

