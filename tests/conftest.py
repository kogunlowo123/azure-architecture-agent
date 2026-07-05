"""Test configuration for Azure Architecture Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "azure-architecture-agent", "category": "Cloud Engineering"}
