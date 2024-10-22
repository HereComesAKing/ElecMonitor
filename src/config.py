from os import getcwd, path
import json

from toast import toast_warn

working_dir = getcwd()

config_path = path.join(working_dir, "config.json")
config_version = 1


def read_config() -> dict:
    try:
        config = json.load(open(config_path))
    except FileNotFoundError:
        toast_warn("配置文件不存在，请检查！")
        return None

    if config["version"] != config_version:
        toast_warn("配置文件版本不匹配，请检查！")
        return None

    return config
