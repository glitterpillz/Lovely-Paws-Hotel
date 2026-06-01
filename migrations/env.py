from __future__ import with_statement

import logging
from logging.config import fileConfig
import os

from alembic import context
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy import pool


environment = os.getenv("FLASK_ENV")
# SCHEMA = os.environ.get("SCHEMA")

config = context.config

fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")

config.set_main_option(
    "sqlalchemy.url",
    str(current_app.extensions["migrate"].db.engine.url).replace("%", "%%"),
)

target_metadata = current_app.extensions["migrate"].db.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, "autogenerate", False):
            script = directives[0]

            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info("No changes in schema detected.")

    database_url = current_app.config["SQLALCHEMY_DATABASE_URI"]

    connectable = create_engine(
        database_url,
        poolclass=pool.NullPool,
        connect_args={"sslmode": "require"} if environment == "production" else {},
    )

    with connectable.connect() as connection:
        # if environment == "production" and SCHEMA:
        #     connection.exec_driver_sql(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA}")

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,
            **current_app.extensions["migrate"].configure_args,
        )

        with context.begin_transaction():
            # if environment == "production" and SCHEMA:
            #     context.execute(f"SET search_path TO {SCHEMA}")

            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()