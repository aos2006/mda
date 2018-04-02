from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    print('from custom errokr handler')
    if response is not None:
        errors = []
        for msg in response.data.values():
            errors.append({'message': msg[0], 'error': get_error_message()})

        response.data = {"errors": errors}

    return response
