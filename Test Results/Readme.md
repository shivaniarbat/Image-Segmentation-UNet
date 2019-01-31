# * Required to execute the program * 
Tensorflow
Keras >= 1.0
Most of the part coded with Python 3.7 conventions.


Folder Organization :

Input files :  ./Approach_1/data/wooden-logs/test/.     - for testing 
			./Approach_1/data/wooden-logs/train/images  - for training 
Input files are the input images for the program

Output: ./Approach_1/data/wooden-logs/test/.  
Output will be created with the name same file name .png in above folder

Ground Truth Labels: ./Approach_1/data/wooden-logs/train/labels  - for training 
This folder contains the ground truth labels for the respective images. Mapping can be identified by the name.

** two models were trained on same data ** 
One with 5 epochs - “unet_1203_log.hdf5”

Second with 10 epochs - “unet_new_log.hdf5”

— Instructions to run the program. 

1. Copy the file to be tested in input file folder for testing mentioned above. Rename the file 0.png - this is hardcoded in the code. The program will read the file in numerical order only. Make sure no other files are present in the same folder. 

If needed can be updated in data.py in testGenerator method by updating num_image variable value. 

2. Update the path as required
3. Make sure the trained model is in the same folder as of execution
4. Final step requires matplotlib installed on machine. Since GACRC cluster does not have one this part is coded separately. 
5. Post-processed image is shown in the final report.  
