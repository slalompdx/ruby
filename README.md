RPM spec file to build a ruby package
=====================================

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

    wget https://github.com/innotronic/ruby/raw/master/ruby.spec -O SPECS/ruby.spec
    wget https://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.3.tar.gz -O SOURCES/ruby-2.2.3.tar.gz


Build the RPM

    rpmbuild -ba SPEC/ruby.spec


Have fun with [ruby](http://ruby-lang.org/) ;-)
