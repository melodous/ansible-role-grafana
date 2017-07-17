Welcome to grafana Ansible Role’s documentation!
================================================

Role Name
---------

Ansible role to install and configure grafana as container

### Requirements

Docker engine up and runnig

### Dependencies

N/A

### Example Playbook

    - hosts: servers
      roles:
        - { role: grafana }

pip ansible role default variables
----------------------------------

#### Sections

-   grafana packaging
-   grafana configuration
-   grafana monitoring management

### grafana packaging

`grafana_docker_imagen`

> grafana docker image

    grafana_docker_image: melodous/grafana

`grafana_version`

> grafana docker image version (TAG)

    grafana_version: 4.3.2

`grafana_docker_labels`

> Yaml dictionary which maps Docker labels. os\_environment: Name of the
> environment, example: Production, by default “default”.
> os\_contianer\_type: Type of the container, by default grafana.

    grafana_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_container_type: grafana

### grafana configuration

`grafana_group`

> grafana group name

    grafana_group: grafana

`grafana_group_id`

> grafana group id

    grafana_group_id: 107

`grafana_user`

> grafana user name

    grafana_user: grafana

`grafana_user_id`

> grafana user id

    grafana_user_id: 104

### grafana monitoring management

`grafana_monitoring`

> Enable or disable grafana monitoring
>
>     grafana_monitoring: true

Changelog
---------

**grafana**

This project adheres to Semantic Versioning and human-readable
changelog.

### grafana master - unreleased

##### Added

-   First addition

##### Changed

-   First change

### grafana v0.0.2 - 2017/07/17

##### Changed

-   Fixed playbook.yml

### grafana v0.0.1 - 2017/07/13

##### Added

-   Initial version

Copyright
---------

grafana

Copyright (C) 2017/07/13 Raúl Melo
&lt;<raul.melo@opensolutions.cloud>&gt;

LICENSE
