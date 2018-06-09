import scenedetect

scene_list = []        # Scenes will be added to this list in detect_scenes().
path = 'my_video.mp4'  # Path to video file.

# Usually use one detector, but multiple can be used.
detector_list = [
    scenedetect.detectors.ThresholdDetector(threshold = 16, min_percent = 0.9)
]

video_fps, frames_read = scenedetect.detect_scenes_file(path, scene_list, detector_list, save_images = True)
print 'Scene_list now contains the frame numbers of scene boundaries.'
print scene_list

# create new list with scene boundaries in milliseconds instead of frame #.
scene_list_msec = [(1000.0 * x) / float(video_fps) for x in scene_list]
print 'List with scene boundaries in milliseconds instead of frame'
print scene_list_msec

# create new list with scene boundaries in timecode strings ("HH:MM:SS.nnn").
scene_list_tc = [scenedetect.timecodes.get_string(x) for x in scene_list_msec]
print 'list with scene boundaries in timecode strings ("HH:MM:SS.nnn").'
print scene_list_tc
