from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'consultant_doctor'

urlpatterns = [

    path('consultantDoctor_dashboard',views.consultantDoctor_dashboard,name='consultantDoctor_dashboard'),
    path('logout_view',views.logout_view,name="logout_view"),
    path('consultantDoctor_patientList',views.consultantDoctor_patientList,name="consultantDoctor_patientList"),
    path('consultantDoctor_appointmentList',views.consultantDoctor_appointmentList,name="consultantDoctor_appointmentList"),
    path('consultantDoctor_patientDiagonise/<str:appointment_id>/',views.consultantDoctor_patientDiagonise,name="consultantDoctor_patientDiagonise"),
    path('consultantDoctor_patientDiagonise_View_Edit/<str:patient_id>/',views.consultantDoctor_patientDiagonise_View_Edit,name="consultantDoctor_patientDiagonise_View_Edit"),
    path('consultantDoctor_precribeTest/<str:appointment_id>/',views.consultantDoctor_precribeTest,name="consultantDoctor_precribeTest"),
    path('consultantDoctor_prescription',views.consultantDoctor_prescription,name='consultantDoctor_prescription'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)