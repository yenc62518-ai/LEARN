'''
Class tải dữ liệu:

Tham số: 
batch_size (int)
data_dir: đường dẫn đến data (Path)

Trả về:
prepare_data(): tải dữ liệu được ghi trong data_dir
setup(): chuẩn bị dữ liệu dựa trên hàm gọi 
data_loader(): trả về data_loader với data là train/test/val 
'''
import os
from pathlib import Path
from torchvision.transforms import v2 as TV2
from torch.utils.data import random_split, DataLoader
import pytorch_lightning as PL
from torchvision.datasets import ImageFolder
class DataModule(PL.LightningDataModule) :
    def __init__(self, batch_size=32, data_dir = Path("pizza_steak_sushi/"), num_workers = os.cpu_count()):
        super().__init__()
        self.batch_size = batch_size
        self.data_dir = data_dir
        self.train_transform = TV2.Compose([
            TV2.Resize((64,64)),
            TV2.ToTensor()
            ])
        self.test_transform = TV2.Compose([
            TV2.Resize((64,64)),
            TV2.ToTensor()
            ])
    def prepare_data(self):
        pass
    def setup(self, stage = None):
        if (stage == 'fit' or stage is None):
            full_train_ds = ImageFolder(root=self.data_dir / 'train', transform=self.train_transform)
            train_len = int(0.8 * len(full_train_ds))
            val_len = len(full_train_ds) - train_len
            self.train_ds, self.val_ds = random_split(full_train_ds, [train_len, val_len])
            # train_subset, val_subset = random_split(full_train_ds, [train_len, val_len])
            # self.train_ds = Subset(
            #                     ImageFolder(root=self.data_dir / 'train', transform=self.train_transform),
            #                     indices = train_subset.indices)
            # self.val_ds = Subset(
            #                     ImageFolder(root=self.data_dir / 'train', transform=self.test_transform),
            #                     indices=val_subset.indices)

        if (stage == 'test' or stage is None):
            self.test_ds = ImageFolder(root = self.data_dir / 'test', transform=self.test_transform)

    def train_dataloader(self):
        return DataLoader(dataset = self.train_ds, batch_size=self.batch_size, shuffle=True, num_workers=self.num_worker)
    def test_dataloader(self):
        return DataLoader(dataset = self.test_ds, batch_size=self.batch_size, num_workers=self.num_worker)
    def val_dataloader(self):
        return DataLoader(dataset = self.val_ds, batch_size=self.batch_size,num_workers=self.num_worker)
