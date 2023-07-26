from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class getUserDetails(viewsets.ViewSet):

    http_method_names = ['get']
    def list(self, request):
        try:
            ourusername = request.GET["username"]
            queryset  = User.objects.filter(username=ourusername)
            serializer = getUserSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(None)

    queryset = User.objects.all()
    serializer_class = getUserSerializer

class createUser(viewsets.ModelViewSet):
    http_method_names = ["post"]
    serializer_class = createUserSerializer

class createPackage(viewsets.ModelViewSet):
    http_method_names = ["post"]
    serializer_class = createPackageSerializer

    def create(self, request):
        try:
            if Package.objects.get(name=request.POST["name"]):
                return Response("error", 400)
        except:
            ad = Admin.objects.get(username =request.POST["admin"])
            p = Package(name=request.POST["name"],admin=ad,destination=request.POST["destination"],description=request.POST["description"],no_of_people=request.POST["no_of_people"],no_of_days=request.POST["no_of_days"],cost_per_head=request.POST["cost_per_head"])
            p.save()
            return Response("success")
        
class activatePackage(viewsets.ModelViewSet):
    http_method_names = ["post"]
    serializer_class = activatePackageSerializer

    def create(self, request):
        p= Package.objects.get(name=request.POST["package"])
        ap = ActivePackage(package=p, start_date=request.POST["start_date"],end_date=request.POST["end_date"],last_date_of_booking=request.POST["last_date_of_booking"])
        ap.save()
        return Response("success")


class getParticipants(viewsets.ViewSet):
    http_method_names = ["get"]

    def list(self, request):
            try:
                ourname = request.GET["package"]
                ourpackage = Package.objects.get(name=ourname)
                ouractivepackage = ActivePackage.objects.get(package=ourpackage)
                queryset = [x.user for x in Participant.objects.filter(activepackage = ouractivepackage)]
                serializer = getUserSerializer(queryset, many=True)
                return Response(serializer.data)
            except:
                return Response(None)
    
class getPackages(viewsets.ViewSet):
    http_method_names = ["get"]
    def list(self, request):
        try:
            ouradmin = Admin.objects.get(username=request.GET["admin"])
            queryset = Package.objects.filter(admin = ouradmin)
            serializer = getPackageSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response("error", 400)

class getActivePackages(viewsets.ViewSet):
    http_method_names = ["get"]
    def list(self, request):
        try:
            ourusername = request.GET["user"]
            ouruser = User.objects.get(username=ourusername)
            partipates = Participant.objects.filter(user = ouruser)
            queryset = [x.activepackage for x in partipates]
            serializer = getActivePackageSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
                pass
        try:    
            ourusername = request.GET["admin"]
            ouradmin = Admin.objects.get(username=ourusername)
            packages = Package.objects.filter(admin = ouradmin)
            queryset = []
            for x in packages:
                if ActivePackage.objects.filter(package=x):
                    queryset.extend(ActivePackage.objects.get(package=x))
            serializer = getActivePackageSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            pass
        try:
            queryset = ActivePackage.objects.all()
            serializer = getActivePackageSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            pass
        
class createAdmin(viewsets.ModelViewSet):
    http_method_names = ["post"]
    serializer_class = createAdminSerializer

class getAdminDetails(viewsets.ViewSet):
    http_method_names = ["get"]

    def list(self, request):
        try:
            ourusername = request.GET["username"]
            queryset  = Admin.objects.filter(username=ourusername)
            serializer = getAdminSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(None)
    

    queryset = Admin.objects.all()
    serializer_class = getAdminSerializer

class DeactivatePackage(viewsets.ModelViewSet):
    http_method_names = ["post"]
    serializer_class = DeactivateSerializer
    
    def create(self,request):
        try:
            pack = Package.objects.get(name=request.POST["package"])
            active = ActivePackage.objects.get(package = pack)
            active.delete()
            return Response(request.POST["package"])
        except:
            return Response(None)
        
class ReviewPackage(viewsets.ModelViewSet):
    http_method_names = ["post"]
    serializer_class = createReviewSerializer
    def create(self,request):
        try:
            pack = Package.objects.get(name=request.POST["package"])
            user = User.objects.get(username=request.POST["username"])
            description = request.POST["description"]
            r = Review(package=pack, user = user, description=description)
            r.save()
            return Response(description)
        except:
            return Response(None)
        
class getReviews(viewsets.ViewSet):
    http_method_names = ["get"]
    
    def list(self, request):
        try:
            pack = Package.objects.get(name=request.GET["package"])
            queryset = Review.objects.filter(package = pack)
            serializer = getReviewSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(None)
        
class ApplyPackage(viewsets.ViewSet):
    http_method_names = ["post"]
    serializer_class = ApplyPackageSerializer

    def create(self, request):
        try:
            user = User.objects.get(username=request.POST["username"])
            pack = Package.objects.get(name = request.POST["activepackage"])
            activepackage = ActivePackage.objects.get(package=pack)
        except:
            return Response("unknown error", 400)
        
        try:
            if Participant.objects.get(activepackage=activepackage, user=user):
                return Response("applied before", 400)
        except: 
            p = Participant(activepackage=activepackage, user=user)
            p.save()
            return Response("success", 200)
        
class CancelPackage(viewsets.ViewSet):
    http_method_names = ["post"]
    serializer_class = ApplyPackageSerializer

    def create(self, request):
        try:
            user = User.objects.get(username=request.POST["username"])
            pack = Package.objects.get(name = request.POST["activepackage"])
            activepackage = ActivePackage.objects.get(package=pack)
            p = Participant.objects.get(activepackage=activepackage, user=user)
            p.delete()
            return Response("canceled", 200)
        except: 
            return Response("error", 400)






        



