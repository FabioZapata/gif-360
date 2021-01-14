import imageio
from pygifsicle import optimize

video_read = imageio.mimread('assets/video.mp4', fps=3, memtest=False)
print(len(video_read))
imageio.mimwrite('assets/video.gif', video_read, fps=20)
gif_path = 'assets/video.gif'
# create a new one
optimize(gif_path, 'assets/video.gif')
# overwrite the original one
optimize(gif_path)


# !pip install pygifsicle
# from pygifsicle import optimize
# gif_path = 'video.gif'
# # create a new one
# optimize(gif_path, 'video.gif')
# # overwrite the original one
# optimize(gif_path)