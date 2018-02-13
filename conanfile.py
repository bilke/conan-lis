#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os


class LibnameConan(ConanFile):
    name = "lis"
    version = "1.7.9"
    url = "https://github.com/bilke/conan-lis"
    description = "Library of Iterative Solvers for linear systems"

    # Indicates License type of the packaged library
    license = "Custom"

    # Packages the license for the conanfile.py
    exports = ["LICENSE"]

    # Remove following lines if the target lib does not use cmake.
    #exports_sources = ["CMakeLists.txt"]
    #generators = "cmake"

    # Options may need to change depending on the packaged library.
    settings = "os", "arch", "compiler", "build_type"

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def source(self):
        source_url = "http://www.ssisc.org/lis"
        tools.get("{0}/dl/lis-{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)


    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.configure(configure_dir=self.source_subfolder)
        env_build.make()

    def package(self):
        self.copy(pattern="LICENSE", dst="license", src=self.source_subfolder)
        self.copy(pattern="*.h", dst="include", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
