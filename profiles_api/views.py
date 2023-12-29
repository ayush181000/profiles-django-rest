from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    
    def get(self,request,format=None):
        """Return a list of APIView Features"""
        an_apiView=[
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        
        return Response({'message':'Hello','an_apiView':an_apiView})