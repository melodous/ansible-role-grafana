.. vim: foldmarker=[[[,]]]:foldmethod=marker

pip ansible role default variables
==================================

.. contents:: Sections
   :local:

grafana packaging
------------------

.. envvar:: grafana_docker_imagen

   grafana docker image

::

  grafana_docker_image: melodous/grafana




.. envvar:: grafana_version

   grafana docker image version (TAG)

::

  grafana_version: 4.3.2




.. envvar:: grafana_docker_labels

   Yaml dictionary which maps Docker labels.
   os_environment: Name of the environment, example: Production, by default "default".
   os_contianer_type: Type of the container, by default grafana.

::

  grafana_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_container_type: grafana




grafana configuration
----------------------

.. envvar:: grafana_group

   grafana group name

::

  grafana_group: grafana




.. envvar:: grafana_group_id

   grafana group id

::

  grafana_group_id: 107




.. envvar:: grafana_user

   grafana user name

::

  grafana_user: grafana




.. envvar:: grafana_user_id

   grafana user id

::

  grafana_user_id: 104





grafana monitoring management
------------------------------

.. envvar:: grafana_monitoring

   Enable or disable grafana monitoring
   ::

     grafana_monitoring: true



