%global commit0 bbbd44769de9f3ad48fba6f7905a58ed9a41182b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global checkout 20150729git%{shortcommit0}
%global vendor composer
%global project satis

Name:           php-%{vendor}-%{project}
Version:        1.0.0dev
Release:        1.%{checkout}%{?dist}
Summary:        Simple Repository Generator

Group:          Development/Tools
License:        MIT
URL:            https://github.com/%{vendor}/%{project}
Source0:        https://github.com/%{vendor}/%{project}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# Generated by Composer. First install Composer see: https://getcomposer.org/download/
# Then run 'composer.phar install --no-dev --optimize-autoloader' to generate the directory 'vendor'.
# Finally package the 'vendor directory'.
Source1:        %{name}-%{shortcommit0}-vendor.tar.gz
# A patch for the 'compile' command, so that we can provide the destination of the phar file.
Patch0:         %{name}-%{shortcommit0}-compile.patch

BuildArch:      noarch

BuildRequires:  php-cli >= 5.3.2
Requires:       php-cli >= 5.3.2

Provides:       php-composer(%{vendor}/%{project}) = %{version}

%description
Simple static Composer repository generator.
It uses any composer.json file as input and dumps all the required (according
to their version constraints) packages to a Composer Repository file.


%prep
%setup -q -n %{project}-%{commit0}
%setup -q -n %{project}-%{commit0} -a 1
%patch0 -p 0


%build
%{__mkdir} %{_builddir}/%{project}-%{commit0}/build
php -d phar.readonly=0 bin/compile %{_builddir}/%{project}-%{commit0}/build/satis.phar


%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
%{__cp} -a build/satis.phar %{buildroot}%{_bindir}/satis


%clean
rm -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%doc README.md LICENSE
%attr(0755, -, -) %{_bindir}/satis


%changelog
* Wed Jul 29 2015 Hugo Stijns <hugo@boosboos.net> - 1.0.0dev-1.20150729gitbbbd447
- Initial version.
