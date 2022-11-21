from rest_framework import serializers


class SendMessageBotSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=250)
    phone = serializers.CharField(max_length=250, allow_null=True)
