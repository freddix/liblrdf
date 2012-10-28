Summary:	Library to manipulate RDF files describing LADSPA plugins
Name:		liblrdf
Version:	0.5.0
Release:	2
License:	GPL
Group:		Libraries
#Source0:	https://github.com/swh/LRDF/tarball/%{version}
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	005ea24152620da7f2ee80a78e17f784
URL:		https://github.com/swh/LRDF
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	raptor2-devel
BuildRequires:	libtool
BuildRequires:	ladspa-devel
BuildRequires:	pkg-config
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library to make it easy to manipulate RDF files describing
LADSPA plugins. It can also be used for general RDF manipulation. It
can read RDF/XML and N3 files and export N3 files.

%package devel
Summary:	liblrdf header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
liblrdf library header files.

%prep
# github creates b0rked tarballs
%setup -qn swh-LRDF-7ebc032

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/ladspa/rdf/ladspa.rdfs

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

