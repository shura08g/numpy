import os
import subprocess
from datetime import timedelta, datetime
import time

video_extensions = ['mp4', 'avi']


def get_videos():
    videos = []
    for root, subfolders, files in os.walk(os.getcwd()):
        for file in files:
            if file.split('.')[-1] in video_extensions:
                videos.append(os.path.join(root, file))
                # print(os.path.join(root, file))
    return videos


def get_ps_output(filename):
    filename = filename.replace(' ', '\ ')
    cmd = "@powershell -c (New-Object -ComObject 'Shell.Application').\
                          NameSpace(0).ParseName('{}').\
                          ExtendedProperty('Duration')".format(filename)
    procc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
    # output = procc.stdout.read().decode().strip()
    # return output
    stdout, stderr = procc.communicate()
    return stdout.decode().strip()


def get_ps_size(filename):
    cmd_size = "@powershell -c (New-Object -ComObject 'Shell.Application').\
                          NameSpace(0).ParseName('{}').\
                          ExtendedProperty('Size')".format(filename)
    procc = subprocess.Popen(cmd_size, shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
    stdout, stderr = procc.communicate()
    return int(int(stdout.decode().strip())/1024)


def seconds_to_str(s):
    return str(timedelta(seconds=s))


def main():
    videos = get_videos()
    video_info = {}
    video_time = []
    total_duration_ms = 0
    total_dur = 0
    for video in videos:
        size = {}
        size['Size'] = str((get_ps_size(video))) + ' Kb '
        video_info[video.split('\\')[-1]] = size
        # video_info[video.split('\\')[-1]] = 'Size' + str((get_ps_size(video))) + ' Kb '
        time_r = (get_ps_output(video))
        video_time.append(time_r)
        time_ms = int(time_r)/10000
        time_min = timedelta(milliseconds=time_ms)
        # video_info[video.split('\\')[-1]] += ' Duration: ' + str(time_min)
        duration = {}
        duration['Duration'] = str(time_min).split('.')[0]
        video_info[video.split('\\')[-1]].update(duration)
    print(video_info)

    for t in video_time:
        total_duration_ms += int(t)

    total_ms = int(total_duration_ms)/10000
    total_min = timedelta(milliseconds=total_ms)
    print("Total duration {} files: {}".format(len(videos), total_min))

    for k, v in video_info.items():
        t = time.strptime(v['Duration'], '%H:%M:%S')
        t_s = timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
        total_dur += t_s
    print("Total duration {} files: {}".format(len(videos), seconds_to_str(total_dur)))

if __name__ == '__main__':
    main()
