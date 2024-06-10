from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_bot',
            executable='waypoint_follower.py',
            name='waypoint_follower',
            output='screen',
        ),
    ])
