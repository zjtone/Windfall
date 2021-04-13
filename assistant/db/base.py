from assistant.api.v1.serializers.auth_user import AuthUserSerializer, AuthUserRefSerializer


def get_by_id(model, _id):
    return model.objects.filter(id=_id).get()


def create_auth_user(auth_user_id, name, password, org_id, _type):
    # 创建账号
    auth_user_serializer = AuthUserSerializer(data={
        'username': name,
        'password': password
    })
    if auth_user_serializer.is_valid():
        auth_user_serializer.save()
    else:
        return auth_user_serializer.errors
    # 账号与信息关联
    auth_user_ref_serializer = AuthUserRefSerializer(data={
        'auth_user_id': auth_user_id,
        'auth_id': auth_user_serializer.data['id'],
        'type': _type,
        'org_id': org_id
    })
    if auth_user_ref_serializer.is_valid():
        auth_user_ref_serializer.save()
    else:
        return auth_user_ref_serializer.errors
