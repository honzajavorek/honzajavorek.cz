from pathlib import Path
import importlib.util
from types import ModuleType

import click


class SettingsModuleParam(click.ParamType):
    name = "settings-module"

    def convert(self, value, param, ctx) -> ModuleType:
        settings_path = Path(value).resolve()
        if not settings_path.exists() or not settings_path.is_file():
            self.fail(f"Settings file does not exist: {settings_path}", param, ctx)
        module_name = settings_path.stem
        spec = importlib.util.spec_from_file_location(module_name, settings_path)
        if spec is None or spec.loader is None:
            self.fail(f"Unable to load settings file: {settings_path}", param, ctx)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
