
# DSpace XMLUI Language Packs

## Layout of the source tree

The `messages.xml` files for each language are stored in the `src/main/webapp/i18n/` directory.

The file naming conventions are as follows:

`messages_<ISO 639-1>_<ISO 3166-1>.xml`

* `ISO 639-1`: language code, in lower case.
* `ISO 3166-1`: codes for country, if required.  For example:

For example:
* `src/main/webapp/i18n/`
    * `messages.xml` - file for default (English)
    * `messages_el.xml` - file for Greek
    * `messages_fr_FR.xml` - file for French (France)
    * `messages_fr_CA.xml` - file for French (Canada)

More information on the format of these `messages.xml` files can be found in the Apache Cocoon documentation at https://cocoon.apache.org/2.1/userdocs/i18nTransformer.html


## Release tags

Language packs are versioned according to the main DSpace version, but also include an incrementing `sequence-number` which allows language packs to be updated more frequently than DSpace releases.

So, DSpace software releases are of the format: `[major].[minor]` (e.g. 4.0, 4.1, 5.0, 5.1, etc.)

Whereas, DSpace language packs use the format: `[major].[minor].[sequence-number]` (e.g. 5.0.0, 5.0.1, 5.0.2 for 5.0 releases of the language packs).

Language packs are automatically installed into DSpace via Maven dependencies. In the case of the XMLUI language packs, they are installed as a WAR (e.g. `dspace-xmlui-lang-[version].war`) dependency.

## Documentation

Additional documentation on language packs and I18N (internationalization) may be found at [Internationalization Support](https://wiki.duraspace.org/pages/viewpage.action?pageId=19006307)

Documentation for each release may be viewed online or downloaded via our [Documentation Wiki](https://wiki.duraspace.org/display/DSDOC/).

## Contributing

DSpace is a community built and supported project. We do not have a centralized development or support team,
but have a dedicated group of volunteers who help us improve the software, documentation, resources, etc.

We welcome contributions of any type. Here's a few basic guides that provide suggestions for contributing to DSpace:
* [How to Contribute to DSpace](https://wiki.duraspace.org/display/DSPACE/How+to+Contribute+to+DSpace): How to contribute in general (via code, documentation, bug reports, expertise, etc)
* [Code Contribution Guidelines](https://wiki.duraspace.org/display/DSPACE/Code+Contribution+Guidelines): How to give back code or contribute features, bug fixes, etc.
* [DSpace Community Advisory Team (DCAT)](https://wiki.duraspace.org/display/cmtygp/DSpace+Community+Advisory+Team): If you are not a developer, we also have an interest group specifically for repository managers. The DCAT group meets virtually, once a month, and sends open invitations to join their meetings via the [DCAT mailing list](https://groups.google.com/d/forum/DSpaceCommunityAdvisoryTeam).

We also encourage GitHub Pull Requests (PRs) at any time. Please see our [Development with Git](https://wiki.duraspace.org/display/DSPACE/Development+with+Git) guide for more info.

In addition, a listing of all known contributors to DSpace software can be
found online at: https://wiki.duraspace.org/display/DSPACE/DSpaceContributors

## Getting Help

DSpace provides public mailing lists where you can post questions or raise topics for discussion.
We welcome everyone to participate in these lists:

* [dspace-community@googlegroups.com](https://groups.google.com/d/forum/dspace-community) : General discussion about DSpace platform, announcements, sharing of best practices
* [dspace-tech@googlegroups.com](https://groups.google.com/d/forum/dspace-tech) : Technical support mailing list. See also our guide for [How to troubleshoot an error](https://wiki.duraspace.org/display/DSPACE/Troubleshoot+an+error).
* [dspace-devel@googlegroups.com](https://groups.google.com/d/forum/dspace-devel) : Developers / Development mailing list

Additional support options are listed at https://wiki.duraspace.org/display/DSPACE/Support

DSpace also has an active service provider network. If you'd rather hire a service provider to
install, upgrade, customize or host DSpace, then we recommend getting in touch with one of our
[Registered Service Providers](http://www.dspace.org/service-providers).

## Issue Tracker

The DSpace Issue Tracker can be found at: https://jira.duraspace.org/projects/DS/summary

## License

DSpace source code is freely available under a standard [BSD 3-Clause license](https://opensource.org/licenses/BSD-3-Clause).
The full license is available at http://www.dspace.org/license/
