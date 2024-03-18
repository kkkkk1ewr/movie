# -*- coding: utf-8 -*-

import os

env = os.environ.get("api_env", "develop").lower()
print(" API Project's system environment is under: {}".format(env))

if env == "develop":
    from config.develop import DevelopConfig

    config = DevelopConfig


elif env == "production":
    from config.production import ProductionConfig

    config = ProductionConfig
else:
    from config.develop import DevelopConfig

    config = DevelopConfig
