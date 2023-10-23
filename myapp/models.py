from django.db import models
from wagtailcodeblock.blocks import CodeBlock
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel



class HomePage(Page):
    body = StreamField([
                        ('code', CodeBlock(label='Code', default_language='python')),
                       ], use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body', heading="Blog"),
    ]
