Name:		texlive-br-lex
Version:	44939
Release:	1
Summary:	A Class for Typesetting Brazilian legal texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/br-lex
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/br-lex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/br-lex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class implements rules to typeset Brazilian legal texts.
Its purpose is to be an easy-to-use implementation for the
end-user.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/br-lex
%doc %{_texmfdistdir}/doc/latex/br-lex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
