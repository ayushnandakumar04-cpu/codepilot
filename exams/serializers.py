from rest_framework import serializers
from exams.models import Assessment
from datetime import datetime,timezone,timedelta
class AssesmentSerializers(serializers.ModelSerializer):

    class Meta:

        model=Assessment

        fields="__all__"

        read_only_fields=["id","end_time","created_by"]


    def validate(self, data):
        exam_date = data.get(
            "exam_date",
            getattr(self.instance, "exam_date", None)
        )

        start_time = data.get(
            "start_time",
            getattr(self.instance, "start_time", None)
        )

        duration = data.get(
            "duration",
            getattr(self.instance, "duration", None)
        )

        if exam_date and start_time and duration is not None:
            start = datetime.combine(exam_date, start_time)
            end = start + timedelta(minutes=duration)

            if end.date() != exam_date:
                raise serializers.ValidationError({
                    "duration": "Exam must finish on the same date."
                })

            now = timezone.localtime().replace(tzinfo=None)

            if start < now:
                raise serializers.ValidationError({
                    "start_time": "Exam cannot be scheduled in the past."
                })

        return data