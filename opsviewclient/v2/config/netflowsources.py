#!/usr/bin/env python
# coding: utf-8

from six.moves.urllib import parse

try:
    import simplejson as json
except ImportError:
    import json

from opsviewclient import base


class NetflowSource(base.Resource):

    def __repr__(self):
        return '<NetflowSource: %s>' % self.name

    def delete(self):
        return self.manager.delete(self)


class NetflowSourceManager(base.Manager):

    resource_class = NetflowSource

    def get(self, source):
        return self._get('/config/netflowsource/%s' % base.get_id(source))

    def delete(self, source):
        return self._delete('/config/netflowsource/%s' % base.get_id(source))

    def list(self, rows='all', page=None, cols=None, order=None, search=None,
             in_use=None, kwds=None):

        qparams = {}

        if rows:
            qparams['rows'] = str(rows)
        if page:
            qparams['page'] = int(page)
        if cols:
            qparams['cols'] = str(cols)
        if order:
            qparams['order'] = str(order)
        if search:
            qparams['json_filter'] = json.dumps(search)
        if in_use is not None:
            qparams['in_use'] = 1 if in_use else 0

        if kwds:
            qparams.update(kwds)

        qparams = sorted(qparams.items(), key=lambda x: x[0])
        qstring = "?%s" % parse.urlencode(qparams) if qparams else ""

        return self._list('/config/netflowsource%s' % qstring)
