%global debug_package %{nil}
Summary: Tools for managing OSG Hosted CEs
Name: hosted-ce-tools
Version: 0.5
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
%config(noreplace) %{_sysconfdir}/endpoints.ini
%{_unitdir}/update-all-remote-wn-clients.service
%{_unitdir}/update-all-remote-wn-clients.timer
%dir /var/log/update-remote-wn-client


%post
%systemd_post update-all-remote-wn-clients.service update-all-remote-wn-clients.timer


%preun
%systemd_preun update-all-remote-wn-clients.service update-all-remote-wn-clients.timer


%changelog
* Wed Nov 13 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.5-1
- Don't run updaters in parallel (PR #1)

* Tue Sep 17 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.4-1
- Add --dry-run option to update-all-remote-wn-clients script
- Allow more characters in endpoint names in endpoints.ini

* Wed Sep 11 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.3-1
- Use system fetch-crl
- Change config file name and log directory name

* Tue Sep 10 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.2-1
- Fixes

* Tue Sep 10 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-3
- Add systemd timer and service

* Fri Sep 06 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-2
- update-all-remote-wn-clients script and associated config file and log dir

* Thu Sep 05 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.1-1
- Initial


# vim:ft=spec
