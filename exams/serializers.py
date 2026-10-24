from rest_framework import serializers
from exams.models import Assessment
from datetime import datetime,timezone,timedelta
class AssesmentSerializers(serializers.ModelSerializer):

    class Meta:

        model=Assessment

        fields="__all__"

        read_only_fields=["id","end_time","created_by"]


    