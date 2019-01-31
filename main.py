from model import * 
from data import *

'''
    main file to predict the output
'''

# output will be generated in the same library. make sure you remove files other than input files before execution
testGene = testGenerator("/scratch/sga64681/cv_proj/data/wooden-logs/test/")

model = unet()
model.save_weights("unet_new_log.hdf5")
model.load_weights("unet_new_log.hdf5")

results = model.predict_generator(testGene,1,1,verbose=1)

saveResult("/scratch/sga64681/cv_proj/data/wooden-logs/test",results)
# below step is executed seperately since matplotlib is not installed on cluster
#postprocess("/scratch/sga64681/cv_proj/data/wooden-logs/test")
