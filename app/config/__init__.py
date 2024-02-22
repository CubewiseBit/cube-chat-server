"""
Copyright 2024 Maner·Fan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from types import MappingProxyType

from .config_loader import safe_load
from .loguru_config import loguru_config
from .opentelemetry_config import ot_config, ot_instrument_loguru

app_config = MappingProxyType(safe_load('./config.yml'))

__all__ = [
    app_config,
    loguru_config,
    ot_config,
    ot_instrument_loguru,
]
