from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_spawn_controllers_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("motoman_sia5f", package_name="yaskawa_moveit_config_ros2").to_moveit_configs()
    return generate_spawn_controllers_launch(moveit_config)
