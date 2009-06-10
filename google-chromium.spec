#
# NOTE:
# Debug build - bp: ~1,8 GB bc: ~4,1 GB
# to update sources just run in: gclient update --force
#
# TODO:
# - use shared libs to build
# - does not build on x86_64 ??
#

%define		rev	r17844

Summary:	Google browser
Summary(pl.UTF-8):	przegladarka Google
Name:		google-chromium
Version:	3.0.184.0
Release:	0.%{rev}.1
License:	Distributable
Group:		X11/Applications/Networking
Source0:	chromium-%{rev}.tar.lzma
# Source0-md5:	cab9ef0453e67daf1df3aabea571267d
#Source1:	%{name}.desktop
URL:		http://chromium.org/
BuildRequires:	GConf2-devel
BuildRequires:	gperf
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.356
Requires:	browser-plugins >= 2.0
Requires:	freetype >= 2
Provides:	wwwbrowser
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Google Chromium.

%description -l pl.UTF-8
Google Chromium.

%prep
%setup -q -T -b 0 -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_sysconfdir}}


#sh install.sh \
#	DESTDIR=$RPM_BUILD_ROOT \
#	--prefix=%{_prefix} \
#	--exec_prefix=%{_libdir}/%{name}/bin \

# install in kde etc.
#install %{SOURCE0} $RPM_BUILD_ROOT%{_desktopdir}

#install etc/* $RPM_BUILD_ROOT%{_sysconfdir}
#install usr/share/pixmaps/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/*
