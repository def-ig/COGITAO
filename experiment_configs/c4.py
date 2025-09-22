import copy
import itertools

cp_path = "before_arc_datasets/c4"

cp_base_config = {
    "min_n_shapes_per_grid": 2,
    "max_n_shapes_per_grid": 2,
    "n_examples": 1,
    "min_grid_size": 20,
    "max_grid_size": 20,
    "allowed_combinations": None,
    "allowed_transformations": None,
    "min_transformation_depth": None,
    "max_transformation_depth": None,
    "shape_compulsory_conditionals": [
        "is_shape_less_than_6_rows",
        "is_shape_less_than_6_cols",
        "is_shape_fully_connected",
    ],
    "saving_path": None,
}

def make_config(combos, setting, exp_number, split, min_size=20, max_size=20):
    cfg = copy.deepcopy(cp_base_config)
    cfg["allowed_combinations"] = combos
    cfg["saving_path"] = f"{cp_path}/exp_setting_{setting}/experiment_{exp_number}/{split}.json"
    cfg["min_grid_size"] = min_size
    cfg["max_grid_size"] = max_size
    return cfg

c4_configs = []

base_transforms = [
    "mirror_horizontal",   
    "crop_top_side",       
    "double_right",        
]

extra_transforms = [
    "translate_up",            
    "rot90",                   
    "mirror_vertical",         
    "pad_top",                 
    "translate_right",         
    "pad_right",               
    "fill_holes_same_color",   
    "fill_holes_different_color", 
    "change_shape_color",      
    "empty_inside_pixels",
    "double_down", 
    "extend_contours_same_color",     
]

def all_single_and_double(transforms):
    singles = [[t] for t in transforms]
    doubles = [list(pair) for pair in itertools.combinations(transforms, 2)]
    return singles + doubles

test_combo = [["double_right", "mirror_horizontal"]]

# number of transformations for each experiment
exp_sizes = [3, 6, 9, 12, 15]

for exp_num, size in enumerate(exp_sizes, start=1):
    pool = base_transforms + extra_transforms[: size - len(base_transforms)]
    train_combos = all_single_and_double(pool)

    c4_configs.append(
        make_config(train_combos, setting=4, exp_number=exp_num, split="train")
    )
    c4_configs.append(
        make_config(test_combo, setting=4, exp_number=exp_num, split="test")
    )
