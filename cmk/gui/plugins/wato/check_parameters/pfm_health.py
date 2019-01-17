#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Percentage,
    TextAscii,
    Tuple,
)
from cmk.gui.plugins.wato import (
    RulespecGroupCheckParametersStorage,
    register_check_parameters,
)

register_check_parameters(
    RulespecGroupCheckParametersStorage, "pfm_health", _("PCIe flash module"),
    Dictionary(
        elements=[
            (
                "health_lifetime_perc",
                Tuple(
                    title=_("Lower levels for health lifetime"),
                    elements=[
                        Percentage(title=_("Warning if below"), default_value=10),
                        Percentage(title=_("Critical if below"), default_value=5)
                    ],
                ),
            ),
        ],),
    TextAscii(
        title=_("Number or ID of the disk"),
        help=_("How the disks are named depends on the type of hardware being "
               "used. Please look at already discovered checks for examples.")), "dict")
