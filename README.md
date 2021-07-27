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
