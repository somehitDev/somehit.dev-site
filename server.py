# -*- coding: utf-8 -*-
from aiohttp import web
from sqlalchemy import create_engine
from urllib.parse import quote_plus

app = web.Application()

if __name__ == "__main__":
    # get flags by argparse
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--develop", action = "store_true")
    parser.add_argument("--test", action = "store_true")
    args = parser.parse_args()

    # create engine to db
    if args.test:
        schema = "somehit_dev_test"
    else:
        schema = "somehit_dev"

    if args.develop:
        engine = create_engine(f"mysql+pymysql://root:{quote_plus('3!zRa9(#u]A$Tcf(')}@somehit.dev:33060/{schema}?charset=utf8mb4")
    else:
        engine = create_engine(f"mysql+pymysql://root:{quote_plus('3!zRa9(#u]A$Tcf(')}@127.0.0.1:3306/{schema}?charset=utf8mb4")

    del schema

    ## register apps
    # portal
    from apps.portal.site import PortalSite
    app.add_subapp("/portal", PortalSite(engine, args.develop))
    # blog
    from apps.blog.site import BlogSite
    app.add_subapp("/blog", BlogSite(engine, args.develop))

    # start server
    web.run_app(app, host = "127.0.0.1", port = 60000)
