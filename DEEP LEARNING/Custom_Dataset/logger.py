'''
Hàm khai báo các phương thức Logger, CheckPoint, EarlyStopping và Trainer

Tham số:
không

Trả về: 
trainer: chạy trên auto accelerator, tối đa 10 epoch, sử dụng:
    logger: TensorBoardLogger
    checkpoint: theo dõi val_loss, lưu toàn bộ giá trị model tốt nhất
    earlystop: theo dõi val_f1, dừng nếu 3 epochs không tăng 0.005
'''
from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping
from pytorch_lightning.loggers import TensorBoardLogger
import pytorch_lightning as PL
from pytorch_lightning.tuner import Tuner
def trainer(MAX_EPOCHS = 10):
    logger = TensorBoardLogger(save_dir='tb_log')
    checkpoint = ModelCheckpoint(monitor='val_loss', mode = 'min', save_top_k=1, save_weights_only=False)
    earlystop = EarlyStopping(monitor='val_f1', mode = 'max', min_delta = 0.005, patience=3)
    trainer = PL.Trainer(accelerator='auto',
                        logger = logger,
                        callbacks = [checkpoint, earlystop],
                        max_epochs=MAX_EPOCHS)
    return trainer
def find_lr(model, datamodule):
    tuner = Tuner(trainer)
    lr_finder = tuner.lr_find(model, datamodule=datamodule, min_lr = 0.001, max_lr = 0.01)
    return lr_finder.suggestion()

