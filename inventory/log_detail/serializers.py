from rest_framework import serializers

from .models import LogData,Varient,Item,Properties

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = (id, 'name')

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ('id', 'type', 'color' ,'size')

class VariantSerializer(serializers.ModelSerializer):
    properties = PropertySerializer()

    class Meta:
        model = Varient
        fields = ('id', 'name','selling_price', 'cost_price', 'properties','quantity')

class ItemSerializer(serializers.ModelSerializer):
    variant = VariantSerializer(many=True)

    class Meta:
        model = Item
        fields = ('id', 'name' , 'product_code' , 'brand' , 'variant')

    def create(self, validated_data):
        variant_data = validated_data.pop('variant')

        #Logger.info(variant,properties,validated_data)
        item = Item.objects.create(**validated_data)
        #for el in variant:
        for variant in variant_data:
            properties = variant.pop('properties')
            variant = Varient.objects.create(item=item,**variant)
            Properties.objects.create(variant=variant,**properties)

        #for el in properties:

        return item

    # def update(self, instance, validated_data):
    #     variant_data = validated_data.pop('variant')

class LogDataDetailsSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=50)
    action = serializers.CharField(max_length=10)
    variant= serializers.CharField(max_length=50)
    item = serializers.CharField(max_length=50)
    class Meta:
        model = LogData
        fields = ('id','created_at','item', 'variant' , 'action', 'user')


class LogDataSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=50)
    action = serializers.CharField(max_length=10)
    variant= serializers.CharField(max_length=50)
    item = serializers.CharField(max_length=50)
    class Meta:
        model = LogData
        fields = ('id','created_at','item', 'variant' , 'action', 'user')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("user")
        data.pop("item")
        data.pop("id")
        data.pop("variant")
        data.pop("action")
        data.pop("created_at")
        data['body'] = "User : {} performed {} action on {} for item {}".format(instance.user,instance.action , instance.variant, instance.item)
        return data
    # def __str__(self):
    #     return "User : {} performed {} action on {} for item {}".format(self.user,self.action , self.variant, self.item)
