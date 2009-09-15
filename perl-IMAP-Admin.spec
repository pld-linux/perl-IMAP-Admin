#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# require IMAP server access
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IMAP
%define		pnam	Admin
Summary:	IMAP::Admin - Perl module for basic IMAP server administration
Summary(pl.UTF-8):	IMAP::Admin - moduł Perla do podstawowej administracji serwerem IMAP
Name:		perl-IMAP-Admin
Version:	1.6.7
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IMAP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	86791185d394a50f4122e6139bb07279
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/IMAP-Admin/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMAP::Admin provides basic IMAP server adminstration. It provides
functions for creating and deleting mailboxes and setting various
information such as quotas and access rights.

%description -l pl.UTF-8
IMAP::Admin umożliwia podstawowe administrowanie serwerem IMAP.
Udostępnia funkcje do tworzenia i usuwania skrzynek pocztowych oraz
ustawiania różnych parametrów takich jak quota czy prawa dostępu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes examples/*
%{perl_vendorlib}/IMAP
%{_mandir}/man3/*
