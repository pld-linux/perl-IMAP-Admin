%include	/usr/lib/rpm/macros.perl
Summary:	IMAP-Admin perl module
Summary(pl):	Modu� perla IMAP-Admin
Name:		perl-IMAP-Admin
Version:	1.6.0
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IMAP/IMAP-Admin-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMAP-Admin provides basic IMAP server adminstration. It provides
functions for creating and deleting mailboxes and setting various
information such as quotas and access rights.

%description -l pl
IMAP-Admin umo�liwia podstawowe administrowanie serwerem IMAP.
Udost�pnia funkcje do tworzenia i usuwania skrzynek pocztowych oraz
ustawiania r�nych parametr�w takich jak quota czy prawa dost�pu.

%prep
%setup -q -n IMAP-Admin-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples/*
%{perl_sitelib}/IMAP/Admin.pm
%{_mandir}/man3/*
