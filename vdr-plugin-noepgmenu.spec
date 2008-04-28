
%define plugin	noepgmenu
%define name	vdr-plugin-%plugin
%define version	0.0.5
%define rel	2

Summary:	VDR plugin: a menu for noEPG patch
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://winni.vdr-developer.org/noepgmenu/
Source:		http://winni.vdr-developer.org/noepgmenu/download/vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
A simple OSD to manage the channels for the noEPG patch.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


