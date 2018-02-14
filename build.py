from conan.packager import ConanMultiPackager
import copy
import platform
from conans.tools import os_info

if __name__ == "__main__":
    if not os_info.is_windows:
        builder = ConanMultiPackager(archs = ["x86_64"])
        builder.add_common_builds(pure_c=True)
        builder.run()
