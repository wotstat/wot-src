class AutoProperty(object):

    def __init__(self, fieldName=None):
        self.fieldName = fieldName
        return

    def __get__(self, instance, owner=None):
        if instance is not None:
            return getattr(instance, self.fieldName, None)
        else:
            return self

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)
        return


class TypedProperty(AutoProperty):

    def __init__(self, allowedType, fieldName=None):
        AutoProperty.__init__(self, fieldName)
        self.allowedType = allowedType
        return

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)
        return


class LinkDescriptor(AutoProperty):

    def __init__(self, fieldName=None):
        AutoProperty.__init__(self, fieldName)
        return

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)
        return

    def __call__(self, *args, **kwargs):
        return


class AutoPropertyInitMetaclass(type):

    def __new__(mcs, name, bases, attributes):
        for attributeName, attribute in attributes.iteritems():
            if isinstance(attribute, AutoProperty) and attribute.fieldName is None:
                attribute.fieldName = b'_%s__%s' % (name, attributeName)

        return super(AutoPropertyInitMetaclass, mcs).__new__(mcs, name, bases, attributes)
