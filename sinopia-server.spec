Name:		sinopia-server
Version:	1.4.0
Release:	1%{?dist}
Summary:	A private/caching npm repository server

Group:		unknown
License:	BSD
URL:		https://github.com/rlidwka/sinopia
Source0:	config.yaml
Source1:	sinopia.init
Source2:	sinopia.config

BuildArch:	noarch
Requires:	nodejs-sinopia = 1.4.0
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd


%description
Sinopia is a private/caching npm repository server. This package provides
scripts and default configurations to run sinopia as a system service.


%install
rm -rf %{buildroot}
install -D -m 0644 %{_sourcedir}/config.yaml %{buildroot}%{_sysconfdir}/sinopia/config.yaml
install -D -m 0644 %{_sourcedir}/sinopia.config %{buildroot}%{_sysconfdir}/sysconfig/sinopia
install -D -m 0755 %{_sourcedir}/sinopia.init %{buildroot}%{_sysconfdir}/rc.d/init.d/sinopia
mkdir -p %{buildroot}%{_localstatedir}/log/sinopia
mkdir -p %{buildroot}%{_localstatedir}/run/sinopia


%files
%{_sysconfdir}/sinopia/config.yaml
%{_sysconfdir}/rc.d/init.d/sinopia
%config(noreplace) %{_sysconfdir}/sinopia/config.yaml
%config(noreplace) %{_sysconfdir}/sysconfig/sinopia
%attr(0755,sinopia,sinopia) %dir %{_localstatedir}/log/sinopia
%attr(0755,sinopia,sinopia) %dir %{_localstatedir}/run/sinopia


%pre
/usr/sbin/groupadd -r sinopia || :
/usr/sbin/useradd -r -N -m -d %{_localstatedir}/lib/sinopia -s /sbin/nologin sinopia || :


%changelog
* Fri Sep 11 2015 Jim Sheldon <jim.sheldon@meltwater.com> - 1:1.4.0-1
- Initial sinopia-server spec for 1.4.0

