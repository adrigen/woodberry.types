import doctest
import unittest

from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

import woodberry.types

OPTION_FLAGS = doctest.NORMALIZE_WHITESPACE | \
               doctest.ELLIPSIS

ptc.setupPloneSite(products=['woodberry.types'])


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            zcml.load_config('configure.zcml',
              woodberry.types)

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='woodberry.types',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='woodberry.types.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'INTEGRATION.txt',
            package='woodberry.types',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),

        # -*- extra stuff goes here -*-

        # Integration tests for HomepageFolder
        ztc.ZopeDocFileSuite(
            'HomepageFolder.txt',
            package='woodberry.types',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for Fullwidthsectionwithnotitle
        ztc.ZopeDocFileSuite(
            'Fullwidthsectionwithnotitle.txt',
            package='woodberry.types',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for FullWidthSection
        ztc.ZopeDocFileSuite(
            'FullWidthSection.txt',
            package='woodberry.types',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for TwoColumnSection
        ztc.ZopeDocFileSuite(
            'TwoColumnSection.txt',
            package='woodberry.types',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
