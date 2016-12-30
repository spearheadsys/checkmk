// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
//
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
//
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// tails. You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.

#ifndef ServiceListStateColumn_h
#define ServiceListStateColumn_h

#include "config.h"  // IWYU pragma: keep
#include <cstdint>
#include <string>
#include "IntColumn.h"
#include "nagios.h"

class ServiceListStateColumn : public IntColumn {
public:
    // TODO(sp) Remove the magic arithmetic
    enum class Type {
        num_ok = 0,
        num_warn = 1,
        num_crit = 2,
        num_unknown = 3,
        num_pending = 4,
        worst_state = -2,
        num_hard_ok = (0 + 64),
        num_hard_warn = (1 + 64),
        num_hard_crit = (2 + 64),
        num_hard_unknown = (3 + 64),
        worst_hard_state = (-2 + 64),
        num = -1
    };

    ServiceListStateColumn(const std::string &name,
                           const std::string &description, Type logictype,
                           int offset, int indirect_offset, int extra_offset)
        : IntColumn(name, description, indirect_offset, extra_offset, -1)
        , _offset(offset)
        , _logictype(logictype) {}
    int32_t getValue(void *row, contact *auth_user) override;
    servicesmember *getMembers(void *data);
    static int32_t getValue(Type logictype, servicesmember *mem,
                            contact *auth_user);
    static bool svcStateIsWorse(int32_t state1, int32_t state2);

private:
    int _offset;
    const Type _logictype;
};

#endif  // ServiceListStateColumn_h
