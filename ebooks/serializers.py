from rest_framework import serializers
from .models import Ebook,Review




class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)
    


    class Meta:
        model = Review
        exclude = ('updated_at','ebook')




class EbookSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    rate_avg = serializers.SerializerMethodField()
    number_of_rates = serializers.SerializerMethodField()

    class Meta:
        model = Ebook
        fields = '__all__'

    def get_number_of_rates(self,instance):
        return instance.reviews.count()    

    def get_rate_avg(self,instance):
        total = 0
        reviews = Review.objects.filter(ebook=instance)
        for review in reviews :
            total += review.rating
        
        if len(reviews) > 0:
            return total / len(reviews)
        return 0    

     






    




