from django.http import Http404
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from assistant.models import AuthUserRef
from assistant.api.v1.serializers.teacher import TeacherSerializer
from assistant.db import people, base, org
from assistant.api.apiviews import MyAPIView
from django.contrib.auth.hashers import make_password


class TeacherApi(MyAPIView):
    def get(self, request):
        try:
            params = request.data
            if "id" in params:
                _id = params["id"]
                teacher = people.get_teacher_by_id(_id)
                return Response(TeacherSerializer(teacher).data)
            raise Http404
        except Exception as e:
            print('[TeacherApi]get e = {}'.format(e))
            raise Http404

    def post(self, request):
        params = request.data
        params['password'] = make_password(params['password'])

        if "id" in params:
            return TeacherApi.update(request)

        if 'org_id' not in params:
            return Response("非法机构！", status=status.HTTP_400_BAD_REQUEST)
        org_id = params["org_id"]
        _org = org.get_org_by_id(org_id)
        if _org is None:
            return Response("非法机构！", status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            save_point = transaction.savepoint()
            serializer = TeacherSerializer(data=params)
            if serializer.is_valid():
                serializer.save()
            else:
                transaction.savepoint_rollback(save_point)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            result = base.create_auth_user(serializer.data['id'], params['username'], params['password'],
                                           params['org_id'], AuthUserRef.Type.TEACHER.value)
            if result is None:
                transaction.savepoint_commit(save_point)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                transaction.savepoint_rollback(save_point)
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request):
        try:
            params = request.data
            if 'org_id' in params:
                return Response("非法！机构不能修改！", status=status.HTTP_400_BAD_REQUEST)
            if "id" in params:
                update_teacher = request.data
                exist_teacher = people.get_teacher_by_id(params["id"])
                for key in update_teacher:
                    if hasattr(exist_teacher, key):
                        setattr(exist_teacher, key, update_teacher[key])
                exist_teacher.save()

                # 修改密码
                if 'password' in params:
                    password = make_password(params['password'])
                    if password != exist_teacher.password:
                        auth_user_ref = people.get_people_by_auth_id(auth_id=params['id'])
                        auth_user = people.get_auth_user_by_id(auth_user_ref.id)
                        auth_user.password = password
                        auth_user.save()

                return Response("", status=status.HTTP_200_OK)
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)


class TeacherList(MyAPIView):
    def get(self, request):
        params = request.data
        if 'org_id' not in params:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        org_id = params['org_id']
        offset, limit = 0, 10
        if 'pageIndex' in params:
            offset = int(params['pageIndex'])
        if 'pageSize' in params:
            limit = min(int(params['pageSize']), 50)
        data_status = None
        if 'status' in params:
            data_status = int(params['status'])
            data_status = data_status if data_status > 0 else None
        return Response({
            "data": TeacherSerializer(people.list_teacher(org_id, offset, limit, data_status), many=True).data,
            "total": people.count_teacher(org_id, data_status)
        }, status=status.HTTP_200_OK)
