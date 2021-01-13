from rest_framework.response import Response
from rest_framework import status
from assistant.api.v1.serializers.course import CourseSerializer
from assistant.api.v1.serializers.shopping import ShoppingCartSerializer
from assistant.db.shopping import get_shopping_cart
from assistant.api.apiviews import MyAPIView


class ShoppingCartApi(MyAPIView):
    def get(self, request):
        params = request.data
        if 'user_id' not in params or 'org_id' not in params:
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)
        offset, limit = 0, 10
        if 'offset' in params:
            offset = int(params['offset'])
        if 'limit' in params:
            limit = min(int(params['limit']), 50)
        return Response(CourseSerializer(
            get_shopping_cart(user_id=params['user_id'], org_id=params['org_id'],
                              offset=offset, limit=limit), many=True).data,
            status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ShoppingCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
