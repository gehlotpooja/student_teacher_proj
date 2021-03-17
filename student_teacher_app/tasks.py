from __future__ import absolute_import
# from student_teacher_project.celery import shared_task, app
from student_teacher_project.celery import app

# @shared_task
# @app.task
# def test():
#     data = 'All good in test'
#     return {data}
#     # print("inside test function for celery testing")
#     # print(' The test task executed with argument %s' % param)

from student_teacher_project.celery import app

@app.task
def adding_task(x, y):
    return x + y