# COVID19
you can train your own dataset

creat a new folder 'data' and 'checkpoint'，then the directory structure is as follows:

-checkpoint

-data 

    -train   (train dataset)
        -image    (CT images)
        -mask     (GT images)
        -mask_    (EdgeEGT images)
    -val        (validation dataset)
        -image    (CT images)
        -mask     (GT images)
        -mask_    (EdgeEGT images)

You can modify the parameter settings in /resources/train_config.yaml

-batch_size

-learning_rate

-weight_decay

-checkpoint_save_dir

-loss_function
...


finally run train.py, the model will saved in checkpoint folder.

# Citation
Please cite our paper if you find the work useful:

@article{hu2022deep,

author = {Haigen Hu and Leizhao Shen and Qiu Guan and Xiaoxin Li and Qianwei Zhou and Su Ruan},

journal = {Pattern Recognition},

title = {Deep co-supervision and attention fusion strategy for automatic COVID-19 lung infection segmentation on CT images},

year = {2022},

volume = {124},

pages = {108452},

doi = {https://doi.org/10.1016/j.patcog.2021.108452},

}
