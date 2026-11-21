from django.urls import path

from core.views.candidate import create_candidate
from core.views.department import create_department
from core.views.interview_question_set import (
    interview_question_set_detail,
)
from core.views.job_position import create_job_position
from core.views.resume import upload_resume
from core.views.screening_result import screening_result_detail

app_name = "core_api"

urlpatterns = [
    path(
        "departments/",
        create_department,
        name="department-create",
    ),
    path(
        "job-positions/",
        create_job_position,
        name="job-position-create",
    ),
    path(
        "candidates/",
        create_candidate,
        name="candidate-create",
    ),
    path(
        "resumes/",
        upload_resume,
        name="resume-upload",
    ),
    path(
        "screening-results/<int:pk>/",
        screening_result_detail,
        name="screening-result-detail",
    ),
    path(
        "interview-question-sets/<int:pk>/",
        interview_question_set_detail,
        name="interview-question-set-detail",
    ),
]