from django.middleware.locale import LocaleMiddleware
from django.utils import translation

class CustomLocaleMiddleware(LocaleMiddleware):
    def get_language_from_request(self, request):
        # Get the language from the session
        language = request.session.get('django_language')
        if language:
            request.LANGUAGE_CODE = language
            return language
        # If session variable is not set, fall back to the default language
        return translation.get_language_from_path(request.path_info)
    
    def process_request(self, request):
        translation.activate(self.get_language_from_request(request))
        #return super().process_request(request)