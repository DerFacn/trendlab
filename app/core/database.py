from flask import Flask, g
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Database:
    """
    Database UoW (Unit of Work)  
    Provides all the functions for proper database connection and session management.
    """
    def __init__(self) -> None:
        self.Base = Base
            
    def init_app(self, app: Flask) -> None:
        self.app = app
        
        self.database_url = app.config.get("DATABASE_URL")

        self.engine: Engine | None = None
        self.SessionFactory = None

        if not self.database_url:
            raise Exception('DATABASE_URL variable must be set!')
        
        self.engine = create_engine(
            self.database_url,
            echo=False
        )
        self.SessionFactory = sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            class_=Session,
        )

        self._register_hooks()

    def init_db(self):
        if self.engine:
            with self.engine.begin() as conn:
                self.Base.metadata.create_all(bind=conn)

        else:
            raise RuntimeError("No DATABASE_URL is provided.")

    def _register_hooks(self):

        @self.app.before_request
        def _open_session():
            if self.SessionFactory:
                g.session = self.SessionFactory()
            else:
                g.session = None

        @self.app.after_request
        def _close_session(response):
            session = g.pop("session", None)
            if session:
                session.close()
            return response

        @self.app.teardown_request
        def _teardown(exc):
            session = g.pop("session", None)
            if session:
                session.close()

    def get_sync_session(self) -> Session:
        if not self.SessionFactory:
            raise RuntimeError("Sync engine is not configured.")
        return self.SessionFactory()
