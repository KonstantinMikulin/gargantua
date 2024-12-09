from bot.dialogs.getters.weight_getters import (
    weight_getter,
    all_weights_getter,
    last_weight_getter,
    weight_delta_getter
)
from bot.dialogs.getters.measure_getters import (
    measurments_getter,
    all_chest_getter,
    last_chest_getter,
    last_waist_getter,
    last_hips_getter,
    measurements_delta_getter
)

__all__ = [
    "weight_getter",
    "all_chest_getter",
    "all_weights_getter",
    "measurments_getter",
    "last_weight_getter",
    "last_chest_getter",
    "last_waist_getter",
    "last_hips_getter",
    "weight_delta_getter",
    "measurements_delta_getter",
]
