# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import unittest2 as unittest


class OlympiadPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import omdf.policy
        self.loadZCML(package=omdf.policy, context=configurationContext)
        # import plone.app.contenttypes
        # self.loadZCML(
        #     package=plone.app.contenttypes,
        #     context=configurationContext
        # )

        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'Products.DateRecurringIndex')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        applyProfile(portal, 'omdf.policy:default')

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'omdf.policy')
        # z2.uninstallProduct(app, 'plone.app.contenttypes')

        # Uninstall old-style Products
        z2.uninstallProduct(app, 'Products.DateRecurringIndex')


FIXTURE = OlympiadPolicyLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="OlympiadPolicyLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="OlympiadPolicyLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """docstring for IntegrationTestCase"""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """docstring for FunctionalTestCase"""

    layer = FUNCTIONAL_TESTING
