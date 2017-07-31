from package import Package
class PackageInstaller(object):
    def __init__(self):
        self.package_list = []
        self.installs = []
        self.package_to_install=[]
        self.package_params = []
        self.dependencies = []

    def install_package(self,txt):
        #open the file containing the packages to install
        input_txt = open(txt)
        self.package_list = input_txt.readlines()
        for package in self.package_list:
            package_param = package.split()
            self.package_params.append(package_param)
        print(self.package_params)

        #Check for packages to be installed and append them to a list self.package_to_nstall
        for packy in self.package_params:
            if packy[0] == 'INSTALL':
                self.package_to_install.append(packy[1])
        # print(self.package_to_install)

        #Check for a particular package's dependencies and append the depencies into a list self.dependencies
        for packa in self.package_to_install:
            print("Install %s" %packa)
            for dependant in self.package_params:
                if dependant[0] =='DEPEND' and(dependant[1] == packa):
                    for dependency in dependant:
                        self.dependencies.append(dependency)

            lens = len(self.dependencies)
        #loop through the dependencies and install one by one

            while lens > 1:
                pack = Package(self.dependencies[lens-1])
                install = pack.mypackage()
                self.installs.append(install)
                if install == packa and install== self.dependencies[lens-1]:
                    break
                if packa not in self.dependencies:
                    break
                print("Installing dependant %s " %install)
                lens-=1
            print('Now installing package %s' %packa)
        # print(self.package_list)

        # return self.installs


packs = PackageInstaller()
print(packs.install_package('tt.txt'))




    # def uninstall_package(self):