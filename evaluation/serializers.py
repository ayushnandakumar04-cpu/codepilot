from rest_framework import serializers
from evaluation.models import Answer
from Problem.models import Question
from evaluation.models import Submission
class SubmissionSerializer(serializers.ModelSerializer):

    assessment=serializers.StringRelatedField(read_only=True)

    student=serializers.StringRelatedField(read_only=True)

    answers=serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model=Submission
        fields="__all__"
        read_only_fields=[fields]

    def get_answers(self,obj):
        answer_obj=Answer.objects.filter(submission=obj)
        serializer_instance=AnswerSerializer(answer_obj,many=True)
        return serializer_instance.data

    # def get_fields(self):
    #     fields= super().get_fields()
    #     for f in fields.values():
    #         f.read_only=True
    #     return f
    #answer view

class AnswerSerializer(serializers.ModelSerializer):

    #question = serializers.PrimaryKeyRelatedField(query_set=Question.objects.all())

    class Meta:

        model=Answer

        fields="__all__"

        read_only_fields=["id","submission","question","answer_text","evaluated_at"]

#   def validate(self, validated_data):
      #  marks_awarded = validated_data.get("marks_awarded")
       # question = validated_data.get("question")

        #During a partial update, use the existing value when a field is omitted.
        #if marks_awarded is None and self.instance is not None:
        #    marks_awarded = self.instance.marks_awarded
        #if question is None and self.instance is not None:
         #   question = self.instance.question

        #if marks_awarded is not None and question is not None and marks_awarded > question.score:
         #   raise serializers.ValidationError({"marks_awarded": "Marks awarded cannot exceed the question score."})

       # return validated_data