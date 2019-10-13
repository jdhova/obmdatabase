from rest_framework import serializers
from .models import *


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('first_name', 'infix', 'last_name', 'photo', 'company_name', 'job_title', 'company_photo',
                  'company_address')


