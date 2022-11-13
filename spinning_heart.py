## for janie uwu
from cv2 import imread, resize, INTER_AREA
from os import system, listdir, path
from time import sleep

frames = [imread(path.join('heart_frames', file_name), 0) for file_name in listdir('heart_frames')]
frames_amount = len(frames)

width, height = frames[0].shape
new_height = 25
height, width = new_height, int(new_height * (width / height))
frames = [resize(frame, (height, width), INTER_AREA) for frame in frames]

max_gray, min_gray = -1, 256
for frame in frames:
    for i in range(width):
        for j in range(height):
            if frame[i][j] == 0: continue
            max_gray = max(max_gray, frame[i][j])
            min_gray = min(min_gray, frame[i][j])

luminance = ' .,-~:;=!*#$@'
luminance_len = len(luminance)

thickness = 4
wait_time = 0.1

wave_pos = 0
index = 0
while True:
    system('cls') 
    for i in range(width - 1):
        print(20 * ' ', end = '')
        for j in range(height):
            gray = frames[index // 2][i][j]
            if gray == 0: print(thickness * luminance[0], end = '')
            else:
                for k in range(1, luminance_len):
                    if gray > int(k * ((max_gray - min_gray + 1) / (luminance_len - 1)) + min_gray - 1): continue
                    print(thickness * luminance[k], end = '')
                    break
        print('\n')
    wave = 10 * '-'
    if wave_pos > 0: wave = wave[: wave_pos - 1] + "_" + wave[wave_pos :]
    if wave_pos < 9: wave = wave[: wave_pos + 1] + "'" + wave[wave_pos + 2 :]
    wave1 = wave[: 9] + '_' if wave_pos == 0 else wave
    print(44 * ' ' + wave[: : -1] + wave1[: : -1] + 'chái tym uwu' + wave1 + wave)
    index = index + 1 if index < 2 * (frames_amount - 1) else 0
    wave_pos = wave_pos + 1 if wave_pos < 9 else 0
    sleep(wait_time)