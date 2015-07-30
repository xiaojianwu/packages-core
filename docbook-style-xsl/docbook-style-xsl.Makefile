BINDIR = /usr/bin
DESTDIR = ..overridden in spec file..

all: install

install: install-xsl install-img install-extensions install-misc

install-xsl:
	mkdir -p $(DESTDIR)/{common,fo,html,htmlhelp/doc,javahelp,lib,template,xhtml,manpages,profiling,highlighting,roundtrip}
	cp common/*.dtd $(DESTDIR)/common
	cp common/*.ent $(DESTDIR)/common
	cp common/*.xml $(DESTDIR)/common
	cp common/*.xsl $(DESTDIR)/common
	cp fo/*.xml $(DESTDIR)/fo
	cp fo/*.xsl $(DESTDIR)/fo
	cp html/*.xml $(DESTDIR)/html
	cp html/*.xsl $(DESTDIR)/html
	cp htmlhelp/*.xsl $(DESTDIR)/htmlhelp
	cp javahelp/*.xsl $(DESTDIR)/javahelp
	cp lib/*.xsl $(DESTDIR)/lib
	cp template/*.xsl $(DESTDIR)/template
	cp xhtml/*.xsl $(DESTDIR)/xhtml
	cp manpages/*.xsl $(DESTDIR)/manpages
	cp profiling/*.xsl $(DESTDIR)/profiling
	cp highlighting/*.xml $(DESTDIR)/highlighting
	cp highlighting/*.xsl $(DESTDIR)/highlighting
	cp roundtrip/*.xml $(DESTDIR)/roundtrip
	cp roundtrip/*.xsl $(DESTDIR)/roundtrip

install-img:
	mkdir -p $(DESTDIR)/images/callouts
	cp images/*.gif $(DESTDIR)/images
	cp images/*.png $(DESTDIR)/images
	cp images/callouts/*.png $(DESTDIR)/images/callouts

install-extensions:
	mkdir -p $(DESTDIR)/extensions
	cp -r extensions/* $(DESTDIR)/extensions

install-misc:
	cp VERSION $(DESTDIR)
