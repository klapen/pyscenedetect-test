# PySceneDetect test

Test to learn how to use [PySceneDetect](https://github.com/Breakthrough/PySceneDetect).

## Dependencies
# [Numpy](http://www.numpy.org)
# [OpenCV](https://opencv.org)

## Preparation

The last version available present some problems, so [it is required to use v0.3.5](https://github.com/Breakthrough/PySceneDetect/issues/32#issuecomment-309627736). So for this is better to use PIP to install the last stable version, and not follow the proyect readme instructions. 

### MacOS
For MacOS creating a virtual enviroment to use this repo create an error. For that reason, to be able to use it, it is required to install some dependencies throught [Homebrew](https://brew.sh). The steps for MacOS are:

* First ensure you have python2.7 globally installed in your computer. If not, you can get python2.7 [here](https://www.python.org).
* Install OpenCV with [Homebrew](https://brew.sh):
    ```
	$ brew install opencv3
    ```
* Install PySceneDetect:
    ```
	$ pip install pyscenedetect
    ```
* Git clone this repo to your PC
    ```
        $ git clone https://github.com/klapen/pyscenedetect-test.git
     ```
* Ready to use the test on global terminal

### Linux
On Linux, it is straight forward to use it on virtual enviroments. To run the test:
    ```
        $ git clone https://github.com/klapen/pyscenedetect-test.git
	$ cd pyscenedetect-test
	$ virtualenv -p python2.7 vtest
    	$ source vtest/bin/activate
    	$ pip install -r requirements.txt
    ```

## Usage

   ```
	python test.py [options] [files list]
   ```
   Options and arguments:
   * -s --save-images  : Save images for scene detection.
   * -d --detector     : Scene detector type. Only aceptable options are 'content' (default) or 'threshold'
   * [video file list] : List of video files to parse.
