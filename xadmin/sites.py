import sys


reload(sys)
sys.setdefaultencoding("utf-8")

class AlreadyRegistered(Exception):
    pass


class NotRegistered(Exception):
    pass


class MergeAdminMetaclass(type):
    def __new__(cls, name, bases, attrs):
        return type.__new__(cls, str(name), bases, attrs)

class AdminSite(object):

    def __init__(self, name='xadmin'):
        self.name = name
        self.app_name = 'xadmin'

        self._registry = {}  # model_class class -> admin_class class
        self._registry_avs = {}  # admin_view_class class -> admin_class class
        self._registry_settings = {}  # settings name -> admin_class class
        self._registry_views = []
            # url instance contains (path, admin_view class, name)
        self._registry_modelviews = []
            # url instance contains (path, admin_view class, name)
        self._registry_plugins = {}  # view_class class -> plugin_class class

        self._admin_view_cache = {}

        self.check_dependencies()

        self.model_admins_order = 0

    # 复制当前 AdminSite 实例的信息
    def copy_registry(self):
        import copy
        return {
            'models': copy.copy(self._registry),
            'avs': copy.copy(self._registry_avs),
            'views': copy.copy(self._registry_views),
            'settings': copy.copy(self._registry_settings),
            'modelviews': copy.copy(self._registry_modelviews),
            'plugins': copy.copy(self._registry_plugins),
        }


    def restore_registry(self, data):
        self._registry = data['models']
        self._registry_avs = data['avs']
        self._registry_views = data['views']
        self._registry_settings = data['settings']
        self._registry_modelviews = data['modelviews']
        self._registry_plugins = data['plugins']
