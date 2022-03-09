# global
from typing import Union

# local
import ivy
from ivy.framework_handler import current_framework as _cur_framework

Finfo = None
Iinfo = None


# Dtype Info #
# -----------#

# noinspection PyShadowingBuiltins
def iinfo(type: Union[ivy.Dtype, str, ivy.Array, ivy.NativeArray])\
        -> Iinfo:
    """
    Machine limits for integer data types.

    :param type: the kind of integer data-type about which to get information.
    :return: iinfo object.
        a class with that encapsules the following attributes:
        - **bits**: *int*
          number of bits occupied by the type.
        - **max**: *int*
          largest representable number.
        - **min**: *int*
          smallest representable number.
    """
    return _cur_framework(None).iinfo(type)


# noinspection PyShadowingBuiltins
def finfo(type: Union[ivy.Dtype, str, ivy.Array, ivy.NativeArray])\
        -> Finfo:
    """
    Machine limits for floating-point data types.

    :param type: the kind of floating-point data-type about which to get information.
    :return: finfo object.
        an object having the followng attributes:
        - **bits**: *int*
          number of bits occupied by the floating-point data type.
        - **eps**: *float*
          difference between 1.0 and the next smallest representable floating-point number larger than 1.0 according to the IEEE-754 standard.
        - **max**: *float*
          largest representable number.
        - **min**: *float*
          smallest representable number.
        - **smallest_normal**: *float*
          smallest positive floating-point number with full precision.
    """
    return _cur_framework(None).finfo(type)


def can_cast(from_: Union[ivy.Dtype, str, ivy.Array, ivy.NativeArray], to: Union[ivy.Dtype, str])\
        -> bool:
    """
        Determines if one data type can be cast to another data type.

        :param from_: input data type or array from which to cast.
        :param to: desired data type to be casted to.
        :return: boolean object.
            If the data type can be casted to another data type
        """
    return _cur_framework(None).finfo(from_, to)


def can_cast(from_: Union[ivy.Dtype, str, ivy.Array, ivy.NativeArray], to: Union[ivy.Dtype, str])\
        -> bool:
    """
        Determines if one data type can be cast to another data type.

        :param from_: input data type or array from which to cast.
        :param to: desired data type to be casted to.
        :return: boolean object.
            If the data type can be casted to another data type
        """
    return _cur_framework(None).finfo(from_, to)