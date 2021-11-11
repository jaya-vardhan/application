class UserRouter:
    route_app_labels={'User'}

    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user_db'
        return None

    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user_db'
        return None

    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label in self.route_app_labels:
            return db == 'user_db'
        return None

class ProductsRouter:
    route_app_labels={'Products'}

    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products_db'
        return None

    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products_db'
        return None

    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label in self.route_app_labels:
            return db == 'products_db'
        return None