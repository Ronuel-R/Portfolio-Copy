from rest_framework.renderers import TemplateHTMLRenderer,StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.social_acc_model import Social
from ..models.profile import Profile

class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/home.htm'

    def get(self, request):
        social = Social.objects.all().values()
        profile = Profile.objects.all().values()
        return Response({'social': social,'profile': profile})
