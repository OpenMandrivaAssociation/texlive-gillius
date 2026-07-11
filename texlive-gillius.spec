%global tl_name gillius
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Gillius fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gillius
License:	gpl2+ lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gillius.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gillius.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Gillius and Gillius No. 2 families of sans serif fonts and condensed
versions of them, designed by Hirwen Harendal. According to the
designer, the fonts were inspired by Gill Sans.

