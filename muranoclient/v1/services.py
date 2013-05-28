#    Copyright (c) 2013 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from muranoclient.common import base


class ActiveDirectory(base.Resource):
    def __repr__(self):
        return '<ActiveDirectory %s>' % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class ActiveDirectoryManager(base.Manager):
    resource_class = ActiveDirectory

    def list(self, environment_id, session_id=None):
        if session_id:
            headers = {'X-Configuration-Session': session_id}
        else:
            headers = {}

        return self._list('environments/{id}/activeDirectories'.
                          format(id=environment_id),
                          'activeDirectories',
                          headers=headers)

    def create(self, environment_id, session_id, active_directory):
        headers = {'X-Configuration-Session': session_id}

        return self._create('environments/{id}/activeDirectories'.
                            format(id=environment_id),
                            active_directory,
                            headers=headers)

    def delete(self, environment_id, session_id, service_id):
        headers = {'X-Configuration-Session': session_id}
        path = 'environments/{id}/activeDirectories/{active_directory_id}'
        path = path.format(id=environment_id, active_directory_id=service_id)

        return self._delete(path, headers=headers)


class WebServer(base.Resource):
    def __repr__(self):
        return '<WebServer %s>' % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class WebServerManager(base.Manager):
    resource_class = WebServer

    def list(self, environment_id, session_id=None):
        if session_id:
            headers = {'X-Configuration-Session': session_id}
        else:
            headers = {}

        return self._list('environments/{id}/webServers'.
                          format(id=environment_id),
                          'webServers',
                          headers=headers)

    def create(self, environment_id, session_id, web_server):
        headers = {'X-Configuration-Session': session_id}

        return self._create('environments/{id}/webServers'.
                            format(id=environment_id),
                            web_server,
                            headers=headers)

    def delete(self, environment_id, session_id, service_id):
        headers = {'X-Configuration-Session': session_id}

        return self._delete('environments/{id}/webServers/{web_server_id}'
                            .format(id=environment_id,
                                    web_server_id=service_id),
                            headers=headers)


class AspNetApp(base.Resource):
    def __repr__(self):
        return '<AspNetApp %s>' % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class AspNetAppManager(base.Manager):
    resource_class = AspNetApp

    def list(self, environment_id, session_id=None):
        if session_id:
            headers = {'X-Configuration-Session': session_id}
        else:
            headers = {}

        return self._list('environments/{id}/aspNetApps'.
                          format(id=environment_id),
                          'aspNetApps',
                          headers=headers)

    def create(self, environment_id, session_id, app):
        headers = {'X-Configuration-Session': session_id}

        return self._create('environments/{id}/aspNetApps'.
                            format(id=environment_id),
                            app,
                            headers=headers)

    def delete(self, environment_id, session_id, service_id):
        headers = {'X-Configuration-Session': session_id}

        return self._delete('environments/{id}/aspNetApps/{app_id}'
                            .format(id=environment_id,
                                    app_id=service_id),
                            headers=headers)


class WebServerFarm(base.Resource):
    def __repr__(self):
        return '<WebServerFarm %s>' % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class WebServerFarmManager(base.Manager):
    resource_class = WebServerFarm

    def list(self, environment_id, session_id=None):
        if session_id:
            headers = {'X-Configuration-Session': session_id}
        else:
            headers = {}

        return self._list('environments/{id}/webServerFarms'.
                          format(id=environment_id),
                          'webServerFarms',
                          headers=headers)

    def create(self, environment_id, session_id, web_server_farm):
        headers = {'X-Configuration-Session': session_id}

        return self._create('environments/{id}/webServerFarms'.
                            format(id=environment_id),
                            web_server_farm,
                            headers=headers)

    def delete(self, environment_id, session_id, service_id):
        headers = {'X-Configuration-Session': session_id}

        return self._delete('environments/{id}/webServerFarms'
                            '/{web_server_farm_id}'
                            .format(id=environment_id,
                                    web_server_farm_id=service_id),
                            headers=headers)


class AspNetAppFarm(base.Resource):
    def __repr__(self):
        return '<AspNetAppFarm %s>' % self._info

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class AspNetAppFarmManager(base.Manager):
    resource_class = AspNetAppFarm

    def list(self, environment_id, session_id=None):
        if session_id:
            headers = {'X-Configuration-Session': session_id}
        else:
            headers = {}

        return self._list('environments/{id}/aspNetAppFarms'.
                          format(id=environment_id),
                          'aspNetAppFarms',
                          headers=headers)

    def create(self, environment_id, session_id, app_farm):
        headers = {'X-Configuration-Session': session_id}

        return self._create('environments/{id}/aspNetAppFarms'.
                            format(id=environment_id),
                            app_farm,
                            headers=headers)

    def delete(self, environment_id, session_id, service_id):
        headers = {'X-Configuration-Session': session_id}

        return self._delete('environments/{id}/aspNetAppFarms/{app_id}'
                            .format(id=environment_id,
                                    app_id=service_id),
                            headers=headers)
