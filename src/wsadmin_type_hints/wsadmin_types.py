"""
Module used internally by `wsadmin-type-hints` to define appropriate return types for some `wsadmin` methods.
"""
class _OpaqueDigestObject(object):
    """
    Opaque "digest" object returned by a call to the `AdminConfig.extract()` method.
    """
    pass