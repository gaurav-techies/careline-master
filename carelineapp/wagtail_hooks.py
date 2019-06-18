from wagtail.admin.rich_text.converters.editor_html import WhitelistRule
from wagtail.core import hooks
from wagtail.core.whitelist import allow_without_attributes, attribute_rule, check_url
from wagtail.admin.forms.choosers import ExternalLinkChooserForm
from django import forms
from django.core.exceptions import ValidationError
import re

@hooks.register('register_rich_text_features')
def blockquote_feature(features):
    # register a feature 'blockquote' which whitelists the <blockquote> element
    features.register_converter_rule('editorhtml', 'blockquote', [
        WhitelistRule('blockquote', allow_without_attributes),
    ])
    # register a feature 'a' which whitelists the <a> element
    features.register_converter_rule('editorhtml', 'a', [
        WhitelistRule('a', attribute_rule(
            {'href': check_url, 'target': True, 'data-toggle': True, 'data-url': True, 'data-target': True,
             'id': True})),
    ])
    # register a feature 'table' which whitelists the <table> element
    features.register_converter_rule('editorhtml', 'table', [
        WhitelistRule('table', attribute_rule({'style': True})),
    ])
    # register a feature 'table' which whitelists the <table> element
    features.register_converter_rule('editorhtml', 'tbody', [
        WhitelistRule('tbody', attribute_rule({'style': True})),
    ])
    # register a feature 'table' which whitelists the <table> element
    features.register_converter_rule('editorhtml', 'tr', [
        WhitelistRule('tr', attribute_rule({'style': True})),
    ])
    # register a feature 'table' which whitelists the <table> element
    features.register_converter_rule('editorhtml', 'td', [
        WhitelistRule('td', attribute_rule({'style': True})),
    ])
    # register a feature 'table' which whitelists the <table> element
    features.register_converter_rule('editorhtml', 'img', [
        WhitelistRule('img', attribute_rule({'alt': True})),
    ])
    # register a feature 'table' which whitelists the <table> element
    features.register_converter_rule('editorhtml', 'h1', [
        WhitelistRule('h1', attribute_rule({'id': True})),
    ])
    # add 'a' to the default feature set
    features.default_features.append('blockquote')
    # add 'a' to the default feature set
    features.default_features.append('a')
    # add 'table' to the default feature set
    features.default_features.append('table')
    # add 'tbody' to the default feature set
    features.default_features.append('tbody')
    # add 'tr' to the default feature set
    features.default_features.append('tr')
    # add 'td' to the default feature set
    features.default_features.append('td')
    # add 'img' to the default feature set
    features.default_features.append('img')
    # add 'h1' to the default feature set
    features.default_features.append('h1')

# Allow Tel in external links
def validate_url(value):

    regex = re.compile(
        r'^(http|https|tel):', re.IGNORECASE)

    regex = re.compile(regex)
    if not regex.match(value):
        raise ValidationError("Please Enter URL")

ExternalLinkChooserForm.base_fields['url'] = forms.CharField(label='URL', required=True, validators=[validate_url])



