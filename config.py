from easydict import EasyDict as edict
import json

config = edict()
config.TRAIN = edict()

## Adam
config.TRAIN.batch_size = 21 #16
config.TRAIN.lr_init = 1e-4
config.TRAIN.beta1 = 0.9

## initialize G
config.TRAIN.n_epoch_init = 60 #100
    # config.TRAIN.lr_decay_init = 0.1
    # config.TRAIN.decay_every_init = int(config.TRAIN.n_epoch_init / 2)

## adversarial learning (SRGAN)
config.TRAIN.n_epoch = 300 #2000
config.TRAIN.lr_decay = 0.1
config.TRAIN.decay_every = max(1, int(config.TRAIN.n_epoch / 2))

## train set location
config.TRAIN.hr_img_path = 'datasets/RELEASE_2015-08-31/DATA/TRAIN/HD/'
config.TRAIN.lr_img_path = 'datasets/RELEASE_2015-08-31/DATA/TRAIN/LR/'

config.VALID = edict()
## test set location
#config.VALID.hr_img_path = 'datasets/DIV2K_valid_HR/'
#config.VALID.lr_img_path = 'datasets/DIV2K_valid_LR_bicubic/X4/'
config.VALID.hr_img_path = 'datasets/RELEASE_2015-08-31/DATA/TEST/HD/'
config.VALID.lr_img_path = 'datasets/RELEASE_2015-08-31/DATA/TEST/LR/'
config.VALID.annot_path = 'datasets/RELEASE_2015-08-31/DATA/TEST/ANNOTATION/'

def log_config(filename, cfg):
    with open(filename, 'w') as f:
        f.write("================================================\n")
        f.write(json.dumps(cfg, indent=4))
        f.write("\n================================================\n")
