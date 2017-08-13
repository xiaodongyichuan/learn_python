
#!/bin/sh

#Hi,there. This is the shell script want to change the train_data.txt's path. The purpose of this shell is to prepare for the date training.




# sed's usage:
#	sed -i 's#'oldpath'#'newpath'#ig' filername 
sed -i 's#'/home/qian/Documents/OpenCV/001_Landmark_with_Regressition_in_Python/afw'#'/home/qian/Documents/OpenCV/001_Landmark_with_Regressition_in_Python/afw/'#ig' afw_train.txt
