from rest_framework.renderers import TemplateHTMLRenderer,StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.profile import Profile

class UserProfile(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/user_profile.htm'

    def get(self, request):
        profile = Profile.objects.all().values()
        return Response({'profile': profile})
