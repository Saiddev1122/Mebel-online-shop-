from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.v1.Category import services
from api.v1.Category.serializer import CategorySerializer
from mebel_site.models import Category


class CategoryView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            print(pk)
            root = Category.objects.get(pk=pk)
        except Exception as e:
            raise NotFound(f"Not found {e}")
        return root

    def get(self, requests, *args, **kwargs):
        if 'pk' in kwargs and kwargs["pk"]:
            result = services.get_one(requests, kwargs["pk"])
        else:
            result = services.list_category(requests)
        return Response(result, status=status.HTTP_200_OK, content_type="application/json")

    def post(self, requests):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        good = serializer.save()
        result = services.get_one(requests, good.id)
        return Response(result, status=status.HTTP_200_OK, content_type="application/json")

    def put(self, requests, pk):
        root = self.get_object(pk)
        serializer = self.get_serializer(
            data=requests.data,
            instance=root,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        good = serializer.save()
        result = services.get_one(requests, good.id)
        return Response(result, status=status.HTTP_200_OK, content_type="application/json")

    def delete(self, requests, *args, **kwargs):
        root = self.get_object(kwargs['pk'])
        a = root.delete()
        return Response({"success": f"{a}id seccessfully deleted"}, status=status.HTTP_204_NO_CONTENT)
