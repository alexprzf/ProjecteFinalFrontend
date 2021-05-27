from django.http.response import FileResponse
from django.views import View
from .models import Dpor
from django.http import JsonResponse
from django.forms import model_to_dict

# Create your views here.
class getOutDatedDpors(View):
    def get(self, request, user):
        dpor = Dpor.objects.filter(user=user,isUpdated=False)
        list = []
        for d in dpor:
            list.append(d.path)
        return JsonResponse(list, safe=False)

class getFile(View):
    def get(self, request, user,path):
        try:
            dpor = Dpor.objects.get(user=user,path=path)
            return FileResponse(open(dpor.file.name,"rb"))
        except:
            return JsonResponse("null",safe=False)
class swapStatus(View):
    def get(self, request, user ,path):
        dpor = Dpor.objects.get(user=user,path=path)
        dpor.isUpdated = True
        dpor.save()
        return JsonResponse("OK",safe=False)
