%bcond_with apps
%bcond_without doc
%bcond_without scribo

Summary:	Olena is a platform dedicated to image processing
Name:		olena
Version:	2.0
Release:	5
Epoch:		2
License:	GPLv2+
Group:		Development/C++
Url:		https://www.lrde.epita.fr/cgi-bin/twiki/view/Olena/WebHome
# Get from https://svn.lrde.epita.fr/svn/oln/tags/olena-1.0 to have scribo
Source0:	%{name}-%{version}.tar.bz2
Patch0:		olena-1.0-subdirs.patch
Patch1:		olena-1.0-linkage.patch
Patch2:		olena-2.0-tesseract-3.01.patch
Patch3:		olena-2.0-gcc4.7.patch
Patch4:		olena-2.0-automake1.13.patch
BuildRequires:	doxygen
BuildRequires:	imagemagick
BuildRequires:	latex2html
BuildRequires:	texlive-latex
BuildRequires:	texlive-dvips
#BuildRequires:	vtk-devel
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(libtiff-4)
%if %{with scribo}
BuildRequires:	pkgconfig(tesseract)
%endif
BuildRequires:	pkgconfig(xmu)

%description
Olena is a platform dedicated to image processing. At the
moment it is mainly composed of a C++ library: Milena. This library features
many tools to easily perform image processing tasks. Its main characteristic is
its genericity: it allows to write an algorithm once and run it over many kinds
of images (grey scale, color, 1D, 2D, 3D, ...).

#------------------------------------------------------------------------------

%if %{with doc}
%package doc
Summary:	Olena documentation
Group:		Books/Howtos

%description doc
This is the documentation for Olena.
Olena is a platform dedicated to image processing. At the
moment it is mainly composed of a C++ library: Milena. This library features
many tools to easily perform image processing tasks. Its main characteristic is
its genericity: it allows to write an algorithm once and run it over many kinds
of images (grey scale, color, 1D, 2D, 3D, ...).

%files doc
%{_docdir}/olena
%endif

#------------------------------------------------------------------------------

%package tools
Summary:	Olena tools
Group:		Development/C++

%description tools
Olena is a platform dedicated to image processing. At the
moment it is mainly composed of a C++ library: Milena. This library features
many tools to easily perform image processing tasks. Its main characteristic is
its genericity: it allows to write an algorithm once and run it over many kinds
of images (grey scale, color, 1D, 2D, 3D, ...).

%files tools
%{_bindir}/*
%{_datadir}/olena
%if %{with scribo}
%{_libdir}/scribo/*
%endif

#------------------------------------------------------------------------------

%define gluit_major 0
%define libgluit %mklibname gluit %{gluit_major}

%package -n %{libgluit}
Summary:	Gluit C++ main Olena library
Group:		Development/C++

%description -n %{libgluit}
Gluit C++ main Olena library.

%files -n %{libgluit}
%{_libdir}/libgluit.so.%{gluit_major}*

#------------------------------------------------------------------------------

%define tri_major 0
%define libtrimesh %mklibname trimesh %{tri_major}

%package -n %{libtrimesh}
Summary:	trimesh C++ main Olena library
Group:		Development/C++

%description -n %{libtrimesh}
trimesh C++ main Olena library.

%files -n %{libtrimesh}
%{_libdir}/libtrimesh.so.%{tri_major}*

#------------------------------------------------------------------------------

%package devel
Summary:	Olena devel files
Group:		Development/C++
Requires:	%{libtrimesh} = %{EVRD}
Requires:	%{libgluit} = %{EVRD}
Requires:	olena-tools

%description devel
Olena devel files
Olena is a platform dedicated to image processing. At the
moment it is mainly composed of a C++ library: Milena. This library features
many tools to easily perform image processing tasks. Its main characteristic is
its genericity: it allows to write an algorithm once and run it over many kinds
of images (grey scale, color, 1D, 2D, 3D, ...).

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/*.a

#------------------------------------------------------------------------------

%prep
%setup -q
%patch1 -p0
%patch2
%patch3 -p1
%patch4 -p1
%if ! %{with doc}
%patch0 -p0 -b .orig
%endif

%build
%global optflags %{optflags} -fpermissive
autoreconf -fi
pushd external/trimesh
autoreconf -fi
popd
%configure2_5x \
%if %{with scribo}
	--enable-scribo \
%endif
	--enable-trimesh \
%if %{with apps}
	--enable-apps \
%endif
	--enable-tools

pushd external/trimesh
%configure2_5x
popd

%make

%install
%makeinstall_std

