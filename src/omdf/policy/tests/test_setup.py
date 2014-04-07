# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from omdf.policy.testing import IntegrationTestCase

import unittest2 as unittest


class TestsInstall(IntegrationTestCase):
    """Test installation of omdf.policy into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_portal_title(self):
        self.assertEqual(
            "Olimpiada Matemática del Distrito Federal",
            self.portal.getProperty('title')
        )

    def test_portal_description(self):
        self.assertEqual(
            "Bienvenido a la Olimpiada Matématica",
            self.portal.getProperty('description')
        )


def test_suite():
    """This """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
