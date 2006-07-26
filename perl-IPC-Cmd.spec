#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	Cmd
Summary:	perl(IPC::Cmd) − finding and running system commands made easy
Name:		perl-IPC-Cmd
Version:	0.24
Release:	0.2
# "same as perl"
License:	GPLv1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9061bd187defad873432f91fa6de9f9b
URL:		http://search.cpan.org/dist/IPC-Cmd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} && %{with tests}
BuildRequires:	perl-Params-Check
BuildRequires:	perl-Module-Load-Conditional
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module IPC::Cmd allows you to run commands, interactively if desired,
platform independent but have them still work.
The "can_run" function can tell you if a certain binary is installed and if so
where, whereas the "run" function can actually execute any of the commands you
give it and give you a clear return value, as well as adhere to your verbosity
settings.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/IPC/Cmd.pm
%{_mandir}/man3/*
