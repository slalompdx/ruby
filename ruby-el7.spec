#
# ruby.spec
#

%define rubyver         %{?override_rubyver}%{?!override_rubyver:2.3.1}
%define _prefix /usr/local

Name:           ruby2
Version:        %{rubyver}
Release:        1%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel compat-db47 byacc make libffi-devel
Requires:       libyaml openssl
Source0:        https://cache.ruby-lang.org/pub/ruby/2.2/ruby-%{rubyver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Prefix: /usr/local

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
export LDFLAGS="-Wl,-rpath,/usr/local/lib64/"

%configure \
  --enable-shared \
  --disable-rpath \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_includedir}
%{_datadir}
%{_libdir}

%changelog
* Tue Aug 19 2015 Innotronic Ingenieurbüro GmbH <info@inno.ch> - 2.2.3
- Update to 2.2.3
* Tue Aug 18 2015 Tanner Jones <tannerjones10@gmail.com> - 2.2.2
- Update to 2.2.2
* Sat Jul 25 2015 Innotronic Ingenieurbüro GmbH <info@inno.ch> - 2.1.6
- Update to 2.1.6
* Sat Nov 29 2014 Innotronic Ingenieurbüro GmbH <info@inno.ch> - 2.1.5
- Update to 2.1.5
* Fri Apr 25 2014 Spike Grobstein <sgrobstein@shutterstock.com> - 2.1.1
- Bumps 2.1.1
* Wed Dec 25 2013 Nathan Milford <nathan@milford.io> - 2.1.0
- Bumped 2.1.0
* Wed Dec 18 2013 Nathan Milford <nathan@milford.io> - 2.0.0-p353
- Bumped 2.0.0-p353.
* Fri Jun 28 2013 Nathan Milford <nathan@milford.io> - 2.0.0-p247
- Bumped 2.0.0-p247.
* Sun Feb 24 2013 Nathan Milford <nathan@milford.io> - 2.0.0-p0
- Initial 2.0.0-p0 for realz.
* Mon Jan 7 2013 Nathan Milford <nathan@milford.io> - 2.0.0-rc1
- Initial 2.0.0 release candidate.
* Sun Nov 25 2012 Gareth Jones <me@gazj.co.uk> - 1.9.3-p327
- Update for Ruby 1.9.3-p327 release.
* Wed Apr 25 2012 mathew <meta@pobox.com> - 1.9.3-p194-1
- Update for Ruby 1.9.3-p194 release.
* Sat Feb 24 2012 Ian Meyer <ianmmeyer@gmail.com> - 1.9.3-p125-1
- Spec to replace system ruby with 1.9.3-p125
