﻿from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.Facility.Exceptions.UnionTypeError import UnionTypeError


class UnionTypeField(OTLField):
    def __str__(self):
        return OTLField.__str__(self)

    attributen = None
    waarde_shortcut_applicable = True

    @staticmethod
    def validate(value, attribuut):
        if value is None:
            return True
        if isinstance(value, attribuut.field.waardeObject):
            return True
        valueDict = vars(attribuut.field.waardeObject())
        for attr in valueDict.values():
            try:
                validate_result = attr.field.validate(value, attr)
                if validate_result:
                    return True
            except:
                raise UnionTypeError(
                    f'Invalid value for {attribuut.naam}, check attr_type_info to see what kind of values are valid.')
        raise UnionTypeError(f'Invalid value for {attribuut.naam}, check attr_type_info to see what kind of values are valid.')


