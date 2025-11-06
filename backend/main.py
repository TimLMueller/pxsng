from flask import Flask
from flask_restx import Api
from Controllers.Course import api as courses_ns

app = Flask(__name__)
api = Api(
    app,
    version="1.0",
    title="pxsng backend"
)

api.add_namespace(courses_ns, path="/courses")
# api.init_app(app)

# myCourse = Course("test1", "testCourse", 3.00)
# courses = [
#         myCourse
#     # { 'description': 'salary', 'amount': 5000 }
# ]


# class CourseController:
#     def get(self):
#         return courses


# @app.route('/incomes', methods=['POST'])
# def add_income():
#     courses.append(request.get_json())
#     return '', 204


if __name__ == '__main__':
    app.run(debug=True)