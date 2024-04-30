# import numpy as np
# import matplotlib.pyplot as plt
# import os
# import imageio as iio
# import pickle 


# file_path =lambda x: f"datasets/cps/traj{x}/traj_data.pkl"

# def get_position_yaw(i):
#     with open(file_path(i),"rb") as f:
#         data = pickle.load(f)
#     return data["position"],data["yaw"]



# positions = [get_position_yaw(i)[0] for i in range(12)]
# avg_list = []
# n = 0 
# for p in positions:
#     avg = np.array([np.linalg.norm(b-a,ord=2) for a,b in zip(p,p[1:])]).sum()
#     print(avg)
#     avg_list.append(avg)
#     n+=len(p)

# print("final:",np.array(avg_list).sum(0)/n)

# exit()
# for i in range(12):

#     position,yaw = get_position_yaw(i)

#     plt.subplot(211)
#     plt.plot(position[:,0],position[:,1])
#     plt.subplot(212)
#     plt.plot(yaw)
#     plt.show()






















 #########################################traj_data.pkl visualization###############################
# import numpy as np
# import matplotlib.pyplot as plt
# import os
# import imageio as iio
# import pickle 

# file_path =lambda x: f"datasets/cps/traj{x}/traj_data.pkl"

# def get_position_yaw(i):
#     with open(file_path(i),"rb") as f:
#         data = pickle.load(f)
#     return data["position"],data["yaw"]


# for i in range(12):
#     position,yaw = get_position_yaw(i)

#     plt.subplot(211)
#     plt.plot(position[:,0],position[:,1])
#     plt.subplot(212)
#     plt.plot(yaw)
#     plt.show()




################################change to RGB (bluish to color problem)###########################################################

import numpy as np
import matplotlib.pyplot as plt
import os
import imageio as iio

folder = "/media/vishnu/New Volume/Acads/Sem2/RLC/project/visualnav-transformer/deployment/topomaps/images/cps_board_room/"


for file in os.listdir(folder):
    file_path = os.path.join(folder,file)
    if file_path.endswith(".png"):
        img = iio.imread(file_path)
        img = img[:,:,::-1]
        iio.imwrite(file_path,img)


exit()


# img_path = "datasets/cps/traj9_2/95.jpg"

 
# # read an image 

# print(img.shape)
# plt.imshow(img[:,:,::-1])
# plt.show()
