from wagtail.core import blocks

class TextBlock(blocks.StructBlock):

    content = blocks.RichTextBlock(
        label='Text box',
        help_text='Content of the text field.',
    )
