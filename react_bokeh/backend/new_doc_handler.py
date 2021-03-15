# coding=utf-8
"""
Create on 2021/3/15 16:07
@desc   : 
@author : wurenxi
@File   : new_doc_handler
"""
import json

from bokeh.embed.bundle import bundle_for_objs_and_resources
from bokeh.server.views.session_handler import SessionHandler
from tornado.web import authenticated


class NewDocHandler(SessionHandler):
    @authenticated
    async def get(self, *args, **kwargs):
        session = await self.get_session()

        bundle = bundle_for_objs_and_resources(None, self.application.resources())

        render_item = {
            "token": session.token,
            "use_for_title": True,
            "bundle": {
                "js_files": bundle.js_files,
                "js_raw": bundle.js_raw,
                "css_files": bundle.css_files,
                "css_raw": bundle.css_raw
            }
        }

        self.write(json.dumps(render_item))
