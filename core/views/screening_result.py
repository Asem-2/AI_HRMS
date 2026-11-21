from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import ScreeningResult
from ..serializers import ScreeningResultSerializer


@api_view(["GET"])
def screening_result_detail(request, pk):
    screening_result = get_object_or_404(
        ScreeningResult,
        pk=pk,
    )

    serializer = ScreeningResultSerializer(screening_result)

    return Response(serializer.data)