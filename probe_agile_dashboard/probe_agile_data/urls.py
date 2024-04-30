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
    
    
    
    path('irdai_life_insurers_datefilter/', views.irdai_life_insurers_datefilter, name='irdai_life_insurers_datefilter'),
    path('irdai_general_insurers_datefilter/', views.irdai_general_insurers_datefilter, name='irdai_general_insurers_datefilter'),
    path('irdai_health_insurers_datefilter/', views.irdai_health_insurers_datefilter, name='irdai_health_insurers_datefilter'),
    path('irdai_reinsurers_datefilter/', views.irdai_reinsurers_datefilter, name='irdai_reinsurers_datefilter'),
    path('irdai_reinsurer_branches_datefilter/', views.irdai_reinsurer_branches_datefilter, name='irdai_reinsurer_branches_datefilter'),
    path('irdai_corporate_surveyors_datefilter/', views.irdai_corporate_surveyors_datefilter, name='irdai_corporate_surveyors_datefilter'),
    path('irdai_partner_surveyors_datefilter/', views.irdai_partner_surveyors_datefilter, name='irdai_partner_surveyors_datefilter'),
    path('irdai_third_party_administrators_datefilter/', views.irdai_third_party_administrators_datefilter, name='irdai_third_party_administrators_datefilter'),
    path('irdai_web_aggregators_datefilter/', views.irdai_web_aggregators_datefilter, name='irdai_web_aggregators_datefilter'),
    path('irdai_insurance_repositories_datefilter/', views.irdai_insurance_repositories_datefilter, name='irdai_insurance_repositories_datefilter'),
    path('irdai_insurance_marketing_firms_datefilter', views.irdai_insurance_marketing_firms_datefilter, name='irdai_insurance_marketing_firms_datefilter'),
    path('irdai_corporate_agents_datefilter/', views.irdai_corporate_agents_datefilter, name='irdai_corporate_agents_datefilter'),
    path('irdai_telemarketer_datefilter/', views.irdai_telemarketer_datefilter, name='irdai_telemarketer_datefilter'),
    
    path('pfrda_aggregators_datefilter/', views.pfrda_aggregators_datefilter, name='pfrda_aggregators_datefilter'),
    path('pfrda_cra_datefilter/', views.pfrda_cra_datefilter, name='pfrda_cra_datefilter'),
    path('pfrda_custodian_datefilter/', views.pfrda_custodian_datefilter, name='pfrda_custodian_datefilter'),
    path('pfrda_pension_funds_datefilter/', views.pfrda_pension_funds_datefilter, name='pfrda_pension_funds_datefilter'),
    path('pfrda_pop_datefilter/', views.pfrda_pop_datefilter, name='pfrda_pop_datefilter'),
    path('pfrda_pop_se_datefilter/', views.pfrda_pop_se_datefilter, name='pfrda_pop_se_datefilter'),
    path('pfrda_ra_individual_datefilter/', views.pfrda_ra_individual_datefilter, name='pfrda_ra_individual_datefilter'),
    path('pfrda_ra_renewal_datefilter/', views.pfrda_ra_renewal_datefilter, name='pfrda_ra_renewal_datefilter'),
    path('pfrda_trustee_bank_datefilter/', views.pfrda_trustee_bank_datefilter, name='pfrda_trustee_bank_datefilter'),
]



