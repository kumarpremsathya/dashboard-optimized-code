from django.urls import path
# from .views import show
from probe_agile_data import views

urlpatterns = [
    
    path('rbinewhome/', views.rbinewhome, name='rbinewhome'),
    path('rbi_tab/', views.rbi_tab, name='rbi_tab'),
    path('rbiget_data_for_popup1/<str:source_name>/', views.rbiget_data_for_popup1, name='rbiget_data_for_popup1'),
    path('rbinewfema_datefilter/', views.rbinewfema_datefilter, name='rbinewfema_datefilter'),
    path('rbinewecb_datefilter/', views.rbinewecb_datefilter, name='rbinewecb_datefilter'),
    path('rbinewodi_datefilter/', views.rbinewodi_datefilter, name='rbinewodi_datefilter'),
    path('rbinewstartupindia_datefilter/', views.rbinewstartupindia_datefilter, name='rbinewstartupindia_datefilter'),
    # path('rbiget_data_for_popup123/<str:source_name>/', views.rbiget_data_for_popup123, name='rbiget_data_for_popup123'),
    # path('rbinewhome123/', views.rbinewhome123, name='rbinewhome123'),
    
    path('mca_roc_datefilter/', views.mca_roc_datefilter, name='mca_roc_datefilter'),
    path('mca_rd_datefilter/', views.mca_rd_datefilter, name='mca_rd_datefilter'),
    path('sebi_so_datefilter/', views.sebi_so_datefilter, name='sebi_so_datefilter'),
    path('sebi_ao_datefilter/', views.sebi_ao_datefilter, name='sebi_ao_datefilter'),
    path('sebi_ed_datefilter/', views.sebi_ed_datefilter, name='sebi_ed_datefilter'),
    path('sebi_members_datefilter/', views.sebi_members_datefilter, name='sebi_members_datefilter'),
    path('sebi_ed_datefilter/', views.sebi_ed_datefilter, name='sebi_ed_datefilter'),
   

]



