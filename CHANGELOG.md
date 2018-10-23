# Changelog

## v3.3.0 (unreleased)

* Feature: Support for block storage volumes in GCE, EC2, Openstack, DigitalOcean
* Feature: Automatic db migrations
* Feature: Display org logo in user menu
* Feature: Resize GCE machines
* Feature: Allow to create multiple interfaces and assign static IPs to KVM guest VMs
* Feature: Implement VM cloning for KVM
* Feature: Support snapshots in vSphere
* Feature: Allow to enable/disable and edit the window/frequency of a NoDataRule
* Feature: Saved searches in log listings
* Feature: Cloud listing page
* Change: Use html5 date & time inputs
* Change: Improve performance when applying patches to the model over websocket
* Change: Reduce poller update threshold to 90 secs
* Change: Add k8s deployment specific script that displays online portal users
* Bugfix: Properly pass params when running scheduled scripts
* Bugfix: Display prices in resize dialog correctly for DigitalOcean
* Bugfix: Fix required machine fields when creating stacks
* Change: Reduce poller update threshold to 90 secs

## v3.2.0 (6 Aug 2018)

Performance optimizations, use existing machines when creating stacks, preliminary support for Alibaba Cloud (Aliyun ECS), minor bugfixes.

* Feature: Allow using existing machines in stacks instead of provisioning new ones
* Feature: Initial support for Alibaba Cloud
* Feature: Configure default post deploy steps for selected clouds
* Feature: Support VNC console action on OpenStack
* Bugfix: Fix influxdb mountpath in helm chart
* Bugfix: Fix VCloud OS detection
* Bugfix: Fix vSphere machine listing issue
* Bugfix: Fix load graph for many machines
* Change: Expose more settings for rabbitmq, gocky, cilia in helm chart
* Change: Upgrade gocky images
* Change: Configurable pollers in helm chart
* Change: Add flag to disable machine polling acceleration
* Change: Optimize tag query when calculating machine cost
* Change: Re-implement metering for checks and datapoints based on rate/sec
* Change: Dont probe stopped machines or localhost
* Change: Dont run update_poller task if not necessary
* Change: Import middleware chains from plugins, if defined
* Change: Make scheduler configurable in bin/poller

## v3.1.1 (19 Jul 2018)

Minor bugfix release

* Bugfix: Stack page display after installing new template
* Bugfix: Fix KeyError exception which could happen when a user does not belong to any team
* Bugfix: Updating an org would sometimes toggle the ownership flag

## v3.1.0 (16 Jul 2018)

Adds polling for networks. Improves KVM machine creation & networking. Optimize vSphere API queries. Improves DB query performance. Upgrades ELK which lowers RAM requirements.

### Changes

* Feature: Add templates from any Git repo
* Bugfix: Fix KVM networks upon machine creation.
* Bugfix: Prevent setting telegraf deployment error to "None"
* Bugfix: Do not schedule MeteringPollingSchedule task immediately, since that would result in the task being scheduled every time the Organization instance is saved
* Bugfix: Fix bug regarding incidents not closing when disabling monitoring

## v3.0.0 (27 June 2018)

Major new release of the Mist Cloud Management Platform.

Mist now integrates with Telegraf & InfluxDB to provide a fully open source infrastructure management & monitoring stack. It also includes a revamped alerting & automation engine that will apply your rules to any group of machines. We enhanced the support of many clouds, most notably vSphere, GCE & OpenStack. It's now possible to bring together machines into a single virtual "Cloud". The usability and performance of the UI was greatly improved. At the same time we've remorselessly eliminated more than a few bugs.

A new plugin system was introduced, which is currently used by the Enterprise Edition and the Hosted Service to provide add-on functionality like i) Role Based Access Control, ii) Cost Insights, iii) VPN tunnels, iv) Orchestration of multi-tier architectures like Kubernetes clusters, as well as v) metering & billing extensions.

You can purchase a license for the Mist Enterprise Edition and a subscription for the Mist Hosted Service at https://mist.io

Adds polling for networks. Improves KVM machine creation & networking. Optimize vSphere API queries. Improves DB query performance. Upgrades ELK which lowers RAM requirements.

### Changes

* Feature: Allow private ownership of resources
* Feature: Machine monitoring, using InfluxDB & Telegraf
* Feature: Alerting and automation rules on machine metrics, apply rules on groups of machines
* Feature: Interactive API docs using OpenAPI 3.0 spec & Swagger UI
* Feature: Poller for cloud locations & sizes
* Feature: Select network & subnetwork when creating GCE machine
* Feature: Support ClearCenter SDN as cloud
* Change: Improved vSphere support
* Change: UI performance improvements
* Change: Support for plugins
* Feature: Support custom sizes when creating KVM machines.
* Feature: Store & display resource creator & owner
* Feature: Allow to undefine a KVM domain, if it is not active
* Feature: Support multiple interfaces and attaching to more than one networks when creating KVM machines.
* Feature: Poller for networks.
* Change: Sharding of polling tasks.
* Change: Deprecate collectd support.
* Change: Support metering of datapoints.
* Change: Add owner index, improves performance of DB queries.
* Change: Upgrade ELK to 5.6.10
* Change: Get vm properties in batches in vSphere driver
* Bugfix: Fix internal server error when editing some rules.
* Change: Improve layout in small screens
* Bugfix: Update required fields for provisioning in OpenStack
* Change: Remove deprecated polling tasks
* Bugfix: Fix create stack perm check
* Bugfix: Fix machine resize action, rename plan_id to size_id
* Bugfix: Update OpenStack imported key naming scheme
* Bugfix: Fail gracefully when listing networks and cloud does not respond
* Change: Use OpenStack auth URL without force
* Change: Look for and assign portgroup to nic on vSphere provisioning
* Bugfix: Redirect to social auth on invite if email signin is disabled
* Change: Add swagger service in ee docker-compose
* Feature: Networks RBAC
* Change: Openapi spec (!691)
* Change: Story patches
* Change: Send machine patches in batches and optimize parsing
* Change: Only return rds enabled clusters as vSphere locations if available
* Change: Allow users & teams to be specified as e-mail alert recipients
* Change: Update notifications api & notification patches
* Change: Add mongodb index for monitored machines
* Change: Hide empty location fields
* Change: Display cloud instead of provider in networks list
* Bugfix: Refit run script dialog on params change
* Bugfix: Update keys in sub-form element

## v2.12.0 (15 Feb 2018)

### Changes

* Change: Get datacenter from cluster when provisioning in vSphere
* Bugfix: Fix backwards compatible computed properties of Rule model
* Bugfix: Fix primary key of the PeriodicTaskInfo document
* Change: Remove ListLocationsPollingSchedule from the update_poller task
* Change: Stop writing logs to mongoDB
* Change: Add an index on the Organization's name field


## v2.11.0 (14 Feb 2018)

### Changes

* Feature: Provisioning in vSphere cluster when RDS is enabled
* Bugfix: Fix rendering of delete network action

## v2.10.1 (12 Feb 2018)

### Changes

* Bugfix: Correctly get DigitalOcean image id in machine listing
* Bugfix: Compute dashboard chart labels on all monitored machine list updates

## v2.9.0 (6 Feb 2018)

### Changes

* Feature: Improve vSphere support (provisioning, VNC console, display more metadata)
* Feature: Support ClearCenter SDN as cloud
* Feature: Support multiple hosts in other server clouds
* Feature: Fine grained notification overrides
* Change: Improve alert email notifications
* Change: Split celery into a gevent and prefork worker in docker-compose.ee.yml
* Change: Move RBAC & billing plugins to their own submodules
* Change: Cilia: InfluxDB & multi-monitoring
* Change: Rbac plugin
* Change: More pep8 fixes
* Change: Garbage collection for schedulers
* Change: Traefik v1.4
* Change: Split poller
* Change: Multi monitoring
* Change: Use poller for listing locations
* Change: Return cached data by default when requesting all machines over API

## v2.8.0 (10 Dec, 2017)

### Changes

* Feature: Export CSV on any list
* Bugfix: Do not require payment if Stripe is not configured
* Change: Localmail for tests
* Change: Improve layout in small screens
* Change: Do not use CELERY_CONTEXT when celery uses a gevent pool of workers
* Change: Cilia
* Change: Small tweak in insights-handler
* Bugfix: Fix tag regex for pushing ee image in CI
* Bugfix: Update required fields for provisioning in OpenStack
* Change: Remove deprecated polling tasks

## v2.7.0 (18 Nov 2017)

* Feature: Chained actions in Rules, backend only
* Feature: CSV renderer for API results
* Feature: Send multipart emails when required
* Feature: List all machines view
* Change: Dismiss notifications menu
* Change: Async session update
* Change: Vsphere opts and metadata
* Bugfix: Catch me.NotUniqueError when renaming a Cloud


## v2.6.0 (27 Oct 2017)

### Changes

* Feature: Azurearm provisioning
* Feature: Improved Windows support
* Feature: Granular Notification Overrides
* Feature: Resize machine action for EC2, DigitalOcean, OpenStack
* Bugfix: Fix lock bug https://gitlab.ops.mist.io/mistio/mist.core/issues/1221
* Bugfix: Properly read cost from tags for generic (non-libcloud) machines
* Bugfix: Fix ping parsing
* Bugfix: Fix poller computed property
* Change: Update xterm.js & fix shell display issues
* Change: Improve display of probe data
* Change: Exclude audit log ES templates
* Change: Run tests with headless Chrome
* Change: New rules models
* Change: Sso refresh token
* Change: Update docker/nginx/nginx.conf
* Change: Move ES template for cloudify-metrics to mist.io/docker/elasticsearch-manage

