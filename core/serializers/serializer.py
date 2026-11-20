
from pathlib import Path
from typing import Any

from django.core.files.uploadedfile import UploadedFile
from rest_framework import serializers

from ..models import (
    Candidate,
    Department,
    InterviewQuestionSet,
    JobPosition,
    Resume,
    ScreeningResult,
)


class DepartmentSerializer(serializers.ModelSerializer[Department]):
    class Meta(serializers.ModelSerializer.Meta):
        model = Department  # pyright: ignore[reportAssignmentType]
        fields = "__all__"
        read_only_fields = ("id", "created_at")


class JobPositionSerializer(serializers.ModelSerializer[JobPosition]):
    department_name = serializers.CharField(
        source="department.name",
        read_only=True,
    )

    class Meta(serializers.ModelSerializer.Meta):
        model = JobPosition  # pyright: ignore[reportAssignmentType]
        fields = (
            "id",
            "department",
            "department_name",
            "title",
            "description",
            "required_skills",
            "created_at",
        )
        read_only_fields = ("id", "created_at")


class CandidateSerializer(serializers.ModelSerializer[Candidate]):
    class Meta(serializers.ModelSerializer.Meta):
        model = Candidate  # pyright: ignore[reportAssignmentType]
        fields = "__all__"
        read_only_fields = ("id", "created_at")


class ResumeSerializer(serializers.ModelSerializer[Resume]):
    class Meta(serializers.ModelSerializer.Meta):
        model = Resume  # pyright: ignore[reportAssignmentType]
        fields = "__all__"
        read_only_fields = ("id", "uploaded_at")

    def validate_file(
        self,
        value: UploadedFile[Any],
    ) -> UploadedFile[Any]:
        allowed_extensions = {".pdf", ".docx", ".txt"}

        if not value.name:
            raise serializers.ValidationError(
                "The uploaded file must have a name."
            )

        extension = Path(value.name).suffix.lower()

        if extension not in allowed_extensions:
            raise serializers.ValidationError(
                "Only PDF, DOCX, and TXT files are allowed."
            )

        return value


class ScreeningResultSerializer(
    serializers.ModelSerializer[ScreeningResult]
):
    class Meta(serializers.ModelSerializer.Meta):
        model = ScreeningResult  # pyright: ignore[reportAssignmentType]
        fields = "__all__"
        read_only_fields = (
            "id",
            "candidate",
            "job_position",
            "score",
            "strengths",
            "missing_skills",
            "recommendation",
            "summary",
            "raw_report",
            "generated_at",
        )


class InterviewQuestionSetSerializer(
    serializers.ModelSerializer[InterviewQuestionSet]
):
    class Meta(serializers.ModelSerializer.Meta):
        model = InterviewQuestionSet  # pyright: ignore[reportAssignmentType]
        fields = "__all__"
        read_only_fields = (
            "id",
            "candidate",
            "job_position",
            "screening_result",
            "technical_questions",
            "behavioral_questions",
            "follow_up_questions",
            "generated_at",
        )
