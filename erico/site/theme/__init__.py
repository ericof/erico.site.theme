# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory as BaseMessageFactory
MessageFactory = BaseMessageFactory('erico.site.theme')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
