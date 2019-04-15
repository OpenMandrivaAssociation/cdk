%define debug_package %{nil}
%define date 20190303
%define major 5
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Curses Development Kit
Name:		cdk
Version:	5.0
Release:	0.%{date}.1
License:	BSD
Group:		System/Libraries
Url:		http://invisible-island.net/cdk/
Source0:	ftp://invisible-island.net/cdk/cdk-%{version}-%{date}.tgz
Patch0:		cdk-5.0-20150928-do-not-hardcode-gcc.patch
BuildRequires:	pkgconfig(ncurses)

%description
Cdk stands for 'Curses Development Kit' and it currently contains 21 ready
to use widgets which facilitate the speedy development of full screen
curses programs.

%package -n %{libname}
Summary:	CDK library
Group:		Development/C

%description -n %{libname}
This the cdk library for developing cdk-based applications.

%package -n %{develname}
Summary:	Headers to develop cdk-based applications
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}

%description -n %{develname}
These are the header files, and cdk preprocessor for developing
cdk-based applications.

%prep
%autosetup -n %{name}-%{version}-%{date} -p1

perl -pi -e '/^LIB_DIR/ and s,/lib\b,/%{_lib},' Makefile.in

%build
# (tpg) fix for llvm-ar
sed -i -e "s/\${AR} -cr/\${AR} cr/g" aclocal.m4 configure

export CFLAGS="%{optflags} -fPIC"
%configure \
        --with-ncurses \
        --enable-const \
        --disable-rpath-hack

%make_build cdkshlib

%install
%make_install installCDKSHLibrary INSTALL="install -pD"

# fixes rpmlint unstripped-binary-or-object
chmod +x %{buildroot}%{_libdir}/*.so*
# delete static libs
find %{buildroot} -name '*.a' -delete -print
# delete wrongly installed docs
rm -rf %{buildroot}%{_docdir}/%{name}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README TODO NOTES EXPANDING
%{_includedir}/cdk.h
%dir %{_includedir}/%{name}
%attr(644,root,root) %{_includedir}/%{name}/*
%{_bindir}/cdk5-config
%{_libdir}/*.so
%{_mandir}/man3/*
%{_mandir}/man1/*
