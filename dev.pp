class { '::wget': }
$orig_packageset =
  [
    'rpmdevtools',
    'glibc-devel',
    'readline-devel',
    'libyaml-devel',
    'ncurses-devel',
    'gdbm-devel',
    'tcl-devel',
    'openssl-devel',
    'libffi-devel',
    'make',
    'gcc',
    'unzip',
    'byacc'
  ]
$homedir = '/vagrant'
$package_root = 'ruby2'
$version = '2.3.1'
$release = '1'

if $facts['os']['release']['major'] == '7' {
  $packageset = $orig_packageset + 'compat-db47'
  $packagevar = "${facts['os']['release']['major']}.centos.x86_64"
} else {
  $packageset = $orig_packageset + 'db4-devel'
  $packagevar = "${facts['os']['release']['major']}.x86_64"
}

$packagename = "${homedir}/rpmbuild/RPMS/x86_64/${package_root}-${version}-${release}.el${packagevar}.rpm"

package { $packageset: }
