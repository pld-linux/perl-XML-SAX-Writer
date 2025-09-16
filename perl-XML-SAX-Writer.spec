#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	XML
%define		pnam	SAX-Writer
Summary:	XML::SAX::Writer - SAX2 XML writer
Summary(pl.UTF-8):	XML::SAX::Writer - zapis w XML-u z SAX2
Name:		perl-XML-SAX-Writer
Version:	0.57
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3e3023c648e3003c04de2fb04435f8bd
URL:		https://metacpan.org/dist/XML-SAX-Writer
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Encode >= 2.12
BuildRequires:	perl-Test-Simple >= 0.40
BuildRequires:	perl-XML-Filter-BufferText >= 1.00
BuildRequires:	perl-XML-NamespaceSupport >= 1.00
BuildRequires:	perl-XML-SAX
# perl(XML::SAX::Exception) >= 1.01
BuildRequires:	perl-XML-SAX-Base >= 1.01
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	perl-Encode >= 2.12
Requires:	perl-XML-Filter-BufferText >= 1.00
Requires:	perl-XML-NamespaceSupport >= 1.00
Requires:	perl-XML-SAX-Base >= 1.01
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SAX::Writer Perl module - SAX2 XML Writer.

%description -l pl.UTF-8
Moduł Perla XML::SAX::Writer - zapisujący w XML-u z SAX2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README README.md
%{perl_vendorlib}/XML/SAX/Writer.pm
%{perl_vendorlib}/XML/SAX/Writer
%{_mandir}/man3/XML::SAX::Writer*.3pm*
