from backbones import model_class
from dataloader import dataprocess
import logger
MAX_EPOCHS = 10
INPUT_SIZE = 3
NUM_CLASS = 3
KERNEL = 10
LEARNING_RATE = 0.003

if __name__ == '__main__':
    trainer = logger.trainer(MAX_EPOCHS)
    model = model_class.TinyVGG(INPUT_SIZE,NUM_CLASS,KERNEL,LEARNING_RATE)
    datamodule = dataprocess.DataModule(batch_size=32)
    model.hparams.lr = logger.find_lr(model, datamodule)
    trainer.fit(model, datamodule=datamodule)
    