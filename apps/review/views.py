# from rest_framework import status, permissions
# from rest_framework.generics import CreateAPIView
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Comment, Rating
# from .serializers import CommentSerializer, RatingSerializer
# from ..users.permissions import AnonPermissionOnly
#
#
# class CommentListAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     # authentication_classes = []
#     parser_classes = [JSONParser]
#
#     def get(self, request, partner_id):
#         snippets = Comment.objects.filter(partner_id=partner_id)
#         serializer = CommentSerializer(snippets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class RatingListAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     # authentication_classes = []
#     parser_classes = [JSONParser]
#
#     def get(self, request, partner_id):
#         snippets = Rating.objects.filter(partner_id=partner_id)
#         serializer = RatingSerializer(snippets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# # class CommentCreateAPIView(APIView):
# #     permission_classes = [permissions.AllowAny]
# #     # authentication_classes = []
# #     parser_classes = [JSONParser]
# #
# #     def post(self, request):
# #         serializer = CommentSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CommentCreateAPIView(CreateAPIView):
#     queryset = Comment.objects.all()
#     permission_classes = (AnonPermissionOnly,)
#     serializer_class = CommentSerializer
#
#
# class RatingCreateAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     # authentication_classes = []
#     parser_classes = [JSONParser]
#
#     def post(self, request):
#         serializer = RatingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
