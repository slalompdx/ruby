
Leverage Docker to build Ruby RPMs
==================================
These instructions are tested on Mac OSX, Yosemite and newer:

1. Make sure Docker is running (recommend the new Docker beta)
2. FIXME: Clone this repo to the ~/uproj directory, as the script relies on this location
3. Run:
```
./build6.sh
```
or
```
./build7.sh
```

Depending on building for Centos6 or Centos7.

------------------

####General steps scripted:

Install packages to build RPMs in general:

    sudo yum -y install rpmdevtools


Install libary packages:

    sudo yum -y install glibc-devel readline-devel libyaml-devel ncurses-devel gdbm-devel tcl-devel openssl-devel db4-devel libffi-devel


Install some development tools:

    sudo yum -y install make gcc unzip byacc


Create build environment for RPMs:

    mkdir -p rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
    cd rpmbuild


Get the spec file and ruby sources:

    wget https://github.com/kcrawford/ruby/raw/master/ruby.spec -O SPECS/ruby.spec
    wget https://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.3.tar.gz -O SOURCES/ruby-2.2.3.tar.gz


Build the RPM

    rpmbuild -ba SPEC/ruby.spec


Have fun with [ruby](http://ruby-lang.org/) ;-)
