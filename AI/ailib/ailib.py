#First install pytorch, then install all the libaries listed below (PIL should be default)
from fastai.vision import *
import pandas as pd
import numpy as np
import PIL
from PIL import Image

path = None
data = None
learn = None

#run this before running train1 or train2 (if running predict you can skip this function)
def init(datapath):
    path = Path('../data/train')
    np.random.seed(42)
    data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
        size=112, num_workers=4).normalize(imagenet_stats)
    learn = cnn_learner(data, models.resnet101, metrics=error_rate)
#run train 1 to get info for more accurate train2 function, savename should not include pth extension
def train1(savename):
    learn.fit_one_cycle(4)
    learn.save(savename)
    learn.unfreeze()
    learn.lr_find()
    learn.recorder.plot()
#run train2 after train1 for better training, you should see a file called export.pkl in your training directory, KEEP THIS FILE
def train2(savename,slicemax,slicemin,exportfolder):
    learn.fit_one_cycle(10, max_lr=slice(slicemax,slicemin))
    learn.save(savename)
    learn.export()
#use to predict
def predict(exportfolder,imagepath):
    learn = load_learner(exportfolder)
    img = open_image(imagepath)
    pred,idx,outputs = learn.predict(img)
    return pred