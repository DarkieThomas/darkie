from launch import LaunchDescription
from launch_ros.actions import Node
import os
import xacro

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg_path = get_package_share_directory('darkie')

    xacro_file = os.path.join(pkg_path, 'urdf', 'maze_urdf.xacro')

    robot_description = xacro.process_file(xacro_file).toxml()

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])
