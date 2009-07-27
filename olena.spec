Name:           olena
Version:        1.0
Summary:        Platform dedicated to image processing
Release:        %mkrel 1
License:        GPL
Group:          Graphical desktop/KDE
URL:            http://www.lrde.epita.fr/cgi-bin/twiki/view/Olena/Olena100
Source0:        http://www.lrde.epita.fr/dload/olena/%version/%name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-%version-%release-buildroot

%description
Olena is a platform dedicated to image processing. 
At the moment it is mainly composed of a C++ library: 
Milena. 
This library features many tools to easily perform image 
processing tasks. Its main characteristic is its genericity: 
it allows to write an algorithm once and run it over many 
kinds of images (grey scale, color, 1D, 2D, 3D, ...). We do 
our image processing research using this library, but most 
importantly we have gathered (and still do) generic programming 
expertise from the library development. 

%files
%defattr(-,root,root)
%_bindir/*
%_datadir/olena
%_docdir/olena

#-----------------------------------------------------------------------------

%package   devel
Summary:   Devel stuff for %name
Group:     Development/KDE and Qt

%description  devel
This package contains header files needed if you wish to build applications
based on %name.

%files devel
%defattr(-,root,root)
%_includedir/mln

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --enable-apps  --enable-tools

%make


%install
rm -rf %buildroot
%makeinstall_std
%clean
rm -rf %{buildroot}

