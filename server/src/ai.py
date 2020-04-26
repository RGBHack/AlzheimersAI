from fastai.vision import *


def test(imgpath, trainpath):
    img = open_image(imgpath)
    path2 = Path(trainpath)
    learn = load_learner(path2)
    pred, idx, outputs = learn.predict(img)
    # print('Predicted class: ', pred)
    return str(pred)
