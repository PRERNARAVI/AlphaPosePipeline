import os, sys, glob
sys.path.append('/../../../..')

datapath = os.path.abspath('D:\\')
paths = glob.glob(os.path.join(datapath, 'Data/**/*.mp4'), recursive=True)
for video in paths:
    if video.endswith('.mp4'):
        print('Processing ' + video.split('\\')[-1])
        out = os.path.join(datapath, 'out', video.split('\\')[-3], video.split('\\')[-2])
        if not os.path.exists(out):
            os.makedirs(out)
        os.system('python video_demo.py --video {} --outdir {} --sp --save_video --vis_fast'.format(video, out))
