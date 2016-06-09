wget::fetch { 'Download el6 spec file':
  source => "https://github.com/slalompdx/ruby/raw/master/ruby-el6.spec",
  destination => '/rpmbuild/SPECS/ruby-el6.spec',
} ->

wget::fetch { 'Download el7 spec file':
  source => "https://github.com/slalompdx/ruby/raw/master/ruby-el7.spec",
  destination => '/rpmbuild/SPECS/ruby-el7.spec',
} ->

wget::fetch { 'Download Ruby bundle':
  source => 'https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz',
  destination => '/rpmbuild/SOURCES/ruby-2.3.1.tar.gz',
}
