def test_grafana_server_running_and_enabled(Command, Service):
    # Check that docker service is running and enabled
    docker_service = Service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled
    # Check that grafana service is running and enabled
    grafana_service = Service("grafana")
    assert grafana_service.is_running
    assert grafana_service.is_enabled


def test_grafana_start_stop(Command, Service):
    Command.run_expect([0], "systemctl stop grafana")
    grafana_service = Service("grafana")
    assert not grafana_service.is_running
    Command.run_expect([0], "systemctl start grafana")
    assert grafana_service.is_running
    Command.run_expect([0], "systemctl restart grafana")
    assert grafana_service.is_running
