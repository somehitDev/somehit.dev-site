# -*- coding: utf-8 -*-
import pathlib, jinja2, aiohttp_jinja2
from datetime import datetime
from aiohttp import web
from aiohttp.web_request import Request
from sqlalchemy.engine import Engine


root_dir = pathlib.Path(__file__).resolve().parent
class BlogSite(web.Application):
    def __init__(self, engine:Engine, is_develop:bool):
        super().__init__()

        self.engine, self.is_develop =\
            engine, is_develop

        # routes
        self.add_routes([
            # assets
            web.static("/assets", str(root_dir.joinpath("assets"))),
            # routes
            web.get("/", self.index),
        ])

        # setup template
        aiohttp_jinja2.setup(
            self, loader = jinja2.FileSystemLoader(str(root_dir.joinpath("templates")))
        )

    
    async def index(self, req:Request):
        return aiohttp_jinja2.render_template(
            "index.html", req, {
                "baseUrl": "/blog/" if self.is_develop else "/",
                "portalUrl": "/portal/" if self.is_develop else "https://somehit.dev/",
                "yearString": "2024" if datetime.now().year == 2024 else f"2024-{datetime.now().year}"
            }
        )
