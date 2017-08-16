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

#include "NegatingFilter.h"
#include <algorithm>
#include "FilterVisitor.h"
#include "Row.h"

using std::move;
using std::unique_ptr;

NegatingFilter::NegatingFilter(unique_ptr<Filter> filter)
    : _filter(move(filter)) {}

void NegatingFilter::accept(FilterVisitor &v) const { v.visit(*this); }

#ifdef CMC
const unique_ptr<Filter> &NegatingFilter::subfilter() const { return _filter; }
#endif

bool NegatingFilter::accepts(Row row, const contact *auth_user,
                             int timezone_offset) const {
    return !_filter->accepts(row, auth_user, timezone_offset);
}
