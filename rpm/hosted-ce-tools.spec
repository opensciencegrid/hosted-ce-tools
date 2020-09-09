%global debug_package %{nil}
Summary: Tools for managing OSG Hosted CEs
Name: hosted-ce-tools
Version: 0.8
Release: 2%{?dist}
License: Apache 2.0
Url: https://github.com/opensciencegrid/hosted-ce-tools
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
%if 0%{?rhel} >= 8
Requires: python2-six
%else
Requires: python-six
%endif
Requires: fetch-crl
Requires: sudo
Requires: wget
Requires: /usr/bin/git
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
systemctl daemon-reload


%preun
%systemd_preun update-all-remote-wn-clients.service update-all-remote-wn-clients.timer


%changelog
* Wed Sep 09 2020 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.8-2
- Fix python-six dependency for EL8

* Wed Sep 09 2020 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.8-1
- Download osg-ca-manage from GitHub instead of using a tarball client for fetching CAs (SOFTWARE-4242)

* Tue May 05 2020 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.7-1
- Fix bug in timeout where sudo would prompt the user for a password (SOFTWARE-4081)

* Thu Apr 30 2020 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.6-1
- Have update-all-remote-wn-ce run updaters with a timeout (SOFTWARE-4081)
- If one update fails, keep going with the other updates instead of bailing out

* Fri Dec 20 2019 Mátyás Selmeci <matyas@cs.wisc.edu> - 0.5-2
- Require sudo (SOFTWARE-3954)

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
