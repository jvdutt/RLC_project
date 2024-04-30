#!/bin/bash

# Create a new tmux session
session_name="record_bag_$1"
tmux new-session -d -s $session_name

# Split the window into three panes
tmux selectp -t 0    # select the first (0) pane
tmux splitw -v -p 50 # split it into two halves
tmux selectp -t 0    # go back to the first pane
tmux splitw -h -p 50 # split it into two halves
tmux selectp -t 0    # go back to the first pane
tmux splitw -h -p 50 # split it into two halves


tmux select-pane -t 0
tmux send-keys "rosrun nomad_turtlebot3 image_subscriber.py" Enter

# Run the roslaunch command in the first pane
tmux select-pane -t 1
tmux send-keys "sshpass -p "turtlebot" ssh ubuntu@10.42.0.211" Enter
tmux send-keys "./bringup.sh" Enter

# Run the teleop.py script in the second pane
tmux select-pane -t 2
tmux send-keys "conda activate vint_deployment" Enter
tmux send-keys "../../../teleop.sh" Enter

# # Change the directory to ../topomaps/bags and run the rosbag record command in the third pane
tmux select-pane -t 3
# tmux send-keys "cd ../../datasets/cps_rosbags" Enter
tmux send-keys "cd ../topomaps/bags" Enter
tmux send-keys "rosbag record /camera_img_raw  /odom -O $1" # change topic if necessary

# # Attach to the tmux session
tmux -2 attach-session -t $session_name