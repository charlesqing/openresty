Name:           perl-Test-Nginx
Version:        0.25
Release:        7%{?dist}
Summary:        Data-driven test scaffold for Nginx C module and Nginx/OpenResty-based libraries and applications
License:        BSD
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Nginx/
Source0:        http://www.cpan.org/authors/id/A/AG/AGENT/Test-Nginx-%{version}.tar.gz
Patch0:         Test-Nginx-0.25-older_perl.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.8.1
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(CPAN)

%if 0%{?rhl}
BuildRequires:  epel-release
Requires:       epel-release
%endif

Requires:       perl(Encode)
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(File::Path)
Requires:       perl(File::Temp)
Requires:       perl(Filter::Util::Call)
Requires:       perl(HTTP::Response)
Requires:       perl(List::MoreUtils)
Requires:       perl(List::Util)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Test::Base)
Requires:       perl(Test::LongString)
Requires:       perl(Text::Diff)
Requires:       perl(Time::HiRes)
Requires:       perl(URI::Escape)
#Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This distribution provides two testing modules for Nginx C module
development:

%prep
%setup -q -n Test-Nginx-%{version}

%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Oct 13 2016 Yichun Zhang (agentzh) <agentzh@gmail.com> 0.25-7
- No longer require a particular perl version.
* Thu Oct 13 2016 Yichun Zhang (agentzh) <agentzh@gmail.com> 0.25-6
- Improve the dependency list.
* Tue Jul 12 2016 Yichun Zhang (agentzh) <agentzh@gmail.com> 0.25-1
- Specfile autogenerated by cpanspec 1.78.
