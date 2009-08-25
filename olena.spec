%bcond_with apps

Name: olena
Version: 1.0
Release: %mkrel 1
License: GPLv2
Summary: Olena is a platform dedicated to image processing
Group: Development/C++
URL: http://www.lrde.epita.fr/cgi-bin/twiki/view/Olena/WebHome
Source0:  %name-%version.tar.bz2
Patch0: olena-1.0-undefined-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: cfitsio-devel
BuildRequires: tiff-devel
BuildRequires: imagemagick-devel
BuildRequires: mesaglut-devel
BuildRequires: mesagl-devel

%description
Olena is a platform dedicated to image processing. At the moment it is mainly
composed of a C++ library: Milena. This library features many tools to easily
perform image processing tasks. Its main characteristic is its genericity: it
allows to write an algorithm once and run it over many kinds of images (grey
scale, color, 1D, 2D, 3D, ...). We do our image processing research using this
library, but most importantly we have gathered (and still do) generic
programming expertise from the library development.

#------------------------------------------------------------------------------

%package doc
Summary: Olena documentation
Group: Books/Howtos

%description doc
Olena documentation.

%files doc
%defattr(-,root,root,-)
%_datadir/olena/images
%_docdir/olena

#------------------------------------------------------------------------------

%package tools
Summary: Olena tools
Group: Development/C++

%description tools
Olena tools.

%files tools
%defattr(-,root,root,-)
%_bindir/*

#------------------------------------------------------------------------------

%define gluit_major 0
%define libgluit %mklibname gluit %{gluit_major}

%package -n %{libgluit}
Summary: Gluit C++ main Olena library
Group: Development/C++

%description -n %{libgluit}
Gluit C++ main Olena library.

%files -n %{libgluit}
%_libdir/libgluit.so.%{gluit_major}*

#------------------------------------------------------------------------------

%define tri_major 0
%define libtrimesh %mklibname trimesh %{tri_major}

%package -n %{libtrimesh}
Summary: trimesh C++ main Olena library
Group: Development/C++

%description -n %{libtrimesh}
trimesh C++ main Olena library.

%files -n %{libtrimesh}
%defattr(-,root,root,-)
%{_libdir}/libtrimesh.so.%{tri_major}*

#------------------------------------------------------------------------------

%package devel
Summary: Olena devel files
Group: Development/C++
Requires: %{libtrimesh} = %{version}
Requires: %{libgluit} = %{version}
Requires: olena-tools

%description devel
Olena devel files

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%exclude %_libdir/*.a

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .orig

%build
CXXFLAGS="$CXXFLAGS -I%{_includedir}/ImageMagick"

export CPPFLAGS CXXFLAGS

%configure2_5x \
	--enable-trimesh \
%if %with apps
	--enable-apps \
%endif
	--enable-tools

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %buildroot

