from django.contrib.auth.models import User
from .serializers import getUserDataSerializers
from django.http import JsonResponse


def create_user(request):
    try:

        success = False
        msg = 'User not created'
        post_data = request.POST
        user_data = User(first_name=post_data['firstName'], last_name=post_data['lastName'],
                         email=post_data['email'],
                         username=post_data['userName'])

        user_data.set_password(post_data['password'])
        user_data.save()
        success = True
        msg = 'User data saved successfully'

    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def update_user(request):
    try:
        success = False
        msg = 'failed to update user details'
        put_data = request.POST
        user_data = User.objects.get(id = put_data['id'])
        user_data.set_password(put_data['password'])
        user_data.email = put_data['email']
        user_data.is_staff = put_data['staff']
        user_data.save()
        # User.objects.filter(username__startswith='nobi').delete()
        success = True
        msg = 'User data updated successfully'
    except Exception as e:
        print(e.args)
    return {'success':success , 'msg':msg}


def get_user_details_with_id(request):
    try:
        success = False
        msg = 'Unable to get user details'
        data = 'no data fetched'
        get_data = request.GET
        id = get_data['id']
        if id:
            user_data = User.objects.values_list('id','first_name', 'last_name', 'username').get(id = id)
            data = user_data
            success = True
            msg = 'User details fetched'
    except Exception as e:
        print(e.args)
    return {'success':success , 'msg':msg, 'data':data}


def get_all_user_details(request):
    try:
        # import pdb
        # pdb.set_trace()
        user_data = User.objects.all().order_by('id')
        serializer = getUserDataSerializers(user_data, many=True)

    except Exception as e:
        print(e.args)
    return serializer.data