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
    Integer,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)


@rulespec_registry.register
class RulespecCheckgroupParametersSkypeMediationServer(CheckParameterRulespecWithoutItem):
    @property
    def group(self):
        return RulespecGroupCheckParametersApplications

    @property
    def check_group_name(self):
        return "skype_mediation_server"

    @property
    def title(self):
        return _("Skype for Business Mediation Server")

    @property
    def match_type(self):
        return "dict"

    @property
    def parameter_valuespec(self):
        return Dictionary(elements=[
            ('load_call_failure_index',
             Dictionary(
                 title=_("Load Call Failure Index"),
                 elements=[
                     ("upper",
                      Tuple(elements=[
                          Integer(title=_("Warning at"), default_value=10),
                          Integer(title=_("Critical at"), default_value=20),
                      ],)),
                 ],
                 optional_keys=[],
             )),
            ('failed_calls_because_of_proxy',
             Dictionary(
                 title=_("Failed calls caused by unexpected interaction from proxy"),
                 elements=[
                     ("upper",
                      Tuple(elements=[
                          Integer(title=_("Warning at"), default_value=10),
                          Integer(title=_("Critical at"), default_value=20),
                      ],)),
                 ],
                 optional_keys=[],
             )),
            ('failed_calls_because_of_gateway',
             Dictionary(
                 title=_("Failed calls caused by unexpected interaction from gateway"),
                 elements=[
                     ("upper",
                      Tuple(elements=[
                          Integer(title=_("Warning at"), default_value=10),
                          Integer(title=_("Critical at"), default_value=20),
                      ],)),
                 ],
                 optional_keys=[],
             )),
            ('media_connectivity_failure',
             Dictionary(
                 title=_("Media Connectivity Check Failure"),
                 elements=[
                     ("upper",
                      Tuple(elements=[
                          Integer(title=_("Warning at"), default_value=1),
                          Integer(title=_("Critical at"), default_value=2),
                      ],)),
                 ],
                 optional_keys=[],
             )),
        ],)
