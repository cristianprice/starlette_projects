# app.py
from starlette.applications import Starlette
import settings
import routes

app = Starlette(debug=settings.DEBUG, routes=routes.routes)
