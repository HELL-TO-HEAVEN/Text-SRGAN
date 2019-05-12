# Text-SRGAN
Application of SRGAN to text images for improving OCR accuracy

<b>Prerequisites: </b>Tensorflow, Tensorlayer, Scipy, Numpy, Tesseract OCR, Pytesseract

After installing the prerequisite libraries, run the code with

``python3 main.py``

<b>Arguments:</b>

``--mode=evaluate`` : Evaluate on single image

``--mode=evaluateall`` : Evaluate all images

``--ocr=true`` : Enable OCR

``--ocr=false`` : Run without OCR

<b>Dataset:</b>

In our case, training was done on the ICDAR 2015 Text SR dataset (https://projet.liris.cnrs.fr/sr2015/index.php?p=2) for 60+300 epochs.
