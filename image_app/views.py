from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.core.files.base import ContentFile
from .models import Image
from .serializers import ImageSerializer


class ImageUploadViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser]

    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        ids_data = request.data.get('ids')
        ids = ids_data.split(',')
        timestamps_data = request.data.get('timestamps')
        timestamps = timestamps_data.split(',')

        print(str(len(images)) + " images received")
        print(str(len(ids)) + " ids received")
        print(str(len(timestamps)) + " timestamps received")

        if not (len(images) == len(ids) == len(timestamps)):
            return Response({"error": "Mismatched lengths of images, ids, and timestamps"}, status=status.HTTP_400_BAD_REQUEST)

        for image, given_id, timestamp in zip(images, ids, timestamps):
            image_instance = Image(
                image_path=image,
                given_id=given_id,
                created_at=timestamp
            )
            image_instance.save()

        return Response({"status": "success"}, status=status.HTTP_201_CREATED)
