from model import *
from data import *

'''
    train the model
'''

data_gen_args = dict(rotation_range=0.2,
                    horizontal_flip=True,
                    fill_mode='nearest')
myGene = trainGenerator(2,'/scratch/sga64681/cv_proj/data/wooden-logs/train','images','labels',data_gen_args,save_to_dir = None)
model = unet()
model_checkpoint = ModelCheckpoint('unet_1204_log.hdf5', monitor='loss',verbose=1, save_best_only=True)
model.fit_generator(myGene,steps_per_epoch=2000,epochs=10,callbacks=[model_checkpoint])



