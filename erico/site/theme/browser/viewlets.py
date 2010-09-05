# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import LogoViewlet
from plone.app.layout.viewlets.common import ViewletBase

class MyLogo(LogoViewlet):
    render = ViewPageTemplateFile("templates/logo.pt")