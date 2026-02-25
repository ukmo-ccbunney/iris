# Copyright Iris contributors
#
# This file is part of Iris and is released under the BSD license.
# See LICENSE in the root of the repository for full licensing details.
"""Experimental support ZArr files files using CF conventions for metadata interpretation."""

import logging

import iris.config

# Note: *must* be done before importing from submodules, as they also use this !
logger: logging.Logger = iris.config.get_logger(__name__, propagate=True)
