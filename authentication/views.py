from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

class UserRegistrationApiView(viewsets.ViewSet):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            print("token", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid", uid)
            confirm_link = f"https://pro-tasker-backend-1.onrender.com/active/{uid}/{token}"
            email_subject = "Confirm your email"
            email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})

            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response({'message': 'An email has been sent for confirmation'}, status=201)
        return Response(serializer.errors, status=400)
    
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid credentials'}, status=401)
        return Response(serializer.errors)

class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')