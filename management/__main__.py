from management import RUN_MODE


if RUN_MODE == 0:
    import management.cmd
else:
    import management.gui
