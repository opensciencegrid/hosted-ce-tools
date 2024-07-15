VERSION = 2.1
NAME=hosted-ce-tools
NAME_VERSION=$(NAME)-$(VERSION)
HASH = $(shell git rev-parse HEAD)

_default:
	@echo "Nothing to make. Try make install or make install-noconfig"

install: install-noconfig
	mkdir -p $(DESTDIR)/etc

install-noconfig:
	mkdir -p $(DESTDIR)/usr/bin
	install -p -m 755 scripts/cvmfsexec-osg-wrapper scripts/make-cvmfsexec-tarball $(DESTDIR)/usr/bin/

testsource:
	mkdir -p upstream
	echo "type=git url=. name=$(NAME) tag=HEAD tarball=$(NAME_VERSION).tar.gz hash=$(HASH)" > upstream/test.source

rpmbuild: testsource
	osg-build rpmbuild

kojiscratch: testsource
	osg-build koji --scratch --getfiles


.PHONY: _default install-noconfig install testsource rpmbuild kojiscratch

