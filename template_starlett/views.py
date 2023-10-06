# views.py
from starlette.templating import Jinja2Templates
import settings

templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))


async def home(request):
    template = "index.html"
    context = {"request": request,
               "total": 100,
               "chapters": [{
                   "chapter": "Cucu",
                   "cnum": 1
               }]}
    return templates.TemplateResponse(template, context=context)
