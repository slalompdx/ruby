ln -s /opt/puppetlabs/bin/puppet /usr/bin/puppet
puppet module install maestrodev-wget
puppet apply -v /vagrant/ruby.pp
/usr/bin/rpmbuild -ba --define "_topdir /vagrant/rpmbuild" /vagrant/rpmbuild/SPECS/ruby.spec
