from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from rest_framework.serializers import (
    EmailField,
    CharField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    PrimaryKeyRelatedField,
)
from .models import User, Viewer, Role, Camera
from datetime import datetime
from rest_framework_jwt.settings import api_settings

# User= get_user_model()


# register user
class UserCreateSerializer(ModelSerializer):
    # email = EmailField(label = 'Email Address')
    # email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'username', 
            'email',
            #'email2', 
            'password',
            # 'role',
            ]
        extra_kwargs = {"password": {"write_only": True}}
        # write_only = 'password'
        # fields='__all__'

    # def validated_email(self, value):
    #     data = self
    #     email1 = data["email"]
    #     email2 = data.get["email2"]
    #     if email1 != email2:
    #         raise ValidationError("Emails must match")
    #     return value

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        # role = validated_data['role']
        user_obj = User(
                email=email,
                username=username,
                # role = role,
                # password_hash=password_hash
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


# login serializer
class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    # dropbox_token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)
    full_name = CharField(read_only=True, allow_blank=True)
    camera = PrimaryKeyRelatedField(many=True, read_only=True)
    # camera= CameraSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email', 
            'username', 
            'password',
            'full_name',
            'token',
            'dropbox_token',
            'camera',
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ('dropbox_token',)

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required to login")

        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credential")

        queryset = Camera.objects.filter(
            Q(uid_id__email=email) |
            Q(uid_id__username=username))

        # payload = {
        #         'id': user_obj.pk,
        #         'username': user_obj.username,
        #         'staff': user_obj.is_staff,
        #         'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        #     }
        # token = {'token': jwt.encode(payload, SECRET)}
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user_obj)

        if api_settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(datetime.utcnow().utctimetuple())

        data["id"] = user_obj.id
        data["email"] = user_obj.email
        data["token"] = jwt_encode_handler(payload)
        data["full_name"] = user_obj.get_full_name()
        data["dropbox_token"] = user_obj.dropbox_token
        data["camera"] = queryset
        return data


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',  
        ]

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id'
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class CameraSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Camera
        fields = [
            'cid',
            'name',
            'address',
            'user',
            'created_at',
            'is_active',
        ]

        read_only_fields = ("created_at", "is_active")


class ViewerSerializer(ModelSerializer):

    class Meta:
        model = Viewer
        fields = [
            'master',
            'viewer'
        ]
        # fields='__all__'


class RoleSerializer(ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'