# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_grr_search"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     grr_search_type
    #     grr_search_value
    #   Message Destinations:
    #     fn_grr_search
    #   Functions:
    #     fn_grr_search
    #   Workflows:
    #     example_grr_search_by_ip
    #   Rules:
    #     GRR Search by IP


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJ1dWlkIjogIjU5NzEwMGM4LWM0Mjkt
NDIwOS1iMjc3LWJhYzc2MzlkMDU2OCIsICJkZXNjcmlwdGlvbiI6ICJBbiBleGFtcGxlIFdvcmtm
bG93IHVzaW5nIHRoZSBHUlIgU2VhcmNoIEZ1bmN0aW9uIHRvIGdldCBhIEdSUiBBZ2VudCdzIGlu
Zm9ybWF0aW9uIHVzaW5nIHRoZWlyIElQIEFkZHJlc3MuIiwgIm9iamVjdF90eXBlIjogImFydGlm
YWN0IiwgImV4cG9ydF9rZXkiOiAiZXhhbXBsZV9ncnJfc2VhcmNoX2J5X2lwIiwgIndvcmtmbG93
X2lkIjogMiwgImxhc3RfbW9kaWZpZWRfYnkiOiAicmVzYWRtaW5AZXhhbXBsZS5jb20iLCAiY29u
dGVudCI6IHsieG1sIjogIjw/eG1sIHZlcnNpb249XCIxLjBcIiBlbmNvZGluZz1cIlVURi04XCI/
PjxkZWZpbml0aW9ucyB4bWxucz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1
MjQvTU9ERUxcIiB4bWxuczpicG1uZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIw
MTAwNTI0L0RJXCIgeG1sbnM6b21nZGM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEw
MDUyNC9EQ1wiIHhtbG5zOm9tZ2RpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1
MjQvRElcIiB4bWxuczpyZXNpbGllbnQ9XCJodHRwOi8vcmVzaWxpZW50LmlibS5jb20vYnBtblwi
IHhtbG5zOnhzZD1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hXCIgeG1sbnM6eHNp
PVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2VcIiB0YXJnZXROYW1l
c3BhY2U9XCJodHRwOi8vd3d3LmNhbXVuZGEub3JnL3Rlc3RcIj48cHJvY2VzcyBpZD1cImV4YW1w
bGVfZ3JyX3NlYXJjaF9ieV9pcFwiIGlzRXhlY3V0YWJsZT1cInRydWVcIiBuYW1lPVwiRXhhbXBs
ZTogR1JSIFNlYXJjaCBieSBJUFwiPjxkb2N1bWVudGF0aW9uPjwhW0NEQVRBW0FuIGV4YW1wbGUg
V29ya2Zsb3cgdXNpbmcgdGhlIEdSUiBTZWFyY2ggRnVuY3Rpb24gdG8gZ2V0IGEgR1JSIEFnZW50
J3MgaW5mb3JtYXRpb24gdXNpbmcgdGhlaXIgSVAgQWRkcmVzcy5dXT48L2RvY3VtZW50YXRpb24+
PHN0YXJ0RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VG
bG93XzA4dHV0Z2g8L291dGdvaW5nPjwvc3RhcnRFdmVudD48c2VydmljZVRhc2sgaWQ9XCJTZXJ2
aWNlVGFza18wMzE4YXJ2XCIgbmFtZT1cIkdSUiBTZWFyY2hcIiByZXNpbGllbnQ6dHlwZT1cImZ1
bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cIjgy
OTMwNzYwLTA1ZTEtNDNmNi1hMGYxLTk4YjA0ZWMyZThkNFwiPntcImlucHV0c1wiOntcImUwNTJj
NGY4LWViM2QtNDVhNS1iMjJiLWRkMTkzNGNmMTRjZVwiOntcImlucHV0X3R5cGVcIjpcInN0YXRp
Y1wiLFwic3RhdGljX2lucHV0XCI6e1wibXVsdGlzZWxlY3RfdmFsdWVcIjpbXSxcInNlbGVjdF92
YWx1ZVwiOlwiMDUxY2NlZDUtYzVhNC00OWZkLTkyMDctY2RmNzA4M2M2NzZkXCJ9fX0sXCJwcmVf
cHJvY2Vzc2luZ19zY3JpcHRcIjpcIiMgU2V0IHRoZSBncnJfc2VhcmNoX3ZhbHVlXFxuaW5wdXRz
Lmdycl9zZWFyY2hfdmFsdWUgPSBhcnRpZmFjdC52YWx1ZVwiLFwicmVzdWx0X25hbWVcIjpcIlwi
LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiIyMgRXhhbXBsZTogR1JSIFNlYXJjaCBieSBJ
UCBQb3N0LVByb2Nlc3NpbmcgU2NyaXB0XFxuXFxuaWYgcmVzdWx0cy5zdWNjZXNzOlxcbiAgIyBM
b29wIGFsbCBmb3VuZCBhZ2VudHNcXG4gIGZvciBhZ2VudCBpbiByZXN1bHRzW1xcXCJhZ2VudHNc
XFwiXTpcXG5cXG4gICAgbm90ZV90ZXh0ID0gXFxcIlxcXCJcXFwiJmx0O2kgc3R5bGU9XFxcImNv
bG9yOiMwMGFmMDhcXFwiJmd0O0dSUiBBZ2VudCBGb3VuZDombHQ7L2kmZ3Q7XFxuICAgICAgICAg
ICAgICAmbHQ7YnImZ3Q7Jmx0O2ImZ3Q7U3lzdGVtIFByb2R1Y3QgTmFtZTombHQ7L2ImZ3Q7IHsw
fVxcbiAgICAgICAgICAgICAgJmx0O2JyJmd0OyZsdDtiJmd0O1N5c3RlbSBVVUlEOiZsdDsvYiZn
dDsgezF9XFxuICAgICAgICAgICAgICAmbHQ7YnImZ3Q7Jmx0O2ImZ3Q7U3lzdGVtIE1hbnVmYWN0
dXJlcjombHQ7L2ImZ3Q7IHsyfVxcbiAgICAgICAgICAgICAgJmx0O2JyJmd0OyZsdDtiJmd0O1Jl
bGVhc2U6Jmx0Oy9iJmd0OyB7M31cXG4gICAgICAgICAgICAgICZsdDticiZndDsmbHQ7YiZndDtN
YWNoaW5lOiZsdDsvYiZndDsgezR9XFxuICAgICAgICAgICAgICAmbHQ7YnImZ3Q7Jmx0O2ImZ3Q7
VmVyc2lvbjombHQ7L2ImZ3Q7IHs1fVxcXCJcXFwiXFxcIi5mb3JtYXQoYWdlbnRbXFxcImhhcmR3
YXJlSW5mb1xcXCJdW1xcXCJzeXN0ZW1Qcm9kdWN0TmFtZVxcXCJdLFxcbiAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYWdlbnRbXFxcImhhcmR3YXJlSW5mb1xcXCJd
W1xcXCJzeXN0ZW1VdWlkXFxcIl0sXFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICBhZ2VudFtcXFwiaGFyZHdhcmVJbmZvXFxcIl1bXFxcInN5c3RlbU1hbnVmYWN0
dXJlclxcXCJdLFxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
YWdlbnRbXFxcIm9zSW5mb1xcXCJdW1xcXCJyZWxlYXNlXFxcIl0sXFxuICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhZ2VudFtcXFwib3NJbmZvXFxcIl1bXFxcIm1h
Y2hpbmVcXFwiXSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
IGFnZW50W1xcXCJvc0luZm9cXFwiXVtcXFwidmVyc2lvblxcXCJdKVxcbiAgaW5jaWRlbnQuYWRk
Tm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZV90ZXh0KSlcXG5cXG5lbHNlOlxcbiAgbm90
ZV90ZXh0ID0gXFxcInswfSBzeXN0ZW0gbm90IGZvdW5kIGluIEdSUlxcXCIuZm9ybWF0KHJlc3Vs
dHMuZ3JyX3NlYXJjaF92YWx1ZSlcXG4gIGluY2lkZW50LmFkZE5vdGUoaGVscGVyLmNyZWF0ZVBs
YWluVGV4dChub3RlX3RleHQpKVxcblwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9u
RWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18wOHR1dGdoPC9pbmNvbWluZz48b3V0Z29p
bmc+U2VxdWVuY2VGbG93XzBxdzF6Mno8L291dGdvaW5nPjwvc2VydmljZVRhc2s+PGVuZEV2ZW50
IGlkPVwiRW5kRXZlbnRfMDJybWZlYVwiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMHF3MXoyejwv
aW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzBxdzF6
MnpcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18wMzE4YXJ2XCIgdGFyZ2V0UmVmPVwiRW5kRXZl
bnRfMDJybWZlYVwiLz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzA4dHV0Z2hcIiBz
b3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJTZXJ2aWNlVGFza18w
MzE4YXJ2XCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIj48
dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNz
b2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgc291cmNlUmVmPVwiU3RhcnRFdmVu
dF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiLz48L3Byb2Nl
c3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5Q
bGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRp
OkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRF
dmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZc
IiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhl
aWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBN
TkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1c
IlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlc
Ij48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwi
MjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwi
QXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdk
aTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+
PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1
NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNl
cnZpY2VUYXNrXzAzMThhcnZcIiBpZD1cIlNlcnZpY2VUYXNrXzAzMThhcnZfZGlcIj48b21nZGM6
Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMzUyXCIgeT1cIjE2NlwiLz48
L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVu
dF8wMnJtZmVhXCIgaWQ9XCJFbmRFdmVudF8wMnJtZmVhX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWln
aHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNjA3XCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5M
YWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEyXCIgd2lkdGg9XCIwXCIgeD1cIjYyNVwiIHk9
XCIyMjhcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQ
TU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBxdzF6MnpcIiBpZD1cIlNlcXVlbmNl
Rmxvd18wcXcxejJ6X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0NTJcIiB4c2k6dHlwZT1cIm9t
Z2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjYwN1wiIHhzaTp0eXBl
PVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3Vu
ZHMgaGVpZ2h0PVwiMTJcIiB3aWR0aD1cIjBcIiB4PVwiNTI5LjVcIiB5PVwiMTg1XCIvPjwvYnBt
bmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVt
ZW50PVwiU2VxdWVuY2VGbG93XzA4dHV0Z2hcIiBpZD1cIlNlcXVlbmNlRmxvd18wOHR1dGdoX2Rp
XCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1c
IjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjM1MlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRc
IiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTJc
IiB3aWR0aD1cIjBcIiB4PVwiMjc1XCIgeT1cIjE4NVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9i
cG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwv
ZGVmaW5pdGlvbnM+IiwgIndvcmtmbG93X2lkIjogImV4YW1wbGVfZ3JyX3NlYXJjaF9ieV9pcCIs
ICJ2ZXJzaW9uIjogMjh9LCAibGFzdF9tb2RpZmllZF90aW1lIjogMTUzOTk0NDUxNTA5MiwgImNy
ZWF0b3JfaWQiOiAicmVzYWRtaW5AZXhhbXBsZS5jb20iLCAiYWN0aW9ucyI6IFtdLCAicHJvZ3Jh
bW1hdGljX25hbWUiOiAiZXhhbXBsZV9ncnJfc2VhcmNoX2J5X2lwIiwgIm5hbWUiOiAiRXhhbXBs
ZTogR1JSIFNlYXJjaCBieSBJUCJ9XSwgImFjdGlvbnMiOiBbeyJsb2dpY190eXBlIjogImFsbCIs
ICJuYW1lIjogIkdSUiBTZWFyY2ggYnkgSVAiLCAidmlld19pdGVtcyI6IFtdLCAidHlwZSI6IDEs
ICJ3b3JrZmxvd3MiOiBbImV4YW1wbGVfZ3JyX3NlYXJjaF9ieV9pcCJdLCAib2JqZWN0X3R5cGUi
OiAiYXJ0aWZhY3QiLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogImE2OTZiMjhi
LWExNjAtNDk3OC04MmE1LWM1YzNlZjVjMjViYyIsICJhdXRvbWF0aW9ucyI6IFtdLCAiZXhwb3J0
X2tleSI6ICJHUlIgU2VhcmNoIGJ5IElQIiwgImNvbmRpdGlvbnMiOiBbeyJ0eXBlIjogbnVsbCwg
ImV2YWx1YXRpb25faWQiOiBudWxsLCAiZmllbGRfbmFtZSI6ICJhcnRpZmFjdC50eXBlIiwgIm1l
dGhvZCI6ICJlcXVhbHMiLCAidmFsdWUiOiAiSVAgQWRkcmVzcyJ9XSwgImlkIjogMTQsICJtZXNz
YWdlX2Rlc3RpbmF0aW9ucyI6IFtdfV0sICJsYXlvdXRzIjogW10sICJleHBvcnRfZm9ybWF0X3Zl
cnNpb24iOiAyLCAiaWQiOiA1LCAiaW5kdXN0cmllcyI6IG51bGwsICJwaGFzZXMiOiBbXSwgImFj
dGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGwsICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3Ii
OiAzMCwgInZlcnNpb24iOiAiMzAuNC4yMzciLCAiYnVpbGRfbnVtYmVyIjogMjM3LCAibWlub3Ii
OiA0fSwgInRpbWVmcmFtZXMiOiBudWxsLCAid29ya3NwYWNlcyI6IFtdLCAiYXV0b21hdGljX3Rh
c2tzIjogW10sICJmdW5jdGlvbnMiOiBbeyJkaXNwbGF5X25hbWUiOiAiR1JSIFNlYXJjaCIsICJk
ZXNjcmlwdGlvbiI6IHsiY29udGVudCI6ICJBIGZ1bmN0aW9uIHRvIHNlYXJjaCBmb3IgR1JSIEFn
ZW50IiwgImZvcm1hdCI6ICJ0ZXh0In0sICJjcmVhdG9yIjogeyJkaXNwbGF5X25hbWUiOiAiUmVz
IEFkbWluIiwgInR5cGUiOiAidXNlciIsICJpZCI6IDEsICJuYW1lIjogInJlc2FkbWluQGV4YW1w
bGUuY29tIn0sICJ2aWV3X2l0ZW1zIjogW3sic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjog
Il9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVs
ZF91dWlkIiwgImNvbnRlbnQiOiAiY2M1MzdkYTAtMzZkYS00MmM1LTlkMzUtNTUxZWE2NjY1MmFl
IiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAi
X19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxk
X3V1aWQiLCAiY29udGVudCI6ICJlMDUyYzRmOC1lYjNkLTQ1YTUtYjIyYi1kZDE5MzRjZjE0Y2Ui
LCAic3RlcF9sYWJlbCI6IG51bGx9XSwgImV4cG9ydF9rZXkiOiAiZm5fZ3JyX3NlYXJjaCIsICJ1
dWlkIjogIjgyOTMwNzYwLTA1ZTEtNDNmNi1hMGYxLTk4YjA0ZWMyZThkNCIsICJsYXN0X21vZGlm
aWVkX2J5IjogeyJkaXNwbGF5X25hbWUiOiAiUmVzIEFkbWluIiwgInR5cGUiOiAidXNlciIsICJp
ZCI6IDEsICJuYW1lIjogInJlc2FkbWluQGV4YW1wbGUuY29tIn0sICJ2ZXJzaW9uIjogMiwgIndv
cmtmbG93cyI6IFt7ImRlc2NyaXB0aW9uIjogbnVsbCwgIm9iamVjdF90eXBlIjogImFydGlmYWN0
IiwgImFjdGlvbnMiOiBbXSwgIm5hbWUiOiAiRXhhbXBsZTogR1JSIFNlYXJjaCBieSBJUCIsICJ3
b3JrZmxvd19pZCI6IDIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX2dycl9zZWFyY2hf
YnlfaXAiLCAidXVpZCI6IG51bGx9XSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1Mzk5NDQ1MDI0
MzcsICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAiZm5fZ3JyX3NlYXJjaCIsICJpZCI6IDEsICJuYW1l
IjogImZuX2dycl9zZWFyY2gifV0sICJub3RpZmljYXRpb25zIjogbnVsbCwgInJlZ3VsYXRvcnMi
OiBudWxsLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJjcmVhdGVfZGF0ZSI6IDE1Mzk5NDQ1NjgxMzUs
ICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhw
b3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiaWQiOiAwLCAi
bmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAidXBkYXRlX2RhdGUi
OiAxNTM5OTQ0NTY4MTM1LCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQw
NDRhYTAiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBu
dWxsLCAiaGlkZGVuIjogZmFsc2V9XSwgInNjcmlwdHMiOiBbXSwgInR5cGVzIjogW10sICJtZXNz
YWdlX2Rlc3RpbmF0aW9ucyI6IFt7InV1aWQiOiAiMGE5MTQxNzEtNzUwMy00MWNlLTk1YjktZWRm
MTE2NDkxNDI4IiwgImV4cG9ydF9rZXkiOiAiZm5fZ3JyX3NlYXJjaCIsICJuYW1lIjogImZuX2dy
cl9zZWFyY2giLCAiZGVzdGluYXRpb25fdHlwZSI6IDAsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJm
bl9ncnJfc2VhcmNoIiwgImV4cGVjdF9hY2siOiB0cnVlLCAidXNlcnMiOiBbImludGVncmF0aW9u
c0BleGFtcGxlLmNvbSJdfV0sICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAicm9sZXMi
OiBbXSwgImZpZWxkcyI6IFt7Im9wZXJhdGlvbnMiOiBbXSwgInJlYWRfb25seSI6IHRydWUsICJu
YW1lIjogImluY190cmFpbmluZyIsICJ0ZW1wbGF0ZXMiOiBbXSwgInR5cGVfaWQiOiAwLCAiY2hv
c2VuIjogZmFsc2UsICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2Vy
dmVyIjogZmFsc2UsICJleHBvcnRfa2V5IjogImluY2lkZW50L2luY190cmFpbmluZyIsICJ0b29s
dGlwIjogIldoZXRoZXIgdGhlIGluY2lkZW50IGlzIGEgc2ltdWxhdGlvbiBvciBhIHJlZ3VsYXIg
aW5jaWRlbnQuICBUaGlzIGZpZWxkIGlzIHJlYWQtb25seS4iLCAicmljaF90ZXh0IjogZmFsc2Us
ICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInByZWZpeCI6IG51bGwsICJpbnRlcm5hbCI6IGZhbHNl
LCAidmFsdWVzIjogW10sICJibGFua19vcHRpb24iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAiYm9v
bGVhbiIsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJp
ZCI6IDUxLCAidXVpZCI6ICJjM2YwZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMzMDhjY2EifSwg
eyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwg
InRleHQiOiAiZ3JyX3NlYXJjaF92YWx1ZSIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZp
eCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogOTEsICJyZWFkX29ubHkiOiBmYWxz
ZSwgInV1aWQiOiAiY2M1MzdkYTAtMzZkYS00MmM1LTlkMzUtNTUxZWE2NjY1MmFlIiwgImNob3Nl
biI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiIiwgImludGVybmFs
IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tl
eSI6ICJfX2Z1bmN0aW9uL2dycl9zZWFyY2hfdmFsdWUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBm
YWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjogImdycl9zZWFyY2hfdmFsdWUiLCAiZGVm
YXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAidmFs
dWVzIjogW119LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9w
ZXJtcyI6IHt9LCAidGV4dCI6ICJncnJfc2VhcmNoX3R5cGUiLCAiYmxhbmtfb3B0aW9uIjogZmFs
c2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDkyLCAicmVhZF9v
bmx5IjogZmFsc2UsICJ1dWlkIjogImUwNTJjNGY4LWViM2QtNDVhNS1iMjJiLWRkMTkzNGNmMTRj
ZSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAic2VsZWN0IiwgInRvb2x0aXAiOiAi
IiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtd
LCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2dycl9zZWFyY2hfdHlwZSIsICJoaWRlX25vdGlm
aWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAiZ3JyX3NlYXJjaF90
eXBlIiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVzIjogW3sidXVp
ZCI6ICIwNTFjY2VkNS1jNWE0LTQ5ZmQtOTIwNy1jZGY3MDgzYzY3NmQiLCAiZGVmYXVsdCI6IHRy
dWUsICJlbmFibGVkIjogdHJ1ZSwgInZhbHVlIjogMTAwLCAibGFiZWwiOiAiaXAiLCAiaGlkZGVu
IjogZmFsc2UsICJwcm9wZXJ0aWVzIjogbnVsbH0sIHsidXVpZCI6ICJkMWJkNjU1Yi0zM2I2LTRk
ZGQtODAwMi03OWU2MjQzZTg4MGYiLCAiZGVmYXVsdCI6IGZhbHNlLCAiZW5hYmxlZCI6IHRydWUs
ICJ2YWx1ZSI6IDEwMSwgImxhYmVsIjogInVzZXIiLCAiaGlkZGVuIjogZmFsc2UsICJwcm9wZXJ0
aWVzIjogbnVsbH0sIHsidXVpZCI6ICI5YzRiMzQzNC02YzBiLTQwMWYtYTdmZi02MmFmZDdlYzEw
NjMiLCAiZGVmYXVsdCI6IGZhbHNlLCAiZW5hYmxlZCI6IHRydWUsICJ2YWx1ZSI6IDEwMiwgImxh
YmVsIjogImhvc3QiLCAiaGlkZGVuIjogZmFsc2UsICJwcm9wZXJ0aWVzIjogbnVsbH1dfV0sICJv
dmVycmlkZXMiOiBbXSwgImV4cG9ydF9kYXRlIjogMTUzOTk0NDUzMjAyOX0=
"""
    )