from pathlib import Path
from render_engine.hookspecs import hook_impl
from render_engine.site import Site
from render_engine.page import Page


class RenderEngineI18n:
    @hook_impl
    def post_render_content(
            page: Page,
            settings: dict[str, any],
            site: Site,
    ):
        """Called after a page is rendered."""
        for lang in settings["RenderEngineI18n"]["languages"]:
            class LangPage(page):
                content_path = Path(settings["RenderEngineI18n"]["languages_path"]).joinpath(lang).joinpath(page.content_path).name
                Parser = page.Parser
            
            lang_page = LangPage()
            route = Path(lang)/settings["route"]
            print(route)
            site._render_output(route = route, page = lang_page)