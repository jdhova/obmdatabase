from rest_framework.views import APIView
from rest_framework.response import Response
import ApiApp.controller as ctrl


# Create your views here.
class GetMembersList(APIView):
    @staticmethod
    def get(request):
        response_status, response_object = ctrl.get_members_list(request.query_params)
        return Response(response_object, status=response_status)


class GetMemberById(APIView):
    @staticmethod
    def get(request):
        response_status, response_object = ctrl.get_member_by_id(request.query_params)
        return Response(response_object, status=response_status)


class PatchMember(APIView):

    @staticmethod
    def patch(request):
        response_status, response_obj = ctrl.patch_member(request.data)
        return Response(response_obj, status=response_status)


class UpdateMember(APIView):

    @staticmethod
    def post(request):
        response_status, response_obj = ctrl.update_member(request.data)
        return Response(response_obj, status=response_status)


class DeleteMember(APIView):

    @staticmethod
    def post(request):
        response_status, response_obj = ctrl.delete_member(request.data)
        return Response(response_obj, status=response_status)
