from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.profile import Profile

class UserProfile(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/user_profile.htm'

    def get(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        profile = Profile.objects.all().values()
        
        data = profile
        return Response({"status": status , "message": message ,  "data": data , "errors":errors})
