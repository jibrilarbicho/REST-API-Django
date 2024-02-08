from rest_framework import serializers
from watchlist_app.models import Movie


def length(value):
    if len(value) < 6:
        raise serializers.ValidationError(f"{value} is too short")


class Movieserilizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[length])
    description = serializers.CharField(validators=[length])
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value  # value is field name in this it is name

    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError("Name and description are no the same")
        else:
            return data
