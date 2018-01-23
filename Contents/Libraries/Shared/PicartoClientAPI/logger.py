
PICARTO_API_ = "[PicartoAPI] %s"
Log = None


class Logger(object):
    def debug(self, msg, *args, **kwargs):
        Log.Debug(PICARTO_API_ % msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        Log.Info(PICARTO_API_ % msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        Log.Warning(PICARTO_API_ % msg, *args, **kwargs)


LOG = Logger()
