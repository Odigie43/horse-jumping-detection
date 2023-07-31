import os
from ultralytics import YOLO

# TO AVOID THE ERROR BOLOW
# SEE: https://stackoverflow.com/questions/20554074/sklearn-omp-error-15-initializing-libiomp5md-dll-but-found-mk2iomp5md-dll-a
# OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.
# OMP: Hint This means that multiple copies of the OpenMP runtime have been linked into the program. That is dangerous, since it can degrade performance or cause incorrect results. The best thing to do is to ensure that only a single OpenMP runtime is linked into the process, e.g. by avoiding static linking of the OpenMP runtime in any library. As an unsafe, unsupported, undocumented workaround you can set the environment variable KMP_DUPLICATE_LIB_OK=TRUE to allow the program to continue to execute, but that may cause crashes or silently produce incorrect results. For more information, please see http://www.intel.com/software/products/support/.
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE" # OR conda install nomkl --channel conda-forge

# FOR COMMAND LINE USAAGE
#windows
#set KMP_DUPLICATE_LIB_OK=True [COMMAND]
#linux
#export KMP_DUPLICATE_LIB_OK=True [COMMAND]

# YOU CAN ALSO: Delete the copy of libiomp5md.dll in your virtual env.
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='D:\PROJECTS\PYTHON\\ROBOFLOW\\yolov8-streamlit-detection-tracking\\datasets\\horse-race\\data.yaml',
   imgsz=640,
   epochs=100,
   batch=10,
   name='yolov8n_v8_horse_race'
)