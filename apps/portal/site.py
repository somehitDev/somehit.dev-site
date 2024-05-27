# -*- coding: utf-8 -*-
import pathlib, jinja2, aiohttp_jinja2
from datetime import datetime
from aiohttp import web
from aiohttp.web_request import Request
from sqlalchemy.engine import Engine


root_dir = pathlib.Path(__file__).resolve().parent
class PortalSite(web.Application):
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
            web.get("/career/", self.career),
            web.get("/resume/", self.resume)
        ])

        # setup template
        aiohttp_jinja2.setup(
            self, loader = jinja2.FileSystemLoader(str(root_dir.joinpath("templates")))
        )


    async def index(self, req:Request):
        return aiohttp_jinja2.render_template(
            "index.html", req, {
                "baseUrl": "/portal/" if self.is_develop else "/",
                "blogUrl": "/blog/" if self.is_develop else "https://blog.somehit.dev",
                "yearString": "2024" if datetime.now().year == 2024 else f"2024-{datetime.now().year}"
            }
        )

    async def career(self, req:Request):
        return aiohttp_jinja2.render_template(
            "career.html", req, {
                "baseUrl": "/portal/" if self.is_develop else "/",
                "blogUrl": "/blog/" if self.is_develop else "https://blog.somehit.dev",
                "currentPage": "career",
                "yearString": "2024" if datetime.now().year == 2024 else f"2024-{datetime.now().year}",
                "totalYear": datetime.now().year - 2016,
                "careerHistory": {
                    "2016": [
                        { "month": "03", "subject": "Joined Engivice Inc.", "content": "Common Software Dev(Staff)" },
                        { "month": "10", "subject": "Joined Dataguru Inc.", "content": "Common Software Dev(Staff)" },
                    ],
                    "2017": [
                        { "month": "05", "subject": "Joined Haneol-Solution Inc.", "content": "UI/UX Dev(Staff)" }
                    ],
                    "2018": [
                        { "month": "01", "subject": "Position Changed", "content": "Engineer IT Dev(Senior)" },
                        { "month": "11", "subject": "Project", "content": "QSI-Laser MES Data-Processing(1st)" }
                    ],
                    "2019": [
                        { "month": "05", "subject": "Project", "content": "QSI-Laser MES Data-Processing(2nd)" }
                    ],
                    "2020": [
                        { "month": "01", "subject": "Position Changed", "content": "Engineer IT Dev(Assistant Manager)" },
                        { "month": "06", "subject": "Project", "content": "Failure Prediction by temperature/humidity(ML)" }
                    ],
                    "2021": [
                        { "month": "01", "subject": "Project", "content": "Excel template managing and Data monitoring" }
                    ],
                    "2022": [
                        { "month": "01", "subject": "Position Changed", "content": "Engineer IT Dev(Manager)" }
                    ],
                    "2023": [
                        { "month": "01", "subject": "Position Changed", "content": "JMP JSL Engineer Dev(Manager)" },
                        { "month": "08", "subject": "Project", "content": "QSI-Laser MES Data-Processing(3rd)" }
                    ],
                    "2024": [
                        { "month": "02", "subject": "Project", "content": "QSI-Laser MES Data-Processing(4th)" },
                        { "month": "04", "subject": "Event", "content": "JMP Korea Discovery Seminar(Seoul)" }
                    ]
                }
            }
        )

    async def resume(self, req:Request):
        return aiohttp_jinja2.render_template(
            "resume.html", req, {
                "baseUrl": "/portal/" if self.is_develop else "/",
                "blogUrl": "/blog/" if self.is_develop else "https://blog.somehit.dev",
                "currentPage": "resume",
                "yearString": "2024" if datetime.now().year == 2024 else f"2024-{datetime.now().year}"
            }
        )
