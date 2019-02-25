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
    Alternative,
    Dictionary,
    Filesize,
    Percentage,
    TextAscii,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)


@rulespec_registry.register
class RulespecCheckgroupParametersMssqlFileSizes(CheckParameterRulespecWithItem):
    @property
    def group(self):
        return RulespecGroupCheckParametersApplications

    @property
    def check_group_name(self):
        return "mssql_file_sizes"

    @property
    def title(self):
        return _("MSSQL Log and Data File Sizes")

    @property
    def match_type(self):
        return "dict"

    @property
    def parameter_valuespec(self):
        return Dictionary(
            title=_("File Size Levels"),
            elements=[
                ("data_files",
                 Tuple(
                     title=_("Levels for Datafiles"),
                     elements=[
                         Filesize(title=_("Warning at")),
                         Filesize(title=_("Critical at")),
                     ],
                 )),
                ("log_files",
                 Tuple(
                     title=_("Log files: Absolute upper thresholds"),
                     elements=[Filesize(title=_("Warning at")),
                               Filesize(title=_("Critical at"))],
                 )),
                ("log_files_used",
                 Alternative(
                     title=_("Levels for log files used"),
                     elements=[
                         Tuple(
                             title=_("Upper absolute levels"),
                             elements=[
                                 Filesize(title=_("Warning at")),
                                 Filesize(title=_("Critical at"))
                             ],
                         ),
                         Tuple(
                             title=_("Upper percentage levels"),
                             elements=[
                                 Percentage(title=_("Warning at")),
                                 Percentage(title=_("Critical at"))
                             ],
                         ),
                     ],
                 )),
            ],
        )

    @property
    def item_spec(self):
        return TextAscii(title=_("Service descriptions"), allow_empty=False)