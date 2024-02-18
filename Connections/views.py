from django.db.models import Count
from django.db.models.functions import TruncMonth, ExtractMonth
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Address,Reviewer,Application
from .serializers import AddressSerializer,ReviewerSerializer,ApplicationSerializer
# Create your views here.

class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class ReviewerViewSet(ModelViewSet):
    serializer_class = ReviewerSerializer
    queryset = Reviewer.objects.all()

class ApplicationViewSet(ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    def list(self, request, *args, **kwargs):
        query_params = request.query_params.dict()
        qs = self.queryset
        if 'id' in query_params and query_params.get('id') != 'undefined' and query_params.get('id') != '':
            qs = qs.filter(id=query_params.get('id'))
        if 'start_date' in query_params:
            qs = qs.filter(date__gte=query_params.get('start_date'))
        if 'end_date' in query_params:
            qs = qs.filter(date__lte=query_params.get('end_date'))
        return Response(self.serializer_class(qs,many=True).data)

    @action(url_path='dashboard_api',methods=['GET'],detail=False)
    def dashboard_api(self,request):
        qs = self.queryset
        status = request.query_params.get('status',None)
        if status is not None and status != '':
            qs = qs.filter(status=status)
        #qs = qs.values_list('date__month',flat=True).annotate(count=Count(id))
        output = []
        import calendar
        for i in range(1,13):
            output.append({'name':calendar.month_name[i],'count':qs.filter(date__month=i).count()})
        return Response(output)
