from django.shortcuts import generic
from rest_framework.views import APIView
from models import Links

class PostListAPI(generic. ListAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateAPI(generic.CreateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailAPI(generic.RetrieveAPIView): 
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateAPI(generic. UpdateAPIView):
     queryset = Links.objects.filter(active=True)
     serializer_class = LinkSerializer

class postDeleteAPI(generic.DestroyAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer
class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)    


       



 
