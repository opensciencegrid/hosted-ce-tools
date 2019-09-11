%global debug_package %{nil}
Summary: Tools for managing OSG Hosted CEs
Name: hosted-ce-tools
Version: 0.3
Release: 1%{?dist}
License: Apache 2.0
Url: https://github.com/opensciencegrid/hosted-ce-tools
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: python-six
Requires: fetch-crl
%systemd_requires


%description
%{summary}


%prep
%setup -q


%build
exit 0


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/update-remote-wn-client
%{_bindir}/update-all-remote-wn-clients
%config(noreplace) %{_sysconfdir}/hosted-ces.ini
%{_unitdir}/update-all-remote-wn-clients.service
%{_unitdir}/update-all-remote-wn-clients.timer
%dir /var/log/updatewn


%post
%systemd_post update-all-remote-wn-clients.service update-all-remote-wn-clients.timer


%preun
%systemd_preun update-all-remote-wn-clients.service update-all-remote-wn-clients.timer


%changelog
* Wed Sep 11 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.3-1
- Use system fetch-crl

* Tue Sep 10 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.2-1
- Fixes

* Tue Sep 10 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-3
- Add systemd timer and service

* Fri Sep 06 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-2
- update-all-remote-wn-clients script and associated config file and log dir

* Thu Sep 05 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-1
- Initial


# vim:ft=spec
