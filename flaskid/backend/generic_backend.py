#!/usr/bin/env python

class GenericBackend(object):
    """
        Generic Authentication Class
    """

    def login(self, user, password):
        raise Exception("Not implemented")