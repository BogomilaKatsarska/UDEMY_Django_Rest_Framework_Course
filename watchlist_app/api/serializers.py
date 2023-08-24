from rest_framework import serializers
'''
from watchlist_app.models import Movie
'''
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    #below should use the same naming as in the model related_name --> One streaming platform has many watchlists
    # watchlist = WatchListSerializer(many=True, read_only=True)
    #below --> if we want to return what is in __str__ of our model
    # watchlist = serializers.StringRelatedField(many=True)
    # below --> if we want to return the pk
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # below --> access to the hyperlink of the movie
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watchlist details')
    class Meta:
        model = StreamPlatform
        fields = '__all__'



'''
class MovieSerializer(serializers.ModelSerializer):
    #how to add new field which is not specified in the model? see below:
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        # fields = '__all__'
        # fields = ['id', 'name', 'description']
        exclude = ['active']

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
        else:
            return value

    #as naming use: 'get_+field_name'
    def get_len_name(self, obj):
        length = len(obj.name)
        return length



def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short')


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True,
    )
    name = serializers.CharField(
        validators=name_length,
    )
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    #instance - carries old value
    #validated data - carries the new value
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    #We do not 'call' the validator anywhere. Just add validate_'field name' as a method here in the serializer
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short.')
        else:
            return value

    # Validate is applied to complete object
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and description should not be the same.')
        else:
            return data

'''