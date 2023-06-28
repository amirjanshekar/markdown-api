from django.shortcuts import render
from rest_framework.views import APIView


class ApiView(APIView):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'svg.svg',
            {
                'name': request.query_params.get('name'),
                'color': request.query_params.get('color'),
            }, content_type='image/svg+xml'
        )
