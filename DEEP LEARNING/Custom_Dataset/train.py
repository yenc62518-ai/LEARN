from backbones import model_class
from dataloader import dataprocess
import logger
if __name__ == '__main__':
    trainer = logger.trainer()
    model = model_class.TinyVGG(3,3,10,0.003)
    datamodule = dataprocess.DataModule(batch_size=32) 
    trainer.fit(model, datamodule=datamodule)