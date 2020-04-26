To create our AI model, we used the Jupyter Notebook `NeuralZ-training\train3.ipynb`. Additionally, `ailib` contains an easy to use library to leverage AI for images. This is an example of how to use the library:
```py
import ailib

def example():
    init("./train")
    train1("train1")
    train2("train2",1e-6,1e-5)
    predict("./img.jpg","./export")
```
More extensive documentation can be found on this repository's [Wiki Page](https://github.com/raad1masum/AlzheimersAI/wiki).