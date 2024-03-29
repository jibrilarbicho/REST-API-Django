from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform, Review


# def length(value):
#     if len(value) < 6:
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ["watchlist"]


#         raise serializers.ValidationError(f"{value} is too short")
class Watchlistserilizer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Watchlist
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = Watchlistserilizer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True, read_only=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"

        # exclude = ["active"]

    # def get_len_name(self, object):
    #     return len(object.name)

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value  # value is field name in this it is name

    # def validate(self, data):
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError("Name and description are no the same")
    #     else:
    #         return data


# class Movieserilizer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[length])
#     description = serializers.CharField(validators=[length])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         return value  # value is field name in this it is name

#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Name and description are no the same")
#         else:
#             return data
