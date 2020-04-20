"""Services Application Entry Point

This file is the actual "FLASK_APP" file. It runs migrations,
initializes the app, and has tools for creating a shell
context for testing.
"""
from app import create_app
APP = create_app()


@APP.shell_context_processor
def make_shell_context():
    """Generate a shell context for testing

    Returns
    -------
    dict
        Dictionary of objects to include in shell session
    """
    return {'app': APP}


@APP.cli.command()
def deploy():
    """Run deployment tasks."""
    # No deployment tasks on sample
    pass
