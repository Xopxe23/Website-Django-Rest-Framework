import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser

from .models import Women
from rest_framework.renderers import JSONRenderer


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Women
        fields = "__all__"


# def encode():
#     model = WomenModel('Анджелина Джоли', 'Контент Анджелины Джоли')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Angelina Jolie", "content": "Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream=stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
