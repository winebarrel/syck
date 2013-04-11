Name:		syck-ruby200
Version:	1.0.0
Release:	1%{?dist}
Summary:	A gemified version of Syck from Ruby’s stdlib.

Group:		Development/Libraries
License:	MIT
URL:		https://github.com/tenderlove/syck
# https://github.com/tenderlove/syck/tarball/v1.0.0
Source0:	syck-1.0.0.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
A gemified version of Syck from Ruby’s stdlib. Syck has been removed from Ruby’s stdlib, and this gem is meant to bridge the gap for people that haven’t updated their YAML yet.

%prep
%setup -q -n tenderlove-syck-cf3290a

%build
cd ext/syck
ruby extconf.rb
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -D -m 0644 lib/syck.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck.rb
install -D -m 0644 lib/syck/baseemitter.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/baseemitter.rb
install -D -m 0644 lib/syck/basenode.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/basenode.rb
install -D -m 0644 lib/syck/constants.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/constants.rb
install -D -m 0644 lib/syck/encoding.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/encoding.rb
install -D -m 0644 lib/syck/error.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/error.rb
install -D -m 0644 lib/syck/loader.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/loader.rb
install -D -m 0644 lib/syck/rubytypes.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/rubytypes.rb
install -D -m 0644 lib/syck/stream.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/stream.rb
install -D -m 0644 lib/syck/stringio.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/stringio.rb
install -D -m 0644 lib/syck/syck.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/syck.rb
install -D -m 0644 lib/syck/tag.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/tag.rb
install -D -m 0644 lib/syck/types.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/types.rb
install -D -m 0644 lib/syck/yamlnode.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/yamlnode.rb
install -D -m 0644 lib/syck/ypath.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/syck/ypath.rb
install -D -m 0644 lib/yaml/syck.rb %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/yaml/syck.rb
install -D -m 0644 ext/syck/syck.so %{buildroot}%{_libdir}/ruby/vendor_ruby/2.0.0/%{_arch}-%{_os}/syck.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/ruby/vendor_ruby/2.0.0/syck.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/baseemitter.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/basenode.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/constants.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/encoding.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/error.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/loader.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/rubytypes.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/stream.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/stringio.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/syck.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/tag.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/types.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/yamlnode.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/syck/ypath.rb
%{_libdir}/ruby/vendor_ruby/2.0.0/x86_64-linux/syck.so
%{_libdir}/ruby/vendor_ruby/2.0.0/yaml/syck.rb
