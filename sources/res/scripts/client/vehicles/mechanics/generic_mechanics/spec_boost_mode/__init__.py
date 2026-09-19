from __future__ import absolute_import
from vehicles.mechanics.generic_mechanics.spec_boost_mode.mechanic_interfaces import ISpecBoostModeMechanicParams, ISpecBoostModeMechanicState
from vehicles.mechanics.generic_mechanics.spec_boost_mode.mechanic_models import SpecBoostModeMechanicParams, SpecBoostModeMechanicState
__all__ = (b'ISpecBoostModeMechanicParams', b'ISpecBoostModeMechanicState', b'SpecBoostModeMechanicParams', b'SpecBoostModeMechanicState', b'DEFAULT_SPEC_BOOST_MODE_PARAMS', b'DEFAULT_SPEC_BOOST_MODE_STATE')
DEFAULT_SPEC_BOOST_MODE_PARAMS = SpecBoostModeMechanicParams(None)
DEFAULT_SPEC_BOOST_MODE_STATE = SpecBoostModeMechanicState(0, 0.0, -1.0)
