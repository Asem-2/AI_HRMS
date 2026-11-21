from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from ..serializers import ResumeSerializer


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def upload_resume(request):
    serializer = ResumeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED,
    )