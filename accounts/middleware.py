from django.core.exceptions import PermissionDenied
from django.urls import resolve


class CKEditorPathMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url_resolved = resolve(request.path_info)
        url_expected = 'ck_editor_5_upload_file'
        if url_resolved.url_name == url_expected and not request.user.is_staff:
              raise PermissionDenied
        return self.get_response(request)
