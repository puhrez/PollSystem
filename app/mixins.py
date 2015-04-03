class ModelMixin(object):
    """
    Mixin class for model's shared functions
    """
    def as_dict(self):
        """
        returns the object as a dictionary
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
