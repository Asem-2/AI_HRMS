from typing import Any

from rest_framework import serializers

from ..models import ScreeningResult


class ScreeningResultSerializer(
    serializers.ModelSerializer[ScreeningResult]
):
    strengths = serializers.ListField(
        child=serializers.CharField(),
        read_only=True,
    )

    missing_skills = serializers.ListField(
        child=serializers.CharField(),
        read_only=True,
    )

    raw_report = serializers.SerializerMethodField()

    def get_raw_report(
        self,
        obj: ScreeningResult,
    ) -> dict[str, Any]:
        return obj.raw_report

    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = ScreeningResult
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