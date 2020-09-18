from rest_framework import serializers
from pictures.models import Pictures, Blog_entry


class PictureSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Pictures
        fields = ('id', 'owner', 'image')





class Blog_entrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    pictures = PictureSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = Blog_entry
        fields = ('id', 'title', 'owner', 'description', 'pictures', 'created_at', 'updated_at')

# class PictureSerializer(serializers.py.ModelSerializer):
#    # model Customer is user defined and it consist of three
#    # fields id, name, and address
#    class Meta:
#       model = Pictures
#       fields = ('field', 'image', 'image_url')
#
#       def get_photo_url(self, pictures):
#          request = self.context.get('request')
#          photo_url = pictures.photo.url
#          return request.build_absolute_uri(photo_url)
#
#
