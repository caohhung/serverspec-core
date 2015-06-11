%global install_dir /opt/gdc/serverspec-core

Name:             serverspec-core
Summary:          GoodData ServerSpec integration
Version:          1.0
Release:          2.gdc

Vendor:           GoodData
Group:            GoodData/Tools

License:          Gooddata proprietary
URL:              https://github.com/gooddata/serverspec-core
Source0:          sources.tar
BuildArch:        noarch
BuildRoot:        %{_tmppath}/%{name}-%{version}-root

Requires:         ruby193-rubygem-rake
Requires:         ruby193-rubygem-serverspec
Requires:         ruby193-rubygem-colorize
Requires:         ruby193-rubygem-parseconfig

%prep
%setup -q -c

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{install_dir}
cp -a * $RPM_BUILD_ROOT%{install_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%description
GoodData ServerSpec integration - core package

%files
%attr(0755, root, root) %dir %{install_dir}
%attr(0755, root, root) %dir %{install_dir}/cfg
%attr(0755, root, root) %dir %{install_dir}/spec
%attr(0755, root, root) %{install_dir}/spec/types
%attr(0755, root, root) %{install_dir}/cfg/cfg_helper.rb
%attr(0755, root, root) %{install_dir}/check_last_run.sh
%attr(0755, root, root) %{install_dir}/cron_run.sh
%attr(0755, root, root) %{install_dir}/Rakefile
%attr(0755, root, root) %{install_dir}/serverspec-core.spec
%attr(0755, root, root) %{install_dir}/spec/spec_helper.rb
%attr(0755, root, root) %doc %{install_dir}/*.md
%exclude %{install_dir}/Gemfile*
%exclude %{install_dir}/Makefile
%exclude %{install_dir}/makemeusable


%changelog
* Wed Jun 10 2015 Yury Tsarev <yury.tsarev@gooddata.com> 1.0-2.gdc
- Fix versioning and file inclusion
* Tue Jun 09 2015 Martin Surovcak <martin.surovcak@gooddata.com> 1.0-1.gdc
- Initial rpmbuild
