from django.shortcuts import render
from rest_framework.views import APIView


class ApiView(APIView):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'svg.html',
            {
                'name': request.query_params.get('name'),
                'color': request.query_params.get('color'),
            }
        )
