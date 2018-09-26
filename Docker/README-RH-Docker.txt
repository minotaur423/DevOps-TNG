Get Docker EE for Red Hat Enterprise Linux
Estimated reading time: 11 minutes
There are two ways to install and upgrade Docker Enterprise Edition (Docker EE) on Red Hat Enterprise Linux:

YUM repository: Set up a Docker repository and install Docker EE from it. This is the recommended approach because installation and upgrades are managed with YUM and easier to do.

RPM package: Download the RPM package, install it manually, and manage upgrades manually. This is useful when installing Docker EE on air-gapped systems with no access to the internet.

Docker Community Edition (Docker CE) is not supported on Red Hat Enterprise Linux.

Prerequisites
This section lists what you need to consider before installing Docker EE. Items that require action are explained below.

Use RHEL 64-bit 7.1 and higher on x86_64, s390x, or ppc64le (not ppc64).
Use storage driver overlay2 or devicemapper (direct-lvm mode in production).
Find the URL for your Docker EE repo at Docker Store.
Uninstall old versions of Docker.
Remove old Docker repos from /etc/yum.repos.d/.
Disable SELinux on s390x (IBM Z) systems before install/upgrade.
Architectures and storage drivers
Docker EE supports Red Hat Enterprise Linux 64-bit, versions 7.1 and higher (7.1, 7.2, 7.3, 7.4), running on one of the following architectures: x86_64, s390x (IBM Z), or ppc64le (IBM Power, little endian format). To ensure you have ppc64le (and not ppc64), run the command, uname -m.

Little endian format only

On IBM Power systems, Docker EE only supports little endian format, ppc64le, even though RHEL 7 ships both big and little endian versions.

On Red Hat Enterprise Linux, Docker EE supports storage drivers, overlay2 and devicemapper. In Docker EE 17.06.2-ee-5 and higher, overlay2 is the recommended storage driver. The following limitations apply:

OverlayFS: If selinux is enabled, the overlay2 storage driver is supported on RHEL 7.4 or higher. If selinux is disabled, overlay2 is supported on RHEL 7.2 or higher with kernel version 3.10.0-693 and higher.

Device Mapper: On production systems using devicemapper, you must use direct-lvm mode, which requires one or more dedicated block devices. Fast storage such as solid-state media (SSD) is recommended. Do not start Docker until properly configured per the storage guide.

Find your Docker EE repo URL
To install Docker EE, you will need the URL of the Docker EE repository associated with your trial or subscription:

Go to https://store.docker.com/my-content. All of your subscriptions and trials are listed.
Click the Setup button for Docker Enterprise Edition for Red Hat Enterprise Linux.
Copy the URL from Copy and paste this URL to download your Edition and save it for later use.
You will use this URL in a later step to create a variable called, DOCKERURL.

Uninstall old Docker versions
The Docker EE package is called docker-ee. Older versions were called docker or docker-engine. Uninstall all older versions and associated dependencies. The contents of /var/lib/docker/ are preserved, including images, containers, volumes, and networks.

$ sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine \
                  docker-ce
Repo install and upgrade
The advantage of using a repository from which to install Docker EE (or any software) is that it provides a certain level of automation. RPM-based distributions such as Red Hat Enterprise Linux, use a tool called YUM that work with your repositories to manage dependencies and provide automatic updates.

Disable SELinux before installing Docker EE on IBM Z systems

There is currently no support for selinux on IBM Z systems. If you attempt to install or upgrade Docker EE on an IBM Z system with selinux enabled, an error is thrown that the container-selinux package is not found. Disable selinux before installing or upgrading Docker on IBM Z.

Set up the repository
You only need to set up the repository once, after which you can install Docker EE from the repo and repeatedly upgrade as necessary.

Remove existing Docker repositories from /etc/yum.repos.d/:

$ sudo rm /etc/yum.repos.d/docker*.repo
Temporarily store the URL (that you copied above) in an environment variable. Replace <DOCKER-EE-URL> with your URL in the following command. This variable assignment does not persist when the session ends.

$ export DOCKERURL="<DOCKER-EE-URL>"
Store the value of the variable, DOCKERURL (from the previous step), in a yum variable in /etc/yum/vars/:

$ sudo -E sh -c 'echo "$DOCKERURL/rhel" > /etc/yum/vars/dockerurl'
Also, store your OS version string in /etc/yum/vars/dockerosversion. Most users should use 7, but you can also use the more specific minor version, starting from 7.2.

$ sudo sh -c 'echo "7" > /etc/yum/vars/dockerosversion'
Install required packages: yum-utils provides the yum-config-manager utility, and device-mapper-persistent-data and lvm2 are required by the devicemapper storage driver:

$ sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
Enable the extras RHEL repository. This ensures access to the container-selinux package required by docker-ee.

The repository can differ per your architecture and cloud provider, so review the options in this step before running:

For all architectures except IBM Power:

$ sudo yum-config-manager --enable rhel-7-server-extras-rpms
For IBM Power only (little endian):

$ sudo yum-config-manager --enable extras
$ sudo subscription-manager repos --enable=rhel-7-for-power-le-extras-rpms
$ sudo yum makecache fast
$ sudo yum -y install container-selinux
Depending on cloud provider, you may also need to enable another repository:

For AWS (where REGION is a literal, and does not represent the region your machine is running in):

$ sudo yum-config-manager --enable rhui-REGION-rhel-server-extras
For Azure:

$ sudo yum-config-manager --enable rhui-rhel-7-server-rhui-extras-rpms
Add the Docker EE stable repository:

$ sudo -E yum-config-manager \
    --add-repo \
    "$DOCKERURL/rhel/docker-ee.repo"
Install from the repository
There are currently two versions of Docker EE Engine available:

18.03 - Use this version if you’re only running Docker EE Engine.
17.06 - Use this version if you’re using Docker Enterprise Edition 2.0 (Docker Engine, UCP, and DTR).
By default, Docker EE Engine 17.06 is installed. If you want to install the 18.03 version run:

 sudo yum-config-manager --enable docker-ee-stable-18.03
Install the latest patch release, or go to the next step to install a specific version:

$ sudo yum -y install docker-ee
If prompted to accept the GPG key, verify that the fingerprint matches 77FE DA13 1A83 1D29 A418 D3E8 99E5 FF2E 7668 2BC9, and if so, accept it.

To install a specific version of Docker EE (recommended in production), list versions and install:

a. List and sort the versions available in your repo. This example sorts results by version number, highest to lowest, and is truncated:

$ sudo yum list docker-ee  --showduplicates | sort -r

docker-ee.x86_64      17.06.ee.2-1.el7.rhel      docker-ee-stable-17.06
The list returned depends on which repositories you enabled, and is specific to your version of Red Hat Enterprise Linux (indicated by .el7 in this example).

b. Install a specific version by its fully qualified package name which is the package name (docker-ee) plus the version string (2nd column) up to the hyphen, for example: docker-ee-17.06.1.ee.2

$ sudo yum -y install <FULLY-QUALIFIED-PACKAGE-NAME>
Docker is installed but not started. The docker group is created, but no users are added to the group.

Start Docker:

If using devicemapper, ensure it is properly configured before starting Docker, per the storage guide.

$ sudo systemctl start docker
Verify that Docker EE is installed correctly by running the hello-world image. This command downloads a test image, runs it in a container, prints an informational message, and exits:

$ sudo docker run hello-world
Docker EE is installed and running. Use sudo to run Docker commands. See Linux postinstall to allow non-privileged users to run Docker commands.

Upgrade from the repository
Add the new repository.

Follow the installation instructions and install a new version.

Package install and upgrade
To manually install Docker EE, download the .rpm file for your release. You need to download a new file each time you want to upgrade Docker EE.

Disable SELinux before installing Docker EE on IBM Z systems

There is currently no support for selinux on IBM Z systems. If you attempt to install or upgrade Docker EE on an IBM Z system with selinux enabled, an error is thrown that the container-selinux package is not found. Disable selinux before installing or upgrading Docker on IBM Z.

Install with a package
Enable the extras RHEL repository. This ensures access to the container-selinux package which is required by docker-ee:

$ sudo yum-config-manager --enable rhel-7-server-extras-rpms
Alternately, obtain that package manually from Red Hat. There is no way to publicly browse this repository.

Go to the Docker EE repository URL associated with your trial or subscription in your browser. Go to rhel/. Choose your Red Hat Enterprise Linux version, architecture, and Docker version. Download the .rpm file from the Packages directory.

If you have trouble with selinux using the packages under the 7 directory, try choosing the version-specific directory instead, such as 7.3.

Install Docker EE, changing the path below to the path where you downloaded the Docker package.

$ sudo yum install /path/to/package.rpm
Docker is installed but not started. The docker group is created, but no users are added to the group.

Start Docker:

If using devicemapper, ensure it is properly configured before starting Docker, per the storage guide.

$ sudo systemctl start docker
Verify that Docker EE is installed correctly by running the hello-world image. This command downloads a test image, runs it in a container, prints an informational message, and exits:

$ sudo docker run hello-world
Docker EE is installed and running. Use sudo to run Docker commands. See Linux postinstall to allow non-privileged users to run Docker commands.

Upgrade with a package
Download the newer package file.

Repeat the installation procedure, using yum -y upgrade instead of yum -y install, and point to the new file.

Uninstall Docker EE
Uninstall the Docker EE package:

$ sudo yum -y remove docker-ee
Delete all images, containers, and volumes (because these are not automatically removed from your host):

$ sudo rm -rf /var/lib/docker
Delete other docker related resources:
$ sudo rm -rf /run/docker
$ sudo rm -rf /var/run/docker
$ sudo rm -rf /etc/docker
If desired, remove the devicemapper thin pool and reformat the block devices that were part of it.
You must delete any edited configuration files manually.

Next steps
Continue to Post-installation steps for Linux

Continue with user guides on Universal Control Plane (UCP) and Docker Trusted Registry (DTR)

requirements, installation, rhel, rpm, install, uninstall, upgrade, update



https://docs.docker.com/install/linux/linux-postinstall/

