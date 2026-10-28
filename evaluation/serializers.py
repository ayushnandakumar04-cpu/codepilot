from rest_framework import serializers
from evaluation.models import Submission
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Submission
        fields="__all__"
        read_only_fields=[fields]
    # def get_fields(self):
    #     fields= super().get_fields()
    #     for f in fields.values():
    #         f.read_only=True
    #     return f
       #answer view