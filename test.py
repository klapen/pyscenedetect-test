#!/usr/bin/python
import os,sys,getopt
import scenedetect

def validateInputFiles(files):
    files_list = []
    for file in files:
        os.path.exists(file) and files_list.append(file)
    return files_list

def videoDetection(path,save_images,detector):
    print "*-*-*- Start processing the file "+path
    scene_list = [] # Scenes will be added to this list in detect_scenes().

    # Usually use one detector, but multiple can be used.
    if(detector == 'content'):
        detector_list = [scenedetect.detectors.ContentDetector(threshold = 30, min_scene_len = 15)]
    else:
        detector_list = [scenedetect.detectors.ThresholdDetector(threshold = 16, min_percent = 0.9)]
        
    video_fps, frames_read = scenedetect.detect_scenes_file(path, scene_list, detector_list, save_images = save_images)
    print 'Scene_list now contains the frame numbers of scene boundaries.'
    print scene_list
    
    # create new list with scene boundaries in milliseconds instead of frame #.
    scene_list_msec = [(1000.0 * x) / float(video_fps) for x in scene_list]
    print 'Boundaries in milliseconds instead of frame'
    print scene_list_msec
    
    # create new list with scene boundaries in timecode strings ("HH:MM:SS.nnn").
    scene_list_tc = [scenedetect.timecodes.get_string(x) for x in scene_list_msec]
    print 'Boundaries in timecode strings ("HH:MM:SS.nnn").'
    print scene_list_tc
    print 'End processing '+path+' *-*-*-'
    
if __name__ == '__main__':
    argv = sys.argv[1:]
    try:
        opts,args = getopt.getopt(argv, "hsd:",["save-images=","detector="])
    except getopt.GetopError:
        print 'test.py -s -d [detector] [video file list]'
        sys.exit(2)
        
    save_images = False
    detector_type = "content"
    for opt,arg in opts:
        if opt == '-h':
            print """
            usage: python test.py [options] [files list]
            Options and arguments:
            -s --save-images  : Save images for scene detection.
            -d --detector     : Scene detector type. Only aceptable options are 'content' (default) or 'threshold'
            [video file list] : List of video files to parse.
            """
            sys.exit()
        elif opt in ("-s","--save-images"):
            save_images = True
        elif opt in ("-d","--detector"):
            detector_type = arg if arg in('content','threshold') else 'content'

    input_files = validateInputFiles(args)
    for video_file in input_files:
        videoDetection(video_file,save_images,detector_type)
