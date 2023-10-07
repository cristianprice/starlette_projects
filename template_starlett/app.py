# app.py
from starlette.applications import Starlette
import settings
import routes
import uvicorn


app = Starlette(debug=settings.DEBUG, routes=routes.routes)

if __name__ == '__main__':
    uvicorn.run(app=app, port=8000)
