from django.urls import include, path
# import routers
from rest_framework import routers
from .views import *
 

router = routers.DefaultRouter()

router.register(r'activatepackage', activatePackage,basename='activatepackage')
router.register(r'createpackage', createPackage,basename='createpackage')
router.register(r'getpackages', getPackages,basename='getpackage')
router.register(r'cancelpackage', CancelPackage,basename='cancel')
router.register(r'applypackage', ApplyPackage,basename='apply')
router.register(r'reviewpackage', ReviewPackage,basename='review')
router.register(r'deactivatepackage', DeactivatePackage,basename='deact')
router.register(r'userprofile', getUserDetails,basename='userdetail')
router.register(r'adminprofile', getAdminDetails,basename='admindetail')
router.register(r'createuser', createUser, basename="createuser")
router.register(r'createadmin', createUser, basename="createadmin")
router.register(r'getparticipants', getParticipants, basename="getpart")
router.register(r'getactivepackages', getActivePackages, basename="getactive")
router.register(r'getreviews', getReviews, basename="getreviews")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]