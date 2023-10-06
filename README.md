# render-engine-i18n
Render Engine Plugin to create multiples language support for Pages and Collections

## Quick Start

### Installation

Install this plugin via pip:

```bash
pip install render-engine-i18n
```

### Configuration

```python
# import render_engine
from render_engine import Site, Page, Collection
# import the plugin
from render_engine_i18n import RenderEngineI18n

app = Site()

site_settings = {
    "plugins":
        languages: ['en', 'es', ...]
        default_language: 'en'
}

```

create a page at the same routes if there is an `en` page there. It will ignore routes. If the page doesn't exist, default to the default_language and add a variable `missing_language` eq true.
