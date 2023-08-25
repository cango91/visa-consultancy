from forms_service.models import FormDefinition
from forms_service.factories.field_factory import FieldFactory
from django.http import JsonResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET

## API ENDPOINTS FOR FORMS WIZARD ##
## TODO: @login_required for all
## TODO: @employee_required for static field and validator endpoints

@require_GET
## get all form definitions
def get_definitions(request):
    definitions = FormDefinition.objects.filter(status__in=['active', 'draft', 'pending_approval'])
    serialized_definitions = [{'name': d.name, 'status': d.status, 'description': d.description, 'version': d.version, 'definition': d.definition, 'translations':d.translations, 'default_lang_code': d.default_lang_code, 'created_at': str(d.created_at), 'created_by__name': d.created_by.name} for d in definitions]
    return JsonResponse(serialized_definitions, encoder=DjangoJSONEncoder, safe=False)

@require_GET
## get single form definition
def get_definition(request,pk):
    d = get_object_or_404(FormDefinition,pk=pk)
    serialized_definition = {'name': d.name, 'status': d.status, 'description': d.description, 'version': d.version, 'definition': d.definition, 'translations':d.translations, 'default_lang_code': d.default_lang_code, 'created_at': str(d.created_at), 'created_by__name': d.created_by.name}
    return JsonResponse(serialized_definition, encoder=DjangoJSONEncoder, safe=False)

@require_GET
## get all available fields
def get_all_fields(request):
    available = list(FieldFactory.FIELD_CLASSES.keys())
    return JsonResponse(available, encoder=DjangoJSONEncoder, safe=False)

@require_GET
## get details for a single field
def get_field(request,field_type):
    field = FieldFactory.FIELD_INFO.get(field_type.lower())
    if not field:
        return Http404()
    return JsonResponse(field,encoder=DjangoJSONEncoder,safe=False)
