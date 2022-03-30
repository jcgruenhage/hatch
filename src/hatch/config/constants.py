class AppEnvVars:
    ENV = 'HATCH_ENV'
    ENV_ACTIVE = 'HATCH_ENV_ACTIVE'
    QUIET = 'HATCH_QUIET'
    VERBOSE = 'HATCH_VERBOSE'
    INTERACTIVE = 'HATCH_INTERACTIVE'
    PYTHON = 'HATCH_PYTHON'
    # https://no-color.org
    NO_COLOR = 'NO_COLOR'
    FORCE_COLOR = 'FORCE_COLOR'


class ConfigEnvVars:
    PROJECT = 'HATCH_PROJECT'
    DATA = 'HATCH_DATA_DIR'
    CACHE = 'HATCH_CACHE_DIR'
    CONFIG = 'HATCH_CONFIG'


class PublishEnvVars:
    USER = 'HATCH_PYPI_USER'
    AUTH = 'HATCH_PYPI_AUTH'
    REPO = 'HATCH_PYPI_REPO'
    PUBLISHER = 'HATCH_PUBLISHER'
    OPTIONS = 'HATCH_PUBLISHER_OPTIONS'