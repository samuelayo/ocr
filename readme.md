Implementing OCR(Optical Character Recognition) using Python and the tesseract library

## Installation:

- Install tesserct-ocr using this command:
```
sudo apt-get install tesseract-ocr
```
- Install python binding for tesseract, PyOCR, using this pip command:
```
pip install git+https://github.com/jflesch/pyocr.git
```
- Install image processing library in python, pillow using this pip command:
```
pip install pillow
```
- Install wand library. python bindings for Imagemagic

```
pip install wand
```

## Setting up and usage

- clone this repo 

```
git clone https://github.com/samuelayo/ocr.git
```

- change directory to this repo 
```
cd ocr
```
- read text from image or pdf
```
python3 ocr.py "MY_FILE_PATH"

```
**MY_FILE_PATH refers to the path of the file you would like to use ocr on.**

- Run unit tests
```
python3 -m unittest discover
```
