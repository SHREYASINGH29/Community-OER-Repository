from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class Render:

    @staticmethod
    def render(path: str, params: dict, filename):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        if os.path.isdir("communities/"+dirname):
            result = open("communities/"+dirname+'/'+filename, 'wb')
        else:
            os.makedirs("communities/"+dirname)
            result = open("communities/"+dirname+'/'+filename, 'wb')
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        result.close()
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)