# Systematic Generalization 
import copy

# Fixed Parameters: 

se_path = "cogitao_datasets/sample_efficiency"

se_base_config = {
    "min_n_shapes_per_grid": 2,
    "max_n_shapes_per_grid": 2,
    "n_examples": 1,
    "min_grid_size": 15,
    "max_grid_size": 15,
    "allowed_combinations": None,
    "allowed_transformations": None,
    "min_transformation_depth": None,
    "max_transformation_depth": None,
    "shape_compulsory_conditionals": ["is_shape_less_than_6_rows", 
                                      "is_shape_less_than_6_cols", 
                                      "is_shape_fully_connected"],
    "saving_path": None,
}

def make_config(combos, setting, exp_number, split, min_size = 15, max_size = 15):
    config = copy.deepcopy(se_base_config)
    config["allowed_combinations"] = combos
    config["saving_path"] = f"{se_path}/exp_setting_{setting}/experiment_{exp_number}/{split}.json"
    return config

sample_efficiency_configs = []

sample_efficiency_configs.append(make_config(
    [["translate_up"]], 1, 1, "train"))

sample_efficiency_configs.append(make_config(
    [["rot90"]], 1, 2, "train"))

sample_efficiency_configs.append(make_config(
    [["mirror_horizontal"]], 1, 3, "train"))

sample_efficiency_configs.append(make_config(
    [["extend_contours_different_color"]], 1, 4, "train"))

sample_efficiency_configs.append(make_config(
    [["empty_inside_pixels"]], 1, 5, "train"))