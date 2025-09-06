import copy

# Default parameters common to all experiments
cp_path = "before_arc_datasets/compositionality_gridsize"

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
    "shape_compulsory_conditionals": ["is_shape_less_than_6_rows", 
                                      "is_shape_less_than_6_cols", 
                                      "is_shape_fully_connected"],
    "saving_path": None,
}

def make_config(combos, setting, exp_number, split, min_size = 15, max_size = 15):
    config = copy.deepcopy(cp_base_config)
    config["allowed_combinations"] = combos
    config["saving_path"] = f"{cp_path}/exp_setting_{setting}/experiment_{exp_number}/grid_size_{max_size}/{split}.json"
    config["min_grid_size"] = min_size
    config["max_grid_size"] = max_size
    return config

### C1

c11_train = [["translate_up"], ["rot90"], ["mirror_horizontal"],
        ["translate_up", "translate_up"], ["rot90", "rot90"],
        ["mirror_horizontal", "mirror_horizontal"],
        ["translate_up", "mirror_horizontal"],
        ["rot90", "mirror_horizontal"], 
        ["rot90", "translate_up"],
        ["mirror_horizontal", "rot90"]]
c11_test = [["translate_up", "rot90"]]

c12_train = [["pad_right"], ["fill_holes_different_color"], ["change_shape_color"],
        ["pad_right", "pad_right"],
        ["fill_holes_different_color", "fill_holes_different_color"],
        ["change_shape_color", "change_shape_color"],
        ["pad_right", "fill_holes_different_color"],
        ["fill_holes_different_color", "change_shape_color"],
        ["change_shape_color", "fill_holes_different_color" ],
        ["change_shape_color", "pad_right"]]

c12_test = [["pad_right", "change_shape_color"]]

c13_train = [["rot90"], ["pad_top"], ["crop_bottom_side"],
        ["rot90", "rot90"],
        ["pad_top", "pad_top"],
        ["crop_bottom_side", "crop_bottom_side"],
        ["rot90", "pad_top"],
        ["pad_top", "crop_bottom_side"],
        ["crop_bottom_side", "rot90"]]

c13_test = [["rot90", "crop_bottom_side"]]

c14_train = [["double_right"], ["crop_contours"], ["change_shape_color"], 
            ["double_right", "double_right"],
            ["crop_contours", "crop_contours"],
            ["change_shape_color", "change_shape_color"],
            ["double_right", "change_shape_color"],
            ["crop_contours", "change_shape_color"],
            ["change_shape_color", "double_right"]]

c14_test = [["double_right", "crop_contours"]]

c15_train = [["extend_contours_same_color"], ["pad_left"], ["mirror_vertical"],
        ["extend_contours_same_color", "extend_contours_same_color"],
        ["pad_left", "pad_left"],
        ["mirror_vertical", "mirror_vertical"],
        ["mirror_vertical", "pad_left"],
        ["extend_contours_same_color", "pad_left"],
        ["extend_contours_same_color", "mirror_vertical"]]

c15_test = [["pad_left", "extend_contours_same_color"]]

###### C3

c31_train = [["translate_up"], ["mirror_horizontal"], ["rot90"],
     ["translate_up", "translate_up"], ["mirror_horizontal", "mirror_horizontal"], ["rot90", "rot90"],
     ["translate_up", "mirror_horizontal"], ["translate_up", "rot90"],
     ["mirror_horizontal", "rot90"]]

c31_test = [["translate_up", "translate_up", "translate_up"],
     ["translate_up", "translate_up", "mirror_horizontal"],
     ["translate_up", "translate_up", "rot90"],
     ["translate_up", "mirror_horizontal", "mirror_horizontal"],
     ["translate_up", "mirror_horizontal", "rot90"],
     ["translate_up", "rot90", "rot90"],
     ["mirror_horizontal", "mirror_horizontal", "mirror_horizontal"],
     ["mirror_horizontal", "mirror_horizontal", "rot90"],
     ["mirror_horizontal", "rot90", "rot90"],
     ["rot90", "rot90", "rot90"],
     ["translate_up", "mirror_horizontal", "translate_up"],
     ["translate_up", "rot90", "translate_up"],
     ["mirror_horizontal", "rot90", "translate_up"],
     ["mirror_horizontal", "translate_up", "rot90"],
     ["rot90", "translate_up", "mirror_horizontal"],
     ["rot90", "mirror_horizontal", "translate_up"]]

c32_train = [["pad_right"], ["fill_holes_different_color"], ["change_shape_color"],
      ["pad_right", "pad_right"], ["fill_holes_different_color", "fill_holes_different_color"], ["change_shape_color", "change_shape_color"],
      ["pad_right", "fill_holes_different_color"], ["pad_right", "change_shape_color"],
      ["fill_holes_different_color", "change_shape_color"]]

c32_test = [["pad_right", "pad_right", "pad_right"],
      ["pad_right", "pad_right", "fill_holes_different_color"],
      ["pad_right", "pad_right", "change_shape_color"],
      ["pad_right", "fill_holes_different_color", "fill_holes_different_color"],
      ["pad_right", "fill_holes_different_color", "change_shape_color"],
      ["pad_right", "change_shape_color", "change_shape_color"],
      ["fill_holes_different_color", "fill_holes_different_color", "fill_holes_different_color"],
      ["fill_holes_different_color", "fill_holes_different_color", "change_shape_color"],
      ["fill_holes_different_color", "change_shape_color", "change_shape_color"],
      ["change_shape_color", "change_shape_color", "change_shape_color"],
      ["pad_right", "fill_holes_different_color", "pad_right"],
      ["pad_right", "change_shape_color", "pad_right"],
      ["fill_holes_different_color", "change_shape_color", "pad_right"],
      ["fill_holes_different_color", "pad_right", "change_shape_color"],
      ["change_shape_color", "pad_right", "fill_holes_different_color"],
      ["change_shape_color", "fill_holes_different_color", "pad_right"]]

c33_train = [["rot90"], ["pad_top"], ["crop_bottom_side"],
      ["rot90", "rot90"], ["pad_top", "pad_top"], ["crop_bottom_side", "crop_bottom_side"],
      ["rot90", "pad_top"], ["rot90", "crop_bottom_side"],
      ["pad_top", "crop_bottom_side"]]

c33_test = [["rot90", "rot90", "rot90"],
      ["rot90", "rot90", "pad_top"],
      ["rot90", "rot90", "crop_bottom_side"],
      ["rot90", "pad_top", "pad_top"],
      ["rot90", "pad_top", "crop_bottom_side"],
      ["rot90", "crop_bottom_side", "crop_bottom_side"],
      ["pad_top", "pad_top", "pad_top"],
      ["pad_top", "pad_top", "crop_bottom_side"],
      ["pad_top", "crop_bottom_side", "crop_bottom_side"],
      ["crop_bottom_side", "crop_bottom_side", "crop_bottom_side"],
      ["rot90", "pad_top", "rot90"],
      ["rot90", "crop_bottom_side", "rot90"],
      ["pad_top", "crop_bottom_side", "rot90"],
      ["pad_top", "rot90", "crop_bottom_side"],
      ["crop_bottom_side", "rot90", "pad_top"],
      ["crop_bottom_side", "pad_top", "rot90"]]

c34_train = [["double_right"], ["crop_contours"], ["change_shape_color"],
             ["double_right", "double_right"], ["crop_contours", "crop_contours"], ["change_shape_color", "change_shape_color"],
             ["double_right", "crop_contours"], ["double_right", "change_shape_color"],
             ["crop_contours", "change_shape_color"]]

c34_test = [["double_right", "double_right", "double_right"],
             ["double_right", "double_right", "crop_contours"],
             ["double_right", "double_right", "change_shape_color"],
             ["double_right", "crop_contours", "crop_contours"],
             ["double_right", "crop_contours", "change_shape_color"],
             ["double_right", "change_shape_color", "change_shape_color"],
             ["crop_contours", "crop_contours", "crop_contours"],
             ["crop_contours", "crop_contours", "change_shape_color"],
             ["crop_contours", "change_shape_color", "change_shape_color"],
             ["change_shape_color", "change_shape_color", "change_shape_color"],
             ["double_right", "crop_contours", "double_right"],
             ["double_right", "change_shape_color", "double_right"],
             ["crop_contours", "change_shape_color", "double_right"],
             ["crop_contours", "double_right", "change_shape_color"],
             ["change_shape_color", "double_right", "crop_contours"],
             ["change_shape_color", "crop_contours", "double_right"]]

c35_train = [["extend_contours_same_color"], ["pad_left"], ["mirror_vertical"],
      ["extend_contours_same_color", "extend_contours_same_color"], ["pad_left", "pad_left"], ["mirror_vertical", "mirror_vertical"],
      ["extend_contours_same_color", "pad_left"], ["extend_contours_same_color", "mirror_vertical"],
      ["pad_left", "mirror_vertical"]]

c35_test = [["extend_contours_same_color", "extend_contours_same_color", "extend_contours_same_color"],
      ["extend_contours_same_color", "extend_contours_same_color", "pad_left"],
      ["extend_contours_same_color", "extend_contours_same_color", "mirror_vertical"],
      ["extend_contours_same_color", "pad_left", "pad_left"],
      ["extend_contours_same_color", "pad_left", "mirror_vertical"],
      ["extend_contours_same_color", "mirror_vertical", "mirror_vertical"],
      ["pad_left", "pad_left", "pad_left"],
      ["pad_left", "pad_left", "mirror_vertical"],
      ["pad_left", "mirror_vertical", "mirror_vertical"],
      ["mirror_vertical", "mirror_vertical", "mirror_vertical"],
      ["extend_contours_same_color", "pad_left", "extend_contours_same_color"],
      ["extend_contours_same_color", "mirror_vertical", "extend_contours_same_color"],
      ["pad_left", "mirror_vertical", "extend_contours_same_color"],
      ["pad_left", "extend_contours_same_color", "mirror_vertical"],
      ["mirror_vertical", "extend_contours_same_color", "pad_left"],
      ["mirror_vertical", "pad_left", "extend_contours_same_color"]]


compositionality_gridsize_config = []
grid_sizes = [30, 40, 50]

for gd in grid_sizes:
    
    ### C1
    
    compositionality_gridsize_config.append(make_config(
        c11_train,
        1, 1, "train", gd, gd))
    compositionality_gridsize_config.append(make_config(
        c11_test,
        1, 1, "test", gd, gd))

    compositionality_gridsize_config.append(make_config(
        c12_train,
        1, 2, "train", gd, gd))
    compositionality_gridsize_config.append(make_config(
        c12_test,
        1, 2, "test", gd, gd))

    compositionality_gridsize_config.append(make_config(
        c13_train,
        1, 3, "train", gd, gd))
    compositionality_gridsize_config.append(make_config(
        c13_test,
        1, 3, "test", gd, gd))

    compositionality_gridsize_config.append(make_config(
        c14_train,
        1, 4, "train", gd, gd))
    compositionality_gridsize_config.append(make_config(
        c14_test,
        1, 4, "test", gd, gd))

    compositionality_gridsize_config.append(make_config(
        c15_train,
        1, 5, "train", gd, gd))
    compositionality_gridsize_config.append(make_config(
        c15_test,
        1, 5, "test", gd, gd))

    #### C3

    compositionality_gridsize_config.append(make_config(
        c31_train,
        3, 1, "train", gd, gd))
    compositionality_gridsize_config.append(make_config(
        c31_test,
        3, 1, "test", gd, gd))

    compositionality_gridsize_config.append(make_config(
        c32_train,
        3, 2, "train", gd, gd))
    compositionality_gridsize_config.append(make_config(
        c32_test,
        3, 2, "test", gd, gd))

    compositionality_gridsize_config.append(make_config(
        c33_train,
        3, 3, "train", gd, gd))
    compositionality_gridsize_config.append(make_config(
        c33_test,
        3, 3, "test", gd, gd))

    compositionality_gridsize_config.append(make_config(
        c34_train,
        3, 4, "train", gd, gd))
    compositionality_gridsize_config.append(make_config(
        c34_test,
        3, 4, "test", gd, gd))

    compositionality_gridsize_config.append(make_config(
        c35_train,
        3, 5, "train", gd, gd))
    compositionality_gridsize_config.append(make_config(
        c35_test,
        3, 5, "test", gd, gd))