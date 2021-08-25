# -*- coding: utf-8 -*-
"""Handle grant URLs.

Copyright (C) 2020 Gitcoin Core

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
from django_distill import distill_path, distill_re_path

from django.conf import settings
from django.conf.urls import include, url
from django.urls import path, re_path

from quadraticlands.helpers import vote
from quadraticlands.router import router
from quadraticlands.views import (
    base, base_auth, dashboard_index, handler400, handler403, handler404, handler500, index, mission_diplomacy,
    mission_diplomacy_room, mission_index, mission_lore, mission_postcard, mission_postcard_svg, mission_schwag,
    workstream_base, workstream_index,
)


def get_index():
    return None


app_name = 'quadraticlands'

urlpatterns = [
    # distill
    distill_path('', index, distill_func=get_index, name='quadraticlands', distill_file='index.html'),
    distill_re_path(r'^dashboard/?$', dashboard_index, name='dashboard', distill_func=get_index, distill_file='dashboard/index.html'),
    distill_re_path(r'^vote/?$', vote, name='vote_json'),
    distill_re_path(r'^(?P<base>about|faq)/?$', base, name='quadraticlands_base', distill_func=get_index, distill_file='dashboard/about.html'),
    distill_re_path(r'^(?P<base>about|faq)/?$', base, name='quadraticlands_base', distill_func=get_index, distill_file='dashboard/about.html'),


    # distill workstreams
    distill_re_path(r'^workstream/?$', workstream_index, name='workstream', distill_func=get_index, distill_file='workstream/index.html'),
    distill_re_path(r'^workstream/(?P<stream_name>publicgoods|sybil|decentralization|labs)/?$', workstream_base, name='workstream', distill_func=get_index, distill_file='workstream/index.html'),

    # distill mission
    distill_re_path(r'^mission/?$', mission_index, name='mission', distill_func=get_index, distill_file='quadraticlands/mission/index.html'),

    re_path(r'^mission/postcard$', mission_postcard, name='mission_postcard'),
    re_path(r'^mission/postcard/svg$', mission_postcard_svg, name='mission_postcard_svg'),
    re_path(r'^mission/ql-lore$', mission_lore, name='mission_lore'),
    re_path(r'^mission/schwag$', mission_schwag, name='mission_schwag'),

    #richard test to build new interface stuff
    distill_path(r'^mission/diplomacy/<str:uuid>/<str:name>/', mission_diplomacy_room, name='mission_diplomacy_room', distill_func=get_index, distill_file='quadraticlands/mission/diplomacy/index.html')
    distill_path(r'^mission/diplomacy/<str:uuid>/<str:name>', mission_diplomacy_room, name='mission_diplomacy_room', distill_func=get_index, distill_file='quadraticlands/mission/diplomacy/index.html')
    distill_re_path(r'^mission/diplomacy/?', mission_diplomacy, name='mission_diplomacy', distill_func=get_index, distill_file='quadraticlands/mission/diplomacy/index.html'),



    url(r'^api/v1/', include(router.urls)),
]


# if settings.DEBUG:
urlpatterns += [
    distill_re_path(r'^400/?$', handler400, name='400', distill_func=get_index),
    distill_re_path(r'^403/?$', handler403, name='403', distill_func=get_index),
    distill_re_path(r'^404/?$', handler404, name='404', distill_func=get_index),
    distill_re_path(r'^500/?$', handler500, name='500', distill_func=get_index),
]

handler403 = 'quadraticlands.views.handler403'
handler404 = 'quadraticlands.views.handler404'
handler500 = 'quadraticlands.views.handler500'
handler400 = 'quadraticlands.views.handler400'
