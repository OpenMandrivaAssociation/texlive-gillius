# revision 32068
# category Package
# catalog-ctan /fonts/gillius
# catalog-date 2013-11-04 00:06:06 +0100
# catalog-license gpl2
# catalog-version undef
Name:		texlive-gillius
Version:	20131104
Release:	9
Summary:	Gillius fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/gillius
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gillius.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gillius.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Gillius and Gillius No. 2 families of sans
serif fonts and condensed versions of them, designed by Hirwen
Harendal. According to the designer, the fonts were inspired by
Gill Sans.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_4bsedw.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_a6mi7n.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_az7pev.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_bg5e7z.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_efuo7w.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_lf6eoq.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_pqq4vh.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_shb4ap.enc
%{_texmfdistdir}/fonts/map/dvips/gillius/gillius.map
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADF-Bold.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADF-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADF-Italic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADF-Regular.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFCond-Bold.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFCond-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFCond-Italic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFCond-Regular.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2-Bold.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2-Italic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2-Regular.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2Cond-Bold.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2Cond-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2Cond-Italic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2Cond-Regular.otf
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-Bold.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-BoldItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-BoldLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-Italic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-ItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-Regular.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-RegularLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-Bold.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-BoldItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-BoldLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-Italic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-ItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-Regular.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-RegularLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-Bold.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-BoldItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-BoldLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-Italic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-ItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-Regular.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-RegularLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-Bold.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-BoldItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-BoldLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-Italic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-ItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-Regular.pfb
%{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-RegularLCDFJ.pfb
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ts1.vf
%{_texmfdistdir}/tex/latex/gillius/LY1GilliusADF-LF.fd
%{_texmfdistdir}/tex/latex/gillius/LY1GilliusADFCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/LY1GilliusADFNoTwo-LF.fd
%{_texmfdistdir}/tex/latex/gillius/LY1GilliusADFNoTwoCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/OT1GilliusADF-LF.fd
%{_texmfdistdir}/tex/latex/gillius/OT1GilliusADFCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/OT1GilliusADFNoTwo-LF.fd
%{_texmfdistdir}/tex/latex/gillius/OT1GilliusADFNoTwoCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/T1GilliusADF-LF.fd
%{_texmfdistdir}/tex/latex/gillius/T1GilliusADFCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/T1GilliusADFNoTwo-LF.fd
%{_texmfdistdir}/tex/latex/gillius/T1GilliusADFNoTwoCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/TS1GilliusADF-LF.fd
%{_texmfdistdir}/tex/latex/gillius/TS1GilliusADFCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/TS1GilliusADFNoTwo-LF.fd
%{_texmfdistdir}/tex/latex/gillius/TS1GilliusADFNoTwoCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/gillius.sty
%{_texmfdistdir}/tex/latex/gillius/gillius2.sty
%doc %{_texmfdistdir}/doc/fonts/gillius/COPYING
%doc %{_texmfdistdir}/doc/fonts/gillius/Gillius-cat.pdf
%doc %{_texmfdistdir}/doc/fonts/gillius/README
%doc %{_texmfdistdir}/doc/fonts/gillius/gillius-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/gillius/gillius-samples.tex
%doc %{_texmfdistdir}/doc/fonts/gillius/gillius2-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/gillius/gillius2-samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
