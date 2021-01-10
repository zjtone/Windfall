from rest_framework.views import APIView


class MyAPIView(APIView):
    """
    用户ID验证方案：将用户token取hash后，使用该hash串作为AES算法的密钥对用户id加密传输，服务端使用同样的方式获取用户id。
    """
    def initialize_request(self, request, *args, **kwargs):
        request = super(MyAPIView, self).initialize_request(request, *args, **kwargs)
        for key in request.GET:
            request.data[key] = request.GET[key]
        return request
