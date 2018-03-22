from django.urls import path
from panel.views import IndexView, TableData


urlpatterns = [
    path('', IndexView.as_view(), name='index' ),
    path('table', TableData.as_view(), name='datatable' )
    ]