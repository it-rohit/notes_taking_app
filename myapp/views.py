# yourapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny


from .serializers import RegisterSerializer, LoginSerializer, NotesSerializer
from .models import Notes

from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from django.shortcuts import get_object_or_404


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    # Add custom data for refresh and access tokens
    refresh['username'] = user.username
    refresh['email'] = user.email
    # refresh['id'] = str(user.id) 
    refresh['user_id'] = str(user.id.hex)    

    access_token = refresh.access_token
    access_token['username'] = user.username
    access_token['email'] = user.email
    # access_token['user_id1'] = str(user.id)
    access_token['user_id'] = str(user.id.hex)    

    return {
        'refresh': str(refresh),
        'access': str(access_token),
    }


class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            tokens = get_tokens_for_user(user)
            return Response({
                "message": "User registered successfully",
                "tokens": tokens
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        # print(hai)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = get_tokens_for_user(user)
            return Response({
                "message": "Login successful",
                "tokens": tokens
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post (self,request):
        try:
           refresh_token = request.data.get("refresh") 
           if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
           print("Received refresh token:", refresh_token)
           token = RefreshToken(refresh_token)
           token.blacklist()
           return Response({"message": "Logout successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

## notes curd
class NotesListCreateView(APIView):

    # list all the notes for the current login user
    def get(self,request):
        notes = Notes.objects.filter(user=request.user)
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        print("data132",data)
        serializer = NotesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotesDetailView(APIView):    
    def get_object(self, note_id, user):
        return get_object_or_404(Notes, note_id=note_id, user=user)

    def get(self, request, note_id):
        note = self.get_object(note_id, request.user)
        serializer = NotesSerializer(note)
        return Response(serializer.data)

    def put(self, request, note_id):
        note = self.get_object(note_id, request.user)
        serializer = NotesSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, note_id):
        note = self.get_object(note_id, request.user)
        note.delete()
        return Response({"message": "Note deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

