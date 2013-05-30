# -*- encoding: utf-8 -*-
"""
Test widget rendering to HTML.
"""


import re

from flask_triangle.widget import Widget
from nose.tools import assert_true, assert_in


class TestRendering(object):

    def setup(self):
        self.widget = Widget(u'bound', name=u'name')

    def test_rendering_on_call(self):
        """
        When calling a widget instance it returns a string.
        """
        assert_true(issubclass(self.widget().__class__, unicode))

    def test_rendering_is_html(self):
        """
        Rendering of a widget is valid HTML.
        """
        assert_true(re.match(r'<("[^"]*"|\'[^\']*\'|[^\'">])*>',
                    self.widget()))

    def test_rendering_format(self):
        """
        Rendering of widget is formatabale
        """
        test = Widget(u'bound', name=u'name', string_format='{test}')
        assert_in('string_format="ok"', test(test=u'ok'))

    def test_rendering_angular(self):
        """
        If double bracket pairs "{{ }}" are used to insert angular expression
        are used, they are automatically escaped to be maintainded despites
        string format.
        """
        test = Widget(u'bound', name=u'name', angular='{{true}}')
        assert_in('angular="{{true}}"', test())

    def test_rendering_angular_format(self):
        """
        Rendering of widget is formatable inside doubled bracketed expressions.
        """
        test = Widget(u'bound', name=u'name', angular='{{{test}}}')
        assert_in('angular="{{ok}}"', test(test=u'ok'))
