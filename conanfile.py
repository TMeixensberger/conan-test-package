from conans import ConanFile, CMake, tools


class WorldConan(ConanFile):
    name = "world"
    version = "1.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Test here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("cp /home/vboxuser/conan-test/world/hello-world . -r")
         
    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure(source_folder="hello-world")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello-world")
        self.copy("*hello-world.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello-world"]

