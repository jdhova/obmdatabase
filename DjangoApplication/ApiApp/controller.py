from ApiApp.models import *
from ApiApp.serializers import *
from rest_framework import status


def get_members_list(params):
    try:
        expected_parameters = ['firstName', 'lastName', 'companyName', 'companyAddress']
        parameter_check_bool = True
        for param in params:
            if param not in expected_parameters:
                parameter_check_bool = False
                break

        if parameter_check_bool:
            members_list_query = Member.objects.all()
            if 'firstName' in params:
                members_list_query = members_list_query.filter(first_name=params['firstName'])

            if 'lastName' in params:
                members_list_query = members_list_query.filter(last_name=params['lastName'])

            if 'companyName' in params:
                members_list_query = members_list_query.filter(company_name=params['companyName'])

            if 'companyAddress' in params:
                members_list_query = members_list_query.filter(company_address=params['companyAddress'])

            members_list = MemberSerializer(members_list_query, many=True).data

            if len(members_list) == 0:
                message = "No members available"
                response_status = status.HTTP_204_NO_CONTENT
            else:
                message = "Members list retrieved successfully"
                response_status = status.HTTP_404_NOT_FOUND

        else:
            message = "Invalid parameters"
            response_status = status.HTTP_400_BAD_REQUEST
            members_list = None

        response_data = {
            'message': message,
            'members_list': members_list
        }

    except Exception as e:
        message = 'Internal Server Error'
        response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        response_data = {
            'message': message,
            'members_list': None
        }
    return response_status, response_data


def get_member_by_id(params):
    expected_parameters = ['id']
    parameter_check_bool = True
    for param in params:
        if param not in expected_parameters:
            parameter_check_bool = False
            break
    if parameter_check_bool:
        if 'id' in params:
            try:
                member_query = Member.objects.get(id=params['id'])
                message = 'Member retrieved successfully'
                member = MemberSerializer(member_query, many=False).data
                response_status = status.HTTP_200_OK
                response_data = {
                    'message': message,
                    'member': member
                }

            except Member.DoesNotExist:
                message = 'No such member exist'
                response_status = status.HTTP_404_NOT_FOUND
                response_data = {
                    'message': message,
                    'member': None
                }
        else:
            message = 'Please provide user id'
            response_status = status.HTTP_400_BAD_REQUEST
            response_data = {
                'message': message,
                'member': None
            }
    else:
        message = "Invalid parameters"
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {
            'message': message,
            'member': None
        }

    return response_status, response_data


def patch_member(params):
    expected_parameters = ['id', 'fieldsToPatch']
    parameter_check_bool = True
    for param in params:
        if param not in expected_parameters:
            parameter_check_bool = False
            break
    if parameter_check_bool:
        if 'id' in params:
            try:
                member_query = Member.objects.get(id=params['id'])
                if 'fieldsToPatch' in params:
                    fields_to_update = params['fieldsToPatch']

                    if 'firstName' in fields_to_update:
                        member_query.first_name = fields_to_update['firstName']
                    if 'infix' in fields_to_update:
                        member_query.infix = fields_to_update['infix']
                    if 'lastName' in fields_to_update:
                        member_query.last_name = fields_to_update['lastName']
                    if 'photo' in fields_to_update:
                        member_query.photo = fields_to_update['photo']
                    if 'companyName' in fields_to_update:
                        member_query.company_name = fields_to_update['companyName']
                    if 'jobTitle' in fields_to_update:
                        member_query.job_title = fields_to_update['jobTitle']
                    if 'companyPhoto' in fields_to_update:
                        member_query.company_photo = fields_to_update['companyPhoto']
                    if 'companyAddress' in fields_to_update:
                        member_query.company_address = fields_to_update['companyAddress']

                member_query.save()
                message = 'Member patched successfully'
                member = MemberSerializer(member_query, many=False).data
                response_status = status.HTTP_200_OK
                response_data = {
                    'message': message,
                    'member': member
                }

            except Member.DoesNotExist:
                message = 'No such member exist'
                response_status = status.HTTP_404_NOT_FOUND
                response_data = {
                    'message': message,
                    'member': None
                }
        else:
            message = 'Please provide user id'
            response_status = status.HTTP_400_BAD_REQUEST
            response_data = {
                'message': message,
                'member': None
            }
    else:
        message = "Invalid parameters"
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {
            'message': message,
            'member': None
        }
    return response_status, response_data


def update_member(params):
    expected_parameters = ['id', 'fieldsToUpdate']
    parameter_check_bool = True
    for param in params:
        if param not in expected_parameters:
            parameter_check_bool = False
            break
    if parameter_check_bool:
        if 'id' in params:
            try:
                can_update = True
                member_query = Member.objects.get(id=params['id'])
                if 'fieldsToUpdate' in params:
                    fields_to_update = params['fieldsToUpdate']

                    if 'firstName' in fields_to_update:
                        member_query.first_name = fields_to_update['firstName']
                    else:
                        can_update = False
                    if 'infix' in fields_to_update:
                        member_query.infix = fields_to_update['infix']
                    else:
                        can_update = False
                    if 'lastName' in fields_to_update:
                        member_query.last_name = fields_to_update['lastName']
                    else:
                        can_update = False
                    if 'photo' in fields_to_update:
                        member_query.photo = fields_to_update['photo']
                    else:
                        can_update = False
                    if 'companyName' in fields_to_update:
                        member_query.company_name = fields_to_update['companyName']
                    else:
                        can_update = False
                    if 'jobTitle' in fields_to_update:
                        member_query.job_title = fields_to_update['jobTitle']
                    else:
                        can_update = False
                    if 'companyPhoto' in fields_to_update:
                        member_query.company_photo = fields_to_update['companyPhoto']
                    else:
                        can_update = False
                    if 'companyAddress' in fields_to_update:
                        member_query.company_address = fields_to_update['companyAddress']
                    else:
                        can_update = False
                if can_update:
                    member_query.save()
                    message = 'Member updated successfully'
                    member = MemberSerializer(member_query, many=False).data
                    response_status = status.HTTP_200_OK
                else:
                    message = 'Incomplete parameters'
                    member = None
                    response_status = status.HTTP_400_BAD_REQUEST

                response_data = {
                    'message': message,
                    'member': member
                }

            except Member.DoesNotExist:
                message = 'No such member exist'
                response_status = status.HTTP_404_NOT_FOUND
                response_data = {
                    'message': message,
                    'member': None
                }
        else:
            message = 'Please provide user id'
            response_status = status.HTTP_400_BAD_REQUEST
            response_data = {
                'message': message,
                'member': None
            }
    else:
        message = "Invalid parameters"
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {
            'message': message,
            'member': None
        }
    return response_status, response_data


def delete_member(params):
    expected_parameters = ['id']
    parameter_check_bool = True
    for param in params:
        if param not in expected_parameters:
            parameter_check_bool = False
            break
    if parameter_check_bool:
        if 'id' in params:
            try:
                member_query = Member.objects.get(id=params['id'])
                member_query.delete()
                message = 'Member deleted successfully'
                response_status = status.HTTP_200_OK
                response_data = {
                    'message': message
                }

            except Member.DoesNotExist:
                message = 'No such member exist'
                response_status = status.HTTP_404_NOT_FOUND
                response_data = {
                    'message': message
                }
        else:
            message = 'Please provide user id'
            response_status = status.HTTP_400_BAD_REQUEST
            response_data = {
                'message': message,
                'member': None
            }
    else:
        message = "Invalid parameters"
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {
            'message': message
        }

    return response_status, response_data

