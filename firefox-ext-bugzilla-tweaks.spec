Summary: Bugzilla extension for firefox
Name: firefox-ext-bugzilla-tweaks
Version: 1.6
Release: %mkrel 3
License: MPL
Group:	Networking/WWW
URL:	https://addons.mozilla.org/en-US/firefox/addon/187588/
Source: http://releases.mozilla.org/pub/mozilla.org/addons/187588/bugzilla_tweaks-%{version}-fx-fn-tb.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox >= %{firefox_epoch}:%{firefox_version}
BuildArch: noarch
BuildRequires: firefox-devel

%description
This extension modifies the pages loaded from bugzilla.mozilla.org and adds features including:
- Interleaving the bug's change history with the comments on the same page
- Showing the last time that a bug or attachment flag was changed
- Proving user name autocompletion support
- And many more...

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}
