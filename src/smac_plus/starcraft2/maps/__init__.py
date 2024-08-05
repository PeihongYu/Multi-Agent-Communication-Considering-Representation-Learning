from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from smac.env.starcraft2.maps import smac_maps


map_param_registry = {
    # "3s_vs_5z": {
    #     "n_agents": 3,
    #     "n_enemies": 5,
    #     "limit": 250,
    #     "a_race": "P",
    #     "b_race": "P",
    #     "unit_type_bits": 0,
    #     "map_type": "stalkers",
    # },
    "1o_10b_vs_1r": {
        "n_agents": 11,
        "n_enemies": 1,
        "limit": 50,
        "a_race": "Z",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "overload_bane"
    },
    "1o_2z_vs_2z": {
        "n_agents": 3,
        "n_enemies": 2,
        "limit": 80,
        "a_race": "Z",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "overload_zergling"
    },
    "1o_2r_vs_4r": {
        "n_agents": 3,
        "n_enemies": 4,
        "limit": 50,
        "a_race": "Z",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "overload_roach"
    },
    "1o_2r_vs_2r": {
        "n_agents": 3,
        "n_enemies": 2,
        "limit": 50,
        "a_race": "Z",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "overload_roach"
    },
    "3m_vs_2m": {
        "n_agents": 3,
        "n_enemies": 2,
        "limit": 50,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "3m_vs_9z_1q": {
        "n_agents": 3,
        "n_enemies": 10,
        "limit": 200,
        "a_race": "T",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "zerg_queen",
    },
    "11m": {
        "n_agents": 11,
        "n_enemies": 11,
        "limit": 120,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "11m_random": {
        "n_agents": 11,
        "n_enemies": 11,
        "limit": 120,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "MM_vs_q": {
        "n_agents": 3,
        "n_enemies": 1,
        "limit": 80,
        "a_race": "T",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "MM_queen",
    },
    "GMMM": {
        "n_agents": 13,
        "n_enemies": 13,
        "limit": 180,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 4,
        "map_type": "GMMM",
    },
    "5z_vs_1ul": {
        "n_agents": 5,
        "n_enemies": 1,
        "limit": 150,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 0,
        "map_type": "stalkers",
    },
    "3m_vs_1v": {
        "n_agents": 3,
        "n_enemies": 1,
        "limit": 100,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
    "2s_vs_1sc_random_v2": {
        "n_agents": 2,
        "n_enemies": 1,
        "limit": 200,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 0,
        "map_type": "stalkers",
    },
    "bane_vs_hM": {
        "n_agents": 3,
        "n_enemies": 2,
        "limit": 30,
        "a_race": "Z",
        "b_race": "T",
        "unit_type_bits": 2,
        "map_type": "bZ_hM"
    },
    "bZ_vs_hM": {
        "n_agents": 3,
        "n_enemies": 2,
        "limit": 30,
        "a_race": "Z",
        "b_race": "T",
        "unit_type_bits": 2,
        "map_type": "bZ_hM"
    },
    "zM_vs_z": {
        "n_agents": 4,
        "n_enemies": 3,
        "limit": 100,
        "a_race": "T",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "zMz"
    },
}


smac_maps.map_param_registry.update(map_param_registry)

def get_map_params(map_name):
    map_param_registry = smac_maps.get_smac_map_registry()
    return map_param_registry[map_name]


for name in map_param_registry.keys():
    globals()[name] = type(name, (smac_maps.SMACMap,), dict(filename=name))
